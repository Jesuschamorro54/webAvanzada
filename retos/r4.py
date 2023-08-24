def guard(function):
    
    def wrapper(*args, **kwargs):

        view_access = {
            'delete_user': ('supadmin'),
            'home': ('free', 'supadmin', 'admin'),
            'create_user': ('admin', 'supadmin')
        }

        view = str(function).split(" ")[1]
        user = args[0] if args else kwargs
        session = user['session']

        print(user)

        if session['token']:

            if user['role'] in view_access[view]:
                function(*args)
            else:
                print("No tienes permisos")

        else:
            loggin()

    return wrapper
    



def loggin():
    print("Entré al login")


@guard
def home(user):
    print("Entre al home")


@guard
def delete_user(user):
    print("Usuario Eliminado")


@guard
def create_user(user):
    print("Usuario creado") 




user = {
    'email': "jesus@gmail.com",
    'role': 'free',  # free - admin - supadmin
    
    # TODO

    'session': {
        'token': True

        # TODO
    } 
    
}



delete_user(user)