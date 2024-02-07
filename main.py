class delegado:
    def tiempocCompleto(salario):
        return salario  + (salario * 0.10)
    def temporal(salario):
        return salario + (salario * 0.05)
    def parcial(salario):
        return salario
    #delegado
    def ejecutar_Funcion(func, salario):
        return func(salario)
class Empleado:
    def __init__(self, nombre, salario, tipo):
        self.nombre = nombre
        self.salario = salario
        self.tipo = tipo
    def calcularSalario(self):
        if self.tipo == "Completo":
            return delegado.ejecutar_Funcion(delegado.tiempocCompleto, self.salario)
        elif self.tipo == "Temporal":
            return delegado.ejecutar_Funcion(delegado.temporal, self.salario)
        else:
            return delegado.ejecutar_Funcion(delegado.parcial, self.salario)

class Main:
    empleado1 = Empleado("Juan", 1000, "Completo")
    empleado2 = Empleado("Maria", 1000, "Temporal")
    empleado3 = Empleado("Pedro", 1000, "Parcial")

    print(empleado1.tipo," | ", empleado1.nombre, " | ", empleado1.calcularSalario())
    print(empleado2.tipo," | ", empleado2.nombre, " | ", empleado2.calcularSalario())
    print(empleado3.tipo," | ", empleado3.nombre, " | ", empleado3.calcularSalario())

