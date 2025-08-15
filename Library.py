from xmlrpc.client import DateTime


def Menu():
    print(" ")
    print("Bienvenido a la biblioteca")
    print("1.Registrar libro ")
    print("2.Registrar usuario")
    print("3.Mostrar libros")
    print("4.Mostrar usuarios")
    print("5.Prestamo de libro")
    print("6.Devolucion de libro")
    print("7.Mostrar prestamos")
    print("8.Salir")
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
        cont = 1
        if len(self.books) < 1:
            print("No hay libros para mostrar")
        else:
            for Book in self.books:
                print(f"Libro {cont}")
                print(f"Titulo {Book.title},Autor: {Book.author},Año de publicacion: {Book.year},Código: {Book.code},Disponible: {Book.aviable}")
                cont += 1
    def AddBook(self, book):
        self.books.append(book)
class User:
    def __init__(self, username, code,carrer):
        self.username = username
        self.password = code
        self.carrer = carrer
class Mod_User:
    def __init__(self):
        self.users = []
allow = False
exit = 0
Mod_Book = Mod_Book()
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    match opt:
        case 1:
            #acutal = DateTime.now().year
            count = 0
            cont = 1
            print("Ingreso de libros")
            print(" ")
            num = int(input("Cuantos libros desae ingresar: "))
            if num <= 0:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    print(" ")
                    print(f"Ingreso del libro {cont}")
                    title = input("Ingrese el titulo del libro: ")
                    author = input("Ingrese el autor del libro: ")
                    year = int(input("Ingrese el año de publicación del libro:"))
                    if year <= 0 :
                        print("La cantidad ingresada no es valida")
                    else:
                        code = f"B{count}"
                        aviable = True
                        book = Book(title,author,year,code,aviable)
                        Mod_Book.AddBook(book)
                        cont = cont + 1
                        count = count + 1
        case 2:
            Mod_Book.Show()
        case 3:
            cont = 1
            countU = 0
            num = int(input("cuantos usuarios va a ingresar? "))
            if num <= 0:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    print(" ")
                    print(f"Ingreso del usuario {cont}")
                    u_name = input("Ingrese el nombre del usuario: ")
                    carrer = input("Ingrese la carrera del usuario: ")
                    ucode= f"U{countU}"
                    user = User(u_name,ucode,carrer)
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            while 1 != 0:
                check = input("Está seguro de que desea salir de la aplicación?(S/N) ")
                if check.upper() == "S":
                    print("Gracias por utilizar el programa")
                    exit = 1
                    break
                elif check.upper() == "N":
                    print("Regresando el Menu")
                    break
                else:
                    print("La opción seleccionada no es valida")
        case _:
            print("La opción seleccionada no es valida")
    if exit == 1:
        break