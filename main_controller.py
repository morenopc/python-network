import cgi
import os
import datetime
import time
import re

# Import webapp
from google.appengine.ext import webapp
# Import handler
from google.appengine.ext.webapp.util import run_wsgi_app
# import webapp template
from google.appengine.ext.webapp import template
# import django context and template render
from django.template import Context, Template

# import load game objects class
from StartMaker import StartMaker
from Reset import Reset

# Global Value to store all game classes objects
# Ugly I know
OB = StartMaker()
reset=Reset()
global ping_flag
ping_flag = [0,0]

class MainPage(webapp.RequestHandler):
    def get(self):
        # Load index.html page
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class TurnOn(webapp.RequestHandler):
    
    def post(self):
        # synchronizing canvas button
        power = self.request.get('power')
        cable = self.request.get('cable')
        power_ctrl = self.request.get('pctrl')
        cable_ctrl = self.request.get('cctrl')
        i=0
        
        if power_ctrl == '1':
            if power[0] == 'S':
                # Switchs power
                for n in range(0,3):
                    if power == 'S'+str(n):
                        i=n*5
                        if OB.switch[n].getLigado() == False:
                            # Turn on Switch
                            OB.switch[n].setLigado(True)
                            # Turn on NIC 01 of Switch
                            OB.nic_switch[0+i].setLigado(True)
                            # Turn on NIC 02 of Switch
                            OB.nic_switch[1+i].setLigado(True)
                            # Turn on NIC 03 of Switch
                            OB.nic_switch[2+i].setLigado(True)
                            # Turn on NIC 04 of Switch
                            OB.nic_switch[3+i].setLigado(True)
                            # Turn on NIC 05 of Switch
                            OB.nic_switch[4+i].setLigado(True)
                            break
                            
            elif power[0] == 'R':
                # Routers power
                for n in range(0,3):
                    if power == 'R'+str(n):
                        i=n*4
                        if OB.router[n].getLigado() == False:
                            # Turn on Router
                            OB.router[n].setLigado(True)
                            # Turn on NIC 01 of Router
                            OB.nic_router[0+i].setLigado(True)
                            # Turn on NIC 02 of Router
                            OB.nic_router[1+i].setLigado(True)
                            # Turn on NIC 03 of Router
                            OB.nic_router[2+i].setLigado(True)
                            # Turn on NIC 04 of Router
                            OB.nic_router[3+i].setLigado(True)
                            break
                            
            elif power[0] == 'H':
                # Hosts power
                for n in range(0,12):
                    if power == 'H'+str(n):
                        if OB.nic_host[n].getLigado() == False:
                            # Turn on Host
                            OB.host[n].setLigado(True)
                            # Turn on NIC
                            OB.nic_host[n].setLigado(True)
                            break
                            
        elif power_ctrl == '0':
            if power[0] == 'H':
                # Hosts power off
                for n in range(0,12):
                    if power == 'H'+str(n):
                        if OB.nic_host[n].getLigado() == True:
                            # Turn off Host
                            OB.host[n].setLigado(False)
                            # Turn off NIC
                            OB.nic_host[n].setLigado(False)
                            break
                            
                            
            elif power[0] == 'S':
                # Switchs power off
                for n in range(0,3):
                    if power == 'S'+str(n):
                        i=n*5
                        if OB.switch[n].getLigado() == True:
                            # Turn off Switch
                            OB.switch[n].setLigado(False)
                            # Turn off NIC 01 of Switch
                            OB.nic_switch[0+i].setLigado(False)
                            # Turn off NIC 02 of Switch
                            OB.nic_switch[1+i].setLigado(False)
                            # Turn off NIC 03 of Switch
                            OB.nic_switch[2+i].setLigado(False)
                            # Turn off NIC 04 of Switch
                            OB.nic_switch[3+i].setLigado(False)
                            # Turn off NIC 05 of Switch
                            OB.nic_switch[4+i].setLigado(False)
                            break
                            
            elif power[0] == 'R':
                # Routers power off
                for n in range(0,3):
                    if power == 'R'+str(n):
                        i=n*4
                        if OB.router[n].getLigado() == True:
                            # Turn on Router
                            OB.router[n].setLigado(False)
                            # Turn on NIC 01 of Router
                            OB.nic_router[0+i].setLigado(False)
                            # Turn on NIC 02 of Router
                            OB.nic_router[1+i].setLigado(False)
                            # Turn on NIC 03 of Router
                            OB.nic_router[2+i].setLigado(False)
                            # Turn on NIC 04 of Router
                            OB.nic_router[3+i].setLigado(False)
                            break
        
        if cable_ctrl == '1':
            if cable[0] == 'S':  
                # Switchs cable
                for n in range(0,3):
                    if cable == 'S'+str(n):
                        i=n*5
                        if OB.nic_switch[0+i].getTDados() == False:
                            # Connect NIC 01 of Switch
                            OB.nic_switch[0+i].setTDados(True)
                            # Connect NIC 02 of Switch
                            OB.nic_switch[1+i].setTDados(True)
                            # Connect NIC 03 of Switch
                            OB.nic_switch[2+i].setTDados(True)
                            # Connect NIC 04 of Switch
                            OB.nic_switch[3+i].setTDados(True)
                            # Connect NIC 05 of Switch
                            OB.nic_switch[4+i].setTDados(True)
                            break
                            
            elif cable[0] == 'R':
                # Routers cable
                for n in range(0,3):
                    if cable == 'R'+str(n):
                        i=n*4
                        if OB.nic_router[0+i].getTDados() == False:
                            # Connect NIC 01 of Router
                            OB.nic_router[0+i].setTDados(True)
                            # Connect NIC 02 of Router
                            OB.nic_router[1+i].setTDados(True)
                            # Connect NIC 03 of Router
                            OB.nic_router[2+i].setTDados(True)
                            # Connect NIC 04 of Router
                            OB.nic_router[3+i].setTDados(True)
                            break
                            
            elif cable[0] == 'H':
                # Hosts cable
                for n in range(0,12):
                    if cable == 'H'+str(n):
                        if OB.nic_host[n].getTDados() == False:
                            # Connect Host
                            OB.nic_host[n].setTDados(True)
                            break
            
        elif cable_ctrl == '0':
            if cable[0] == 'H':
                # Hosts cable
                for n in range(0,12):
                    if cable == 'H'+str(n):
                        if OB.nic_host[n].getTDados() == True:
                            # Disconnect Host
                            OB.nic_host[n].setTDados(False)
                            break
                            
            elif cable[0] == 'S':  
                # Switchs off cable
                for n in range(0,3):
                    if cable == 'S'+str(n):
                        i=n*5
                        if OB.nic_switch[0+i].getTDados() == True:
                            # Disconnect NIC 01 of Switch
                            OB.nic_switch[0+i].setTDados(False)
                            # Disconnect NIC 02 of Switch
                            OB.nic_switch[1+i].setTDados(False)
                            # Disconnect NIC 03 of Switch
                            OB.nic_switch[2+i].setTDados(False)
                            # Disconnect NIC 04 of Switch
                            OB.nic_switch[3+i].setTDados(False)
                            # Disconnect NIC 05 of Switch
                            OB.nic_switch[4+i].setTDados(False)
                            break
                            
            elif cable[0] == 'R':
                # Routers off cable
                for n in range(0,3):
                    if cable == 'R'+str(n):
                        i=n*4
                        if OB.nic_router[0+i].getTDados() == True:
                            # Disconnect NIC 01 of Router
                            OB.nic_router[0+i].setTDados(False)
                            # Disconnect NIC 02 of Router
                            OB.nic_router[1+i].setTDados(False)
                            # Disconnect NIC 03 of Router
                            OB.nic_router[2+i].setTDados(False)
                            # Disconnect NIC 04 of Router
                            OB.nic_router[3+i].setTDados(False)
                            break
        
        # Exit 0
        return 0

class Ping(webapp.RequestHandler):
    
    def consIP(self, n, ip, mask):
        # Check same of itself
        if ip == OB.host[n].getIP():
            return True
        # Check netID
        if ip == OB.ip.netID(ip,mask):
            return False            
        # Check gateway
        for i in range(0,3):
            if (OB.router[i].getIP() == ip):
                return False
        # Check duplicate IP
        for i in range(0,12):
            if (OB.host[i].getIP() == ip):
                return False
        return True

    def post(self):
        global ping_flag
        message = ''
        cmd = self.request.get('textarea');
        cmd_split = cmd.split()
        n = int(self.request.get('host'))
        
        exp = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
        
        # Bash commands dictionary
        try:
            # check command $ ping <ip>
            if cmd_split[0] == 'ping' and exp.match(cmd_split[1])!= None and len(cmd_split) == 2:
                try:
                    # first time
                    if ping_flag[0] == 0 and ping_flag[1] == 0:
                        OB.host[n].resetPing()
                        ping_flag=[1,cmd_split[1]]
                    
                    # Second and more times
                    # important test and correction   
                    elif ping_flag[0] == 1 and cmd_split[1] != '0.0.0.0':
                        OB.host[n].resetPing()
                        ping_flag=[1,cmd_split[1]]
                    
                    # check valid host ip
                    if OB.ip.validaIP(OB.host[n].getIP()) == False:
                        bash='\nHost '+str(n+1)+'-IP: "'+OB.host[n].getIP()+'" invalid\nSet a valid Host '+str(n+1)+'-IP'
                        
                    # check valid ip
                    elif OB.ip.validaIP(ping_flag[1]):
                        request = OB.host[n].ping(ping_flag[1])
                        
                        sub_req = request.split(' ')
                        if sub_req[5] != 'icmp_seq=4':
                            bash='\n'+request
                            time.sleep(0.5)
                        else:
                            # Statistics
                            stcs=OB.host[n].statisticsPing()
                            bash='\n'+request
                            bash+='\n'+stcs[0]+'\n'+stcs[1]+'\n'+stcs[2]
                            ping_flag=[0,0]
                            
                    # ping: unknown host
                    else:
                        bash='\nping: unknown host '+cmd_split[1]
                except (IndexError):
                    bash='\nping: unknown host'
                                       
            # clear
            elif cmd_split[0] == 'clear' and len(cmd_split) == 1:
                bash='clear'
            
            # bash --version
            elif cmd_split[0] == 'bash' and  cmd_split[1] == '--version' and len(cmd_split) == 2:
                bash='bash --version'
            
            # ifconfig
            elif cmd_split[0] == 'ifconfig' and len(cmd_split) == 1:
                bash='\neth0      Link encap:Ethernet  HWaddr '+OB.host[n].getMAC()+'\n          inet addr:'+OB.host[n].getIP()+' Bcast:[not avaiable] Mask:'+OB.host[n].getMascara()+'\n\nCable connect: '+str(OB.nic_host[n].getTDados())
                                
            # ifconfig <IP>
            elif cmd_split[0] == 'ifconfig' and exp.match(cmd_split[1])!= None and len(cmd_split) == 2:
                if OB.ip.validaIP(cmd_split[1]) == False:
                    bash='\nIP: "'+cmd_split[1]+'" invalid'
                elif self.consIP(n,cmd_split[1],OB.host[n].getMascara()) == False:
                    bash='\nIP: "'+cmd_split[1]+'" unavailable'
                else:
                    OB.host[n].setIP(cmd_split[1])
                    bash='\neth0      Link encap:Ethernet  HWaddr '+OB.host[n].getMAC()+'\n          inet addr:'+OB.host[n].getIP()+' Bcast:[not avaiable] Mask:'+OB.host[n].getMascara()+'\n\nCable connect: '+str(OB.nic_host[n].getTDados())
                    
            # netmask <mask>
            elif cmd_split[0] == 'netmask' and exp.match(cmd_split[1])!= None and len(cmd_split) == 2:
                if OB.ip.validaMascara(cmd_split[1]) == False:
                    bash='\nNetmask: "'+cmd_split[1]+'" invalid'
                else:
                    OB.host[n].setMascara(cmd_split[1])
                    bash='\neth0      Link encap:Ethernet  HWaddr '+OB.host[n].getMAC()+'\n          inet addr:'+OB.host[n].getIP()+' Bcast:[not avaiable] Mask:'+OB.host[n].getMascara()+'\n\nCable connect: '+str(OB.nic_host[n].getTDados())
            
            # ifconfig <IP> netmask <mask>
            elif cmd_split[0] == 'ifconfig' and exp.match(cmd_split[1])!= None and  cmd_split[2] == 'netmask' and exp.match(cmd_split[3])!= None and len(cmd_split) == 4:
                if OB.ip.validaIP(cmd_split[1]) == False:
                    bash='\nIP: "'+cmd_split[1]+'" invalid'
                elif self.consIP(n,cmd_split[1],OB.host[n].getMascara()) == False:
                    bash='\nIP: "'+cmd_split[1]+'" unavailable'
                elif OB.ip.validaMascara(cmd_split[3]) == False:
                    OB.host[n].setIP(cmd_split[1])
                    bash='\nNetmask: "'+cmd_split[3]+'" invalid\neth0      Link encap:Ethernet  HWaddr '+OB.host[n].getMAC()+'\n          inet addr:'+OB.host[n].getIP()+' Bcast:[not avaiable] Mask:'+OB.host[n].getMascara()+'\n\nCable connect: '+str(OB.nic_host[n].getTDados())
                else:
                    OB.host[n].setIP(cmd_split[1])
                    OB.host[n].setMascara(cmd_split[3])
                    bash='\neth0      Link encap:Ethernet  HWaddr '+OB.host[n].getMAC()+'\n          inet addr:'+OB.host[n].getIP()+' Bcast:[not avaiable] Mask:'+OB.host[n].getMascara()+'\n\nCable connect: '+str(OB.nic_host[n].getTDados())
            
            # route
            elif cmd_split[0] == 'route' and len(cmd_split) == 1:
                if (n < 4):
                    bash='\nKernel IP routing table\nDestination     Gateway         Genmask         Flags Metric Ref    Use Iface\n201.10.0.0      *               '+OB.host[n].getMascara()+'     U     1      0        0 eth0\nlink-local      *               '+OB.host[n].getMascara()+'     U     1000   0        0 eth0\ndefault         '+OB.router[0].getIP()+'      0.0.0.0         UG    0      0        0 eth0'
                elif (n >= 4 and n < 8):
                    bash='\nKernel IP routing table\nDestination     Gateway         Genmask         Flags Metric Ref    Use Iface\n200.171.0.0      *               '+OB.host[n].getMascara()+'     U     1      0        0 eth0\nlink-local       *               '+OB.host[n].getMascara()+'     U     1000   0        0 eth0\ndefault         '+OB.router[1].getIP()+'      0.0.0.0         UG    0      0        0 eth0'
                elif (n >= 8):
                    bash='\nKernel IP routing table\nDestination     Gateway         Genmask         Flags Metric Ref    Use Iface\n192.168.0.0      *               '+OB.host[n].getMascara()+'     U     1      0        0 eth0\nlink-local       *               '+OB.host[n].getMascara()+'     U     1000   0        0 eth0\ndefault         '+OB.router[2].getIP()+'      0.0.0.0         UG    0      0        0 eth0'
                else:
                     bash='\nRoute-not-found'
                                         
            # help
            elif cmd_split[0] == 'help' and len(cmd_split) == 1:
                bash='help'
            
            # date
            elif cmd_split[0] == 'date' and len(cmd_split) == 1:
                bash='\n'+str(datetime.date.today())
            
            # bash easteregg
            elif cmd_split[0] == 'bash' and  cmd_split[1] == 'easteregg' and  cmd_split[2] == 'momo' and len(cmd_split) == 3:
                bash='\n^>.>^ ^<.<^ ^>_>^ ^<_<^\nMoreno Cunha Tokyo-2010'
            
            # exit
            elif cmd_split[0] == 'exit' and len(cmd_split) == 1:
                bash='exit'
                
            # command-not-found
            else:
                bash='\n"'+cmd+'" command-not-found\nType help to command list'
                
        except (IndexError):
            bash=''
        
        # send n, bash, terminal_title
        message=str(n)+'|:|'+str(bash)+'|:|'+OB.host[n].getIP()
        self.response.out.write(message)

class Reset(webapp.RequestHandler):
    def post(self):
        reset.doReset(OB)
        self.redirect('/')
        
class HowTo(webapp.RequestHandler):
    def post(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'howto.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/on', TurnOn),
                                      ('/reset', Reset),
                                      ('/howto', HowTo),
                                      ('/ping', Ping)],
                                     debug=False)
                                     
def main():    
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
