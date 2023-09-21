# MODEL

from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key = True)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    fecha_prestamo = db.Column(db.Double)
    total = db.Column(db.Double)

    def __init__(self, idCliente):
        self.idCliente = idCliente

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente', 'fecha_prestamo', 'total')
        