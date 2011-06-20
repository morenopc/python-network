# Route Table line
class Rota():

    "@param dest: destination IP"
    "@param route: destination router IP"
    "@param mascara: destination netmask"
    "@param metrica: answer time"
    "@param iFace: network equipment MAC"
    def __init__(self, dest, route, mascara, metrica, iFace):
        self.__dest = dest
        self.__route = route
        self.__mascara = mascara
        self.__metrica = metrica
        self.__iFace = iFace

    "@param dest: destination IP"
    def setDestino(self, dest):
        self.__dest = dest

    def getDestino(self):
       return self.__dest

    "@param route: destination router IP"
    def setRoute(self, route):
        self.__route = route

    def getRoute(self):
       return self.__route

    "@param mascara: destination netmask"
    def setMascara(self, mascara):
        self.__mascara = mascara

    def getMascara(self):
       return self.__mascara

    "@param metrica: answer time"
    def setMetrica(self, metrica):
        self.__metrica = metrica

    def getMetrica(metrica):
       return self.__metrica

    "@param iFace: network equipment MAC"
    def setIFace(self, iFace):
        self.__iFace = iFace

    def getIFace(self):
       return self.__iFace
