from Quadro import Quadro
from Pacote import Pacote

class ARP():

    "@param host: Host a que o ARP pertence"    
    def __init__(self, host):
        self.__host = host
        self.__quadroRecebido = []
        self.__novoQuadro = None

    "@param quadro: Quadro recebido do Host"
    def arpSolicita(self, quadro):
        # Guarda o quadro
        self.__quadroRecebido.append(quadro)

        pacote = quadro.getDados()
        # Cria pacote ARP-Solicita
        pacote_ARP = Pacote(pacote.getIPOrigem(), 12)
        pacote_ARP.setIPDestino(pacote.getIPDestino())
        pacote_ARP.setDados("ARP-Solicita")

        # Cria quadro ARP-Solicita
        # Retorna Quadro ARP-Solicita montado
        return self.__host.constroiQuadro(24, "FFFFFFFFFFFF", pacote_ARP)

    "@param ip: IP origem do Quadro recebido do Host"
    "@param mac: MAC origem do Quadro recebido do Host"
    def arpResponde(self, ip, mac):
        
        # Cria quadro ARP-Responde
        # Retorna Quadro ARP-Responde montado
        pac = self.__host.constroiPacote(12, self.__host.getIP(), "ARP-Responde")
        pac.setIPDestino(ip)
        quad = self.__host.constroiQuadro(24, self.__host.getMAC(), pac)
        quad.setDestino(mac)
        return quad

    "@param ip: IP origem do Quadro recebido do Host"
    "@param mac: MAC origem do Quadro recebido do Host"
    def recuperaQuadro(self, ip, mac):
        for quadro in self.__quadroRecebido:
            pacote = quadro.getDados()
            if pacote.getIPDestino() == ip:
                quadro.setDestino(mac)
                return self.__quadroRecebido.pop(self.__quadroRecebido.index(quadro))
        return None