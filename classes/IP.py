class IP():

    def __init__(self):
        self.__IP = ""

    "@param ip: IP do Host"
    def validaIP(self, ip):
        if type(ip)==type(1):
            return False
        ipPartes = ip.split('.')
        cont = 0
        if  len(ipPartes) != 4:
                return False
        for ips in ipPartes:
            cont = cont + 1
            if  len(ips) > 3:
                return False
            try:
                if int(ips) > 255:
                    return False
                if int(ips) < 0:
                    return False
            except (ValueError):
                return False
            if cont > 4:
                return False
        return True
    
    "@param mrede: Mascara de sub-rede"
    def validaMascara(self, mascara):
        if type(mascara)==type(1):
            return False
        mascPartes = mascara.split('.')
        cont = 0
        mascValidos = ['255', '0', '128', '192', '224', '248', '252', '254']
        valido = False

        # Testa se foram digitados todos os quatro octetos
        for masc in mascPartes:
            cont = cont + 1
            if masc == '':
                return False
        if cont != 4:
            return False
        else:
            cont = 0
        
        # Testa se o primeiro campo e' igual a 255
        if mascPartes[0] != "255":
                return False      

        # Testa a mascara valida 255.0.0.0
        if mascPartes[1] == "0":
            if mascPartes[2] == "0":
                if mascPartes[3] != "0":
                    return False
            
        for mascs in mascPartes:
            valida = False
            if  len(mascs) > 3:
                return False
            try:
                if int(mascs) > 255:
                    return False
                elif int(mascs) < 0:
                    return False

                # Testa de os valores das mascaras sao validos
                for mval in  mascValidos:
                    if mascs == mval:
                        valida = True
                        break
                    valida = False
                if valida == False:
                    return False
            except (ValueError):
                return False
        return True
    
    "@param ip: IP do Host"
    "@param mascara: Mascara de rede"
    def netID(self, ip, mascara):
        if self.validaIP(ip) == False:
            return "0.0.0.0"
        elif self.validaMascara(mascara) == False:
            return "0.0.0.0"
        
        ipPartes = ip.split('.')
        mascaraPartes = mascara.split('.')
        bin_NetID = 0
        NetID = []

        for ips, masc in zip(ipPartes, mascaraPartes):
            bin_NetID = int(int(ips)&int(masc))
            NetID.append(str(bin_NetID))
            NetID.append('.')

        NetID.pop(len(NetID)-1)# Retira o ultimo ponto da string bin_NetID
        NetID = ''.join(NetID)
        return NetID

    "@param ip: IP do Host"
    "@param mascara: Mascara de sub-rede"
    def hostID(self, ip, mascara):
        
        if self.validaIP(ip) == False:
            return "0.0.0.0"
        elif self.validaMascara(mascara) == False:
            return "0.0.0.0"
        
        ipPartes = ip.split('.')
        mascaraPartes = mascara.split('.')
        bin_HostID = 0
        HostID = []

        for ips, masc in zip(ipPartes, mascaraPartes):
            # Mascara XOR 255
            bin_HostID = int(int(masc)^255)

            # Resulta AND IP
            bin_HostID = bin_HostID&int(ips)

            HostID.append(str(bin_HostID))
            HostID.append('.')
                        
        HostID.pop(len(HostID)-1)# Retira o ultimo ponto da string bin_NetID
        HostID = ''.join(HostID)
        return HostID

        "@param objetoIP: Objeto do tipo IP"
        def testaIP(self, objetoIP):
            try:
                if objetoIP == self:
                    return True
                else:
                    return False
            except AttributeError:
                return False
