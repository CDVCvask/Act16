from xmlrpc.client import DateTime


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
class Mod_Book:
    def __init__(self):
        self.books = []
    def Show(self):
        pass
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
            acutal = DateTime.now().year
            count = 0
            print("Ingreso de libros")
            print(" ")
            num = int(input("Cuantos libros desae ingresar: "))
            if num <= 0:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    title = input("Ingrese el titulo del libro: ")
                    author = input("Ingrese el autor del libro: ")
                    year = int(input("Ingrese el año de publicación del libro:"))
                    if year <= 0 or year > acutal:
                        print("La cantidad ingresada no es valida")
                    else:
                        code = f"B{count}"
                        aviable = True
                        bood = Book(title,author,year,code,aviable)
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