class Main:
    def __init__(self):
        self.calc = Calc()
        self.visor = Visor()

    def callSuma(self, num1, num2):
        resultado = self.calc.suma(num1, num2)
        self.visor.imprimir(resultado)
        return resultado

    def __str__(self):
        return "Clase Main"


class Calc:
    def suma(self, num1, num2):
        return num1 + num2

    def __str__(self):
        return "Clase Calc"


class Visor:
    def imprimir(self, valor):
        print(f"Resultado: {valor}")
        return True

    def __str__(self):
        return "Clase Visor"


if __name__ == '__main__':
    Main().callSuma(1, 2)
