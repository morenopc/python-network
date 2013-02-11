# Frame
class Quadro():
  
        "@param origem: source frame MAC"
        "@param tamanho: frame size"
        def __init__(self, origem, tamanho):
                self.__origem = origem
                self.__destino = ""
                self.__tamanho = tamanho
                self.__dados = None
                self.__tipo = 0

        "@param dados: frame data"
        def setDados(self, dados):
                self.__dados = dados

        def getDados(self):
                return self.__dados

        "@param destino: destination MAC"
        def setDestino(self, destino):
                self.__destino = destino
                        
        def getDestino(self):
                return self.__destino

        "@param origem: source MAC"
        def setOrigem(self, origem):
                self.__origem = origem

        def getOrigem(self):
                return self.__origem

        "@param tipo: frame type"
        def setTipo(self, tipo):
                self.__tipo = tipo

        def getTipo(self):
                return self.__tipo

        "@param tipo: frame size"
        def setTamanho(self, tamanho):
                self.__tamanho = tamanho

        def getTamanho(self):
                return self.__tamanho
