from Rota import Rota
from IP import IP

# Route table
class TabelaRotas():

    def __init__(self):
        self.__ip = IP()
        self.__listaRotas = []
        self.__default = None

    "@param ip: destination host ip"
    def encontrarRota(self, ip):
        
        # Routing algorithm
        for linha in self.__listaRotas:
            if linha.getDestino() == self.__ip.netID(ip, linha.getMascara()):
                return linha
        return None

    def getLRotas(self):
        return self.__listaRotas    
    
    "@param rota: new route"
    def addRota(self, rota):
        self.__listaRotas.append(rota)

    "@param ip: ip to remove route"
    def removeRota(self, ip):
        for linha in self.__listaRotas:
            if linha.getDestino() == ip:
                self.__listaRotas.remove(linha)
                return True
            else:
                return False
    
    "@param rota: default route"
    def setRotaDefault(self, rota):
        self.__default = rota

    def getRotaDefault(self):
        return self.__default
