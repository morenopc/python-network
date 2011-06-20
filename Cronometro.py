import time

class Cronometro():

    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def iniciar(self):
        self.__inicio = time.time()

    def parar(self):
        self.__fim = time.time()
        return self.__fim - self.__inicio

    def zerar(self):
        self.__inicio = 0
        self.__fim = 0
        
