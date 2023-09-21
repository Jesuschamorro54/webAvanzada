# MODEL

from Config.db import db, app, ma

class Prestamista(db.Model):
    __tablename__ = "tblprestamista"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))

    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(15))
    monto_disponible = db.Column(db.Double)
    

    def __init__(self, nombre):
        self.nombre = nombre

with app.app_context():
    db.create_all()

class PrestamistaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'direccion', 'telefono', 'monto_disponible')
        