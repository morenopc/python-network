class Ping():

    def __init__(self):
        self.__ipResp = ""
        self.__ipOrig = ""
        self.__tamanho = 64 # bytes
        self.__tempo = 0
        self.__ttl = 0
        self.__icmp_seq = 0
        self.__filaPing = []

    "@param ipResp: IP of ping destination answer"
    def setipResposta(self, ipResp):
        self.__ipResp = ipResp

    def getipResposta(self):
        return self.__ipResp

    "@param ipOrig: Origin IP of ping"
    def setipOrigin(self, ipOrig):
        self.__ipOrig = ipOrig

    def getipOrigin(self):
        return self.__ipOrig

    "@param tamanho: Frame size"
    def setTamanho(self, tamanho):
        self.__tamanho = tamanho
                    
    def getTamanho(self):
        return self.__tamanho

    "@param tempo: Frame return time"
    def setTempo(self, tempo):
        self.__tempo = tempo

    def getTempo(self):
        return self.__tempo

    "@param ttl: variavel TTL"
    def setTTL(self, ttl):
        self.__ttl = ttl

    def getTTL(self):
        return self.__ttl
    
    def setIcmpSeq(self):
        self.__icmp_seq = 0

    def getIcmpSeq(self):
        self.__icmp_seq += 1
        return self.__icmp_seq

    def setFilaPing(self):
        # line: size, ip, icmp_seq, ttl, time 
        self.__filaPing.append([self.getTamanho(), self.getipOrigin(), self.getIcmpSeq(), self.getTTL(), self.getTempo()*1000])
    
    "@param say: Message to Ping result"    
    def setMessage(self, say):
        self.__filaPing.append([self.getTamanho(), self.getipOrigin(), self.getIcmpSeq(), say, self.getTempo()*1000])
                                   
    def getFilaPing(self):
        return self.__filaPing
    
    def zerarFilaPing(self):
        self.__filaPing = []
