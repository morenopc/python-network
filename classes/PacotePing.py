class PacotePing():
  
        "@param tipo: Tipo do pacote"
        "@param codigo: Codigo do pacote"
        def __init__(self, tipo, codigo):
                self.__tipo = tipo
                self.__codigo = codigo
                self.__id = ""
                self.__numSeq = None
                self.__dados = None
                self.__ttl = 255

        "@param tipo: Tipo do pacote"
        def setTipo(self, tipo):
                self.__tipo = tipo
            
        def getTipo(self):
                return self.__tipo

        "@param codigo: Codigo do pacote"
        def getCodigo(self, codigo):
                self.__codigo = codigo

        def getCodigo(self):
                return self.__codigo

        "@param ID: ID do pacote"
        def setID(self, ID):
                self.__id = ID

        def getID(self):
                return self.__id

        "@param numSeq: Numero de sequecia do pacote"
        def setnumSeq(self, numSeq):
                self.__numSeq = numSeq
                        
        def getnumSeq(self):
                return self.__numSeq
            
        "@param dados: Dados do pacote"
        def setDados(self, dados):
                self.__dados = dados

        def getDados(self):
                return self.__dados

        "@param ttl: TTL do pacote"
        def setTtl(self, ttl):
                self.__ttl = ttl

        def getTtl(self):
                return self.__ttl
