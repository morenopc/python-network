from EquipamentoRede import EquipamentoRede
from TabelaRotas import TabelaRotas
from Rota import Rota
from IP import IP
from ICMP import ICMP
from Quadro import Quadro

class Router(EquipamentoRede):

    def __init__(self):
        self.__nome = ""
        EquipamentoRede.__init__(self)
        self.__tRotas = TabelaRotas()
        self.__IP = IP()
        self.__ICMP = ICMP(self)
        self.__ip = ""
        self.__mac = ""
        self.__novoQuadro = None
        self.__quadro = None

    def getIP(self):
        return self.__ip
    
    "@param ip: Router if address"
    def setIP(self, ip):
        self.__ip = ip

    def getMAC(self):
        return self.__mac
    
    "@param mac: Router mac address"
    def setMAC(self, mac):
        self.__mac = mac
    
    # Receive frame from NIC
    "@param quadro: frame received"
    "@param nic: Router NIC"
    def receberQuadro(self, quadro, nic):
        
        self.__quadro = quadro
        pacote = self.__quadro.getDados()
        pacPing = pacote.getDados() 
        ip_pacote = pacote.getIPDestino()
        ttl = pacPing.getTtl()
        
        # Get route list
        lRotas = self.getRota()
        
        # Search for Router NIC source route in the route list
        for rota in lRotas:
            if rota.getIFace() == nic.getMac():
                rota_local = rota
                mascara_local = rota.getMascara()
                ip_local = rota.getRoute()
                
        # Get the netip using destination frame ip
        netid_pacote = self.__IP.netID(ip_pacote, mascara_local)

        # Check if it's not in the local network and if it didn't come from itself
        # If didn't, it tries to find the destination route
        if netid_pacote != rota_local.getDestino() and self.__quadro.getOrigem() != nic.getMac():
            
            # set router NIC source MAC
            self.setMAC(nic.getMac())
            
            # Decrease TTL
            ttl = ttl - 1
            pacPing.setTtl(ttl)
            
            # Search destination route
            rota_destino = self.__tRotas.encontrarRota(ip_pacote)
            
            # Frame ICMP-Solicita (ICMP-Request)
            if pacote.getIPDestino() == self.__ip and self.__quadro.getTipo() == 2 and pacPing.getCodigo() == 0:
                rota_reply = Rota(self.__IP.netID(self.getIP(), "255.255.255.0"),self.getIP(),"255.255.255.0", "0", nic.getMac())
                self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), self.__quadro.getOrigem(), pacPing.getTtl()),rota_reply)
                # Send - PacotePing("reply",8)
            
            # Frame ICMP-Responde (ICMP-Answer)
            elif pacote.getIPDestino() == self.__ip and quadro.getTipo() == 2 and pacPing.getCodigo() == 8:
                rota_reply = Rota(self.__IP.netID(self.getIP(), "255.255.255.0"),self.getIP(),"255.255.255.0", "0", nic.getMac())
                self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), self.__quadro.getOrigem(), pacPing.getTtl()),rota_reply)
                # Send - PacotePing("reply",8)
                
            # If destination was found
            elif rota_destino != None:
                # forwards
                self.enviarQuadro(self.__quadro, rota_destino)
            
            # Destination Host Unreachable
            elif ttl == 0:
                # Send ICMP-Responde (ICMP-Answer)
                rota_reply = Rota("127.0.0.0","127.0.0.1","255.255.255.0", "0", nic.getMac())
                self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), self.__quadro.getOrigem(), ttl), rota_reply)
            
            # Simulating Internet
            else:
                if self.__tRotas.getRotaDefault().getIFace() == "INTERNET":
                    rota_reply = Rota("127.0.0.0","127.0.0.1","255.255.255.0", "0", nic.getMac())
                    self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), self.__quadro.getOrigem(), 0), rota_reply)
               
                else:
                    # Sending to default (next Router)
                    self.enviarQuadro(self.__quadro, self.__tRotas.getRotaDefault())
        
        # Frame ICMP-Solicita (ICMP-Request)
        elif pacote.getIPDestino() == self.__ip and self.__quadro.getTipo() == 2 and pacPing.getCodigo() == 0:
            rota_reply = Rota(self.__IP.netID(self.getIP(), "255.255.255.0"),self.getIP(),"255.255.255.0", "0", nic.getMac())
            self.enviarQuadro(self.__ICMP.respondeICMP(pacote.getIPOrigem(), self.__quadro.getOrigem(), pacPing.getTtl()),rota_reply)
            # Send - PacotePing("reply",8)
    
    "@param quadro: received frame"
    "@param rota: destination route"
    def enviarQuadro(self, quadro, rota):
            
            # Rebuiding the frame to forwards
            quadroRouter = self.constroiQuadro(quadro.getTamanho(), quadro.getDestino(), quadro.getDados())
            quadroRouter.setTipo(quadro.getTipo())
            
            # Find Router NIC to forwards the frame
            nicLista = self.getNicLista()
            nic_origem = None
            for nic in nicLista:
                if nic.getMac() == rota.getIFace():
                    nic_origem = nic
            
            # Change frame source MAC to Router nic MAC 
            if nic_origem != None:
                quadroRouter.setOrigem(nic_origem.getMac())                        
                nic_origem.recebeQuadro(quadroRouter)
                if nic_origem.enviaQuadroEnlace() == True:
                    return True
                else:
                    return False
                    
    "@param tamanho: frame size"
    "@param destino: destination MAC"
    "@param pacote: Packet to be send"
    def constroiQuadro(self, tamanho, destino, pacote):
        self.__novoQuadro = Quadro(self.getMAC(), tamanho)
        self.__novoQuadro.setDados(pacote)
        self.__novoQuadro.setDestino(destino)
        return self.__novoQuadro
    
    "@param rota_def: router default route"
    def setRotaDefault(self, rota_def):
        self.__tRotas.setRotaDefault(rota_def)

    def getRotaDefault(self):
        return self.__tRotas.getRotaDefault()

    "@param rota: new route"
    def setRota(self, rota):
        self.__tRotas.addRota(rota)

    def getRota(self):
        return self.__tRotas.getLRotas()

    "@param nome: Router's name"
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
