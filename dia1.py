class Main:
    def __init__(self):
        pass


'''
la clase Main mediante el método mensaje() llama a mensaje2() de Second

MAIN        SECOND
  | mensaje()  |
  |----------->[]---|
  | mensaje2() []   |
  |<-----------[]<--|
  |            |
  MAIN       SECOND

'''
    def mensaje(self, mensaje):
        if isinstance(mensaje, str):
            return Second().mensaje2(mensaje)
        else:
            raise TypeError("Error")

    def __str__(self):
        return "Class Main"


class Second:
    def __init__(self):
        pass

    def mensaje2(self, mensaje):
        return mensaje

    def __str__(self):
        return "Class Second"


if __name__ == "__main__":
    main = Main()
    print(main.mensaje("Hola Mundo"))

