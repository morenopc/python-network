class TabelaARP():
# Tabela com as relacoes entre o IP e o MAC
  
        "@param ip: IP "
        "@param mac: MAC"
        def __init__(self, ip, mac):
                self.__ip = ip
                self.__mac = mac

        "@param ip: IP a ser modificado"
        def setIP(self, ip):
                self.__ip = ip

        def getIP(self):
                return self.__ip

        "@param mac: MAC a ser modificado"
        def setMAC(self, mac):
                self.__mac = mac
                        
        def getMAC(self):
                return self.__mac
