from Quadro import Quadro
from Pacote import Pacote
from Cronometro import Cronometro
from Ping import Ping
from PacotePing import PacotePing
import time

class ICMP():

    "@param host: ICMP Host"    
    def __init__(self, host):
        self.__host = host
        self.__ping = Ping()
        self.__novoQuadro = None
        self.__quadroRecebido = False
        self.__quadroTempoVital = 4 # Time in seconds
        self.__quadroTTL = 64 # ttl linux defaul
        self.__cronometro = Cronometro()
        #self.__timer = [0,0] useless
        self.__enviados = 0
        self.__recebidos = 0

    "@param ipDest: Destination Ping IP"
    def iniciaPing(self,ipDest):
        self.__ping.setipResposta(ipDest)
        self.__ping.setipOrigin(self.__host.getIP())
        self.__quadroRecebido = False
        self.__cronometro.zerar()
        self.__cronometro.iniciar()
        self.__enviados += 1

        # Sending ping frame
        if (self.__host.enviarQuadro(self.enviaICMP(ipDest)) == False):
            if (self.__enviados > 0):
                self.__enviados -= 1
            else:
                self.__enviados = 0
            self.__ping.setTempo(self.__cronometro.parar())
            self.__ping.setMessage('connect: Network is unreachable')
            #return False
                
        # Timeout without answer
        elif (self.__quadroRecebido == False):
            self.__ping.setTempo(self.__cronometro.parar())
            # Artificial delay
            time.sleep(self.__quadroTempoVital)
            self.__ping.setMessage('Timeout without answer')

    "@param ipDest: ICMP frame IP origin to be created"
    def respostaPing(self, ipOrigem, ttl):
        
        # Check delivery time
        delivery_time=self.__cronometro.parar()
        self.__ping.setTempo(delivery_time)
        self.__quadroRecebido = True
        
        # If the frame was delivered in time and ttl more than 0
        if delivery_time < self.__quadroTempoVital and ttl > 0:
            # Add to ping queue
            self.__recebidos += 1
            self.__ping.setTTL(ttl)
            self.__ping.setFilaPing()

        # If the frame was delivered in time and ttl less or igual 0
        elif delivery_time < self.__quadroTempoVital and ttl <= 0:
            # Destination Host Unreachable
            self.__ping.setMessage('Destination Host Unreachable')
        
        # If the frame was delivered with time's up
        elif delivery_time > self.__quadroTempoVital:
            # Received with time's up
            self.__ping.setMessage('Time\'s up!')
            
        else:
            self.__ping.setMessage('Erro check network connection')

    "@param ipDest: Destination ICMP frame IP to be create"
    def enviaICMP(self, ipDest):
        # Make ICMP packet
        pacote_ICMP = Pacote(self.__host.getIP(),self.__ping.getTamanho())
        pacote_ICMP.setIPDestino(ipDest)
        PacPing = PacotePing("request",0)
        # PING frame TTL
        PacPing.setTtl(self.__quadroTTL)
        pacote_ICMP.setDados(PacPing)
        # Make ICMP frame
        Quadro_ICMP = self.__host.constroiQuadro(self.__ping.getTamanho(), "000000000000", pacote_ICMP)
        Quadro_ICMP.setTipo(2)
        # Return ICMP frame ready
        return Quadro_ICMP

    "@param ipDest: Origin frame IP received from Host"
    "@param macDest: Origin frame MAC received from Host"
    def respondeICMP(self, ipDest, macDest, ttl):
        
        # Make ICMP answer packet 
        pacote_ICMP = Pacote(self.__host.getIP(),self.__ping.getTamanho())
        pacote_ICMP.setIPDestino(ipDest)

        # Make ping answer packet 
        PacPing = PacotePing("reply",8)
        PacPing.setTtl(ttl)
        pacote_ICMP.setDados(PacPing)

        # Make ICMP frame 
        Quadro_ICMP = self.__host.constroiQuadro(self.__ping.getTamanho(), "000000000000", pacote_ICMP)
        Quadro_ICMP.setDestino(macDest)
        Quadro_ICMP.setTipo(2)
        # Return ICMP frame set
        return Quadro_ICMP
        
    def resetStatistics(self):
        # Restart queue, list and variables
        self.__ping.setIcmpSeq()
        self.__ping.zerarFilaPing()
        self.__enviados = 0
        self.__recebidos = 0
        
    # Rebuild the ping fuction
    # store all data in pingTabela and use it until new ping request
    def estatisticas(self):
        statisticsTable = []
        pingTabela = self.__ping.getFilaPing()

        # Lost, sent and received
        perdidos = self.__enviados - self.__recebidos
        try:
            porcentagem = 100*perdidos/self.__enviados
        except (ZeroDivisionError):
            porcentagem = 0
            
        statisticsTable.append("--- "+self.__ping.getipResposta()+" ping statistics ---")
        statisticsTable.append((str(self.__enviados))+" packets transmitted, "+(str(self.__recebidos))+" received, "+(str(porcentagem))+"% packet loss")
        maior = pingTabela[0][4]
        menor = pingTabela[0][4]
        for ptime in pingTabela:
            if ptime[4] > maior:
                maior = ptime[4]
            if ptime[4] < menor:
                menor = ptime[4]
        try:
            media = (maior + menor)/2
        except (ZeroDivisionError):
            media = 0
        #except (TypeError):
        
        statisticsTable.append("rtt min/avg/max = "+"%1.*f" % (3, menor)+"/"+"%1.*f" % (3, media)+"/"+"%1.*f" % (3, maior)+" ms")
        self.resetStatistics()
        perdidos = 0
        media = 0
        return statisticsTable
    
    def getPingResult (self):
        pingTabela = self.__ping.getFilaPing()[len(self.__ping.getFilaPing())-1]
        try:
            pingTabela[3].isalpha()
            return (str(pingTabela[0]))+' bytes from '+pingTabela[1]+' ('+pingTabela[1]+'): icmp_seq='+(str(pingTabela[2]))+' '+pingTabela[3]
        except(AttributeError):
            return (str(pingTabela[0]))+' bytes from '+pingTabela[1]+' ('+pingTabela[1]+'): icmp_seq='+(str(pingTabela[2]))+' ttl='+(str(pingTabela[3]))+'  time='+"%1.*f" % (3, pingTabela[4])+' ms'
    
    # Debug
    #def getFilaPing (self):
        #return self.__ping.getFilaPing()
