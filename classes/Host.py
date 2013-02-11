from EquipamentoRede import EquipamentoRede
from Quadro import Quadro
from TabelaARP import TabelaARP
from Pacote import Pacote
from ARP import ARP
from ICMP import ICMP

class Host(EquipamentoRede):
    
    def __init__(self):
        EquipamentoRede.__init__(self)
        self.__ARP = ARP(self)
        self.__ICMP = ICMP(self)
        self.__novoQuadro = None
        self.__novoPacote = None
        self.__hostNic = []
        self.__hostListaQuadros = []
        self.__listaARP = []
        self.__ip = ""
        self.__mascara = ""

    "@param ip: Host IP"
    def setIP(self, ip):
        self.__ip = ip

    def getIP(self):
        return self.__ip

    "@param mascara: Host Subnet mask"
    def setMascara(self, mascara):
        self.__mascara = mascara

    def getMascara(self):
        return self.__mascara
                                    
    def getMAC(self):
        self.__hostNic = self.getNicLista()
        return self.__hostNic[0].getMac()

    "@param tamanho: frame size"
    "@param destino: destination MAC"
    "@param pacote: packet to be send"
    def constroiQuadro(self, tamanho, destino, pacote):
        self.__novoQuadro = Quadro(self.getMAC(), tamanho)
        self.__novoQuadro.setDados(pacote)
        self.__novoQuadro.setDestino(destino)
        return self.__novoQuadro

    "@param quadro: frame to be send"
    def enviarQuadro(self, quadro):
        self.__hostNic = self.getNicLista()
        # Test if it's on
        if self.__hostNic[0].getLigado() == True:
            if self.__hostNic[0].getTDados() == True:
                # Send frame to your NIC
                self.__hostNic[0].recebeQuadro(quadro)
                # NIC Send frame to EnlacePP
                if self.__hostNic[0].enviaQuadroEnlace() == True:
                    return True
        return False

    "@param quadro: received frame"
    "@param nic: self nic - unused"
    def receberQuadro(self, quadro, nic):
        pacote = quadro.getDados()
        pacPing = pacote.getDados()

        # Frame ARP-Solicita (ARP-Request)
        if pacote.getIPDestino() == self.__ip and quadro.getDestino() == "FFFFFFFFFFFF":
            self.enviarQuadro(self.__ARP.arpResponde(pacote.getIPOrigem(), quadro.getOrigem()))

        # Frame ARP-Responde (ARP-Answer)
        elif pacote.getIPDestino() == self.__ip and pacote.getDados() == "ARP-Responde":
            # Recupero meu quadro e envio para o destino com o MAC correto
            self.enviarQuadro(self.__ARP.recuperaQuadro(pacote.getIPOrigem(), quadro.getOrigem()))   

        # Frame ICMP-Solicita (ICMP-Request)
        elif pacote.getIPDestino() == self.__ip and quadro.getTipo() == 2 and pacPing.getCodigo() == 0:
            self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), quadro.getOrigem(), pacPing.getTtl()))
            # Send - PacotePing("reply",8)

        # Frame ICMP-Responde (ICMP-Answer) - PacotePing("request",0)
        elif pacote.getIPDestino() == self.__ip and quadro.getTipo() == 2 and pacPing.getCodigo() == 8:
            self.__ICMP.respostaPing(pacote.getIPOrigem(), pacPing.getTtl())
            # Send - PacotePing("request",0)

        # Data frame                              
        elif pacote.getIPDestino() == self.__ip:
            self.__hostListaQuadros.append(quadro)

        # If IP and MAC origin do not empty &&  they are different to Host 
        # Find out the IP and MAC origin and store in listaARP                         
        if pacote.getIPOrigem() != "" and pacote.getIPOrigem() != self.__ip and quadro.getOrigem() != "":
                self.setTabelaARP(pacote.getIPOrigem(), quadro.getOrigem())
        #print "\n"

    "@param ip: new ip"
    "@param mac: new mac"
    def setTabelaARP(self, ip, mac):
        try:
            i = self.__listaARP.index(self.getTabelaARP(ip))
            self.__listaARP.pop(i)
            self.__listaARP.insert(i, TabelaARP(ip, mac))
        except:
            self.__listaARP.append(TabelaARP(ip, mac))
                                    
    "@param ip: ip-key to search"
    def getTabelaARP(self, ip):
        for arp in self.__listaARP:
            if arp.getIP() == ip:
                return arp
        return None
    
    "@param ip: ip-key to remove"
    def removeTabelaARP(self, ip):
        for arp in self.__listaARP:
            if arp.getIP() == ip:
                try:
                    self.__listaARP.remove(arp)
                    return True
                except (ValueError):
                    return False
        return False
    
    "@param tamanho: packet size"
    "@param ip: destination IP"
    "@param dados: data packet"
    def constroiPacote(self, tamanho, ip, dados):
        self.__novoPacote = Pacote(self.__ip, tamanho)
        self.__novoPacote.setIPDestino(ip)
        self.__novoPacote.setDados(dados)
        return self.__novoPacote

    "@param tamanho: packet size"
    "@param ip: destination IP"
    "@param dados: data packet"
    def enviarPacote(self, tamanho, ip, dados):
        # Search by IP the destination MAC in the table
        arpDestino = self.getTabelaARP(ip)
        
        # Make Packet
        pacote = self.constroiPacote(tamanho, ip, dados)
                                
        # If knows origin MAC
        if arpDestino != None:
            return self.enviarQuadro(self.constroiQuadro(tamanho, arpDestino.getMAC(), pacote))
        # Else is not in the list send ARP-Solicita (ARP-request)
        else:
            # Call ARP-Solicita (ARP-Request)
            # Make frame and send it
            return self.enviarQuadro(self.__ARP.arpSolicita(self.constroiQuadro(tamanho, "", pacote)))

    "@param ip: destination ping IP"
    def ping(self, ip):
        if self.__ip == "":
            return False
                 
        self.__ICMP.iniciaPing(ip)
        return self.__ICMP.getPingResult()
    
    # return Ping final statistics
    def statisticsPing(self):
        return self.__ICMP.estatisticas()
    
    # reset Ping statistics
    def resetPing(self):
        self.__ICMP.resetStatistics()
        
