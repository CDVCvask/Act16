def Menu():
    print("Bienvenido a la biblioteca")
    print("1.Registrar libro ")
    print("2.Registrar usuario")
    print("3.Prestamo de libro")
    print("4.Devolucion de libro")
    print("5.Salir")
class Book:
    def __init__(self, title, author, year,code,aviable):
        self.title = title
        self.author = author
        self.year = year
        self.code = code
        self.aviable = aviable
class User:
    def __init__(self, username, code,carrer):
        self.username = username
        self.password = code
        self.carrer = carrer
allow = False
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case _:
            pass