class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def mostrar_resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}")

# Crear objetos de la clase Alumno
alumno1 = Alumno("Juan Pérez", 7)
alumno2 = Alumno("María López", 4)

# Imprimir los datos de los alumnos y mostrar el resultado
# alumno1.imprimir_datos()
# alumno1.mostrar_resultado()

# alumno2.imprimir_datos()
# alumno2.mostrar_resultado()


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
         return max(self.lado1, self.lado2, self.lado3)
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_datos(self):
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")

triangulo1 = Triangulo(4,7,5)
triangulo2 = Triangulo(5,5,5)

# triangulo1.imprimir_datos()
# triangulo2.imprimir_datos()

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def division(self):
        return self.num1 / self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    

calculo1 = Calculadora(10, 2)

# print(calculo1.suma())
# print(calculo1.resta())
# print(calculo1.division())
# print(calculo1.multiplicacion())

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        print("Contacto agregado exitosamente.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. {contacto['nombre']} - {contacto['telefono']} - {contacto['email']}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                print(f"Contacto encontrado:\n{contacto}")
                return
        print(f"No se encontró el contacto {nombre}.")

    def editar_contacto(self, nombre, nuevo_telefono=None, nuevo_email=None):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                if nuevo_telefono:
                    contacto['telefono'] = nuevo_telefono
                if nuevo_email:
                    contacto['email'] = nuevo_email
                print(f"Contacto {nombre} actualizado exitosamente.")
                return
        print(f"No se encontró el contacto {nombre} para editar.")

    def menu(self):
        while True:
            print("\nMenú de la agenda:")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                nombre = input("Ingrese el nombre: ")
                telefono = input("Ingrese el teléfono: ")
                email = input("Ingrese el email: ")
                self.agregar_contacto(nombre, telefono, email)
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                nombre = input("Ingrese el nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == '4':
                nombre = input("Ingrese el nombre del contacto a editar: ")
                nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco si no desea cambiar): ")
                nuevo_email = input("Ingrese el nuevo email (deje en blanco si no desea cambiar): ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)
            elif opcion == '5':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")

# Crear una instancia de la agenda
# mi_agenda = Agenda()
# mi_agenda.menu()

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"{self.nombre} ha depositado ${cantidad}")

    def extraer(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"{self.nombre} ha extraído ${cantidad}")
        else:
            print("Fondos insuficientes")

    def mostrar_total(self):
        print(f"El saldo de {self.nombre} es: ${self.saldo}")

class Banco:
    def __init__(self):
        self.clientes = [Cliente("Juan"), Cliente("María"), Cliente("Pedro")]
        self.deposito_total = 0

    def operar(self):
        # Simulación de operaciones bancarias (puedes agregar más opciones)
        self.clientes[0].depositar(1000)
        self.clientes[1].extraer(500)
        self.clientes[2].depositar(200)

    def calcular_deposito_total(self):
        for cliente in self.clientes:
            self.deposito_total += cliente.saldo
        return self.deposito_total

# Crear una instancia del banco
banco = Banco()

# Realizar operaciones
banco.operar()

# Mostrar el depósito total
deposito_total = banco.calcular_deposito_total()
print(f"El depósito total del banco es: ${deposito_total}")