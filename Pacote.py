# Packet
class Pacote():
  
        "@param ipOrigem: source packet ip"
        "@param tamanho: packet size"
        def __init__(self, ipOrigem, tamanho):
                self.__ipOrigem = ipOrigem
                self.__ipDestino = ""
                self.__tamanho = tamanho
                self.__dados = None

        "@param dados: packet data"
        def setDados(self, dados):
                self.__dados = dados

        def getDados(self):
                return self.__dados

        "@param ipDestino: destination IP"
        def setIPDestino(self, ipDestino):
                self.__ipDestino = ipDestino
                        
        def getIPDestino(self):
                return self.__ipDestino
            
        "@param ipOrigem: source IP"
        def setIPOrigem(self, ipOrigem):
                self.__ipOrigem = ipOrigem

        def getIPOrigem(self):
                return self.__ipOrigem
