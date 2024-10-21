class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def print_persona(self):
        print(f'Se ha creado {self.nombre} de {self.edad} años.')
    def es_mayor_de_edad(self):
        return self.edad >= 18
    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.edad
    
    @staticmethod # decorador indica que el método no pertenece a una instancia específica de la clase, sino a la clase en sí.
    
    def get_mayor(primer_persona, segunda_persona):
        if primer_persona.edad > segunda_persona.edad:
            return primer_persona
        elif segunda_persona.edad > primer_persona.edad:
            return segunda_persona
        else:
            return None  

# creamos dos personas
persona1 = Persona('Julian', 38)
persona2 = Persona('Julia', 33)
persona3 = Persona('Juan', 45)

#imprimos por pantalla las personas creadas
#persona1.print_persona()
#persona2.print_persona()

# imprimimos si la perona es mayor de edad
#print(persona1.es_mayor_de_edad())

# imprimo si una persona es mayor que la otra persona
#print(persona1.es_mayor_que(persona2))

# imprimo que me devuelva el mayor
#persona_mayor = Persona.get_mayor(persona1, persona3)
#print(persona_mayor.nombre)

