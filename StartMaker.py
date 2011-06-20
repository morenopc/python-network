from Switch import Switch
from NIC import NIC
from Host import Host
from EnlacePP import EnlacePP
from Router import Router
from Rota import Rota
from IP import IP

class StartMaker():

    ip = IP()
    host = []
    enlacePP = []
    enlacePP = []
    switch = []
    router = []
    nic_host = []
    nic_switch = []
    nic_router = []
    
    # All Class Objects store in arrays[n] started 0 to n-1 
    
    # Start Hosts 0~11
    for n in range(0,12):
        host.append(Host())
    
    # Start Enlace 0~21
    for n in range(0,22):
        enlacePP.append(EnlacePP())
    
    # Start Switchs 0~2
    for n in range(0,3):
        switch.append(Switch())

    switch[0].setNome('switch_0')
    switch[1].setNome('Switch_1')
    switch[2].setNome('Switch_2')
    
    # Start Routers 0~2
    for n in range(0,3):
        router.append(Router())

    router[0].setNome('Router_0')
    router[1].setNome('Router_1')
    router[2].setNome('Router_2')

    # Start Hosts-NICs ( 12th )
    # NIC receved MAC, Enlace and Host
    # Network 201.10.0.0
    nic_host.append(NIC('01:0A:00:FF:0A:01',enlacePP[0],host[0]))
    nic_host.append(NIC('02:0A:00:FF:0A:02',enlacePP[1],host[1]))
    nic_host.append(NIC('03:0A:00:FF:0A:03',enlacePP[2],host[2]))
    nic_host.append(NIC('04:0A:00:FF:0A:04',enlacePP[3],host[3]))
    # Network 200.171.0.0
    nic_host.append(NIC('05:0B:00:EE:0B:05',enlacePP[5],host[4]))
    nic_host.append(NIC('06:0B:00:EE:0B:06',enlacePP[6],host[5]))
    nic_host.append(NIC('07:0B:00:EE:0B:07',enlacePP[7],host[6]))
    nic_host.append(NIC('08:0B:00:EE:0B:08',enlacePP[8],host[7]))
    # Network 192.168.0.0
    nic_host.append(NIC('09:0C:00:CC:0C:09',enlacePP[10],host[8]))
    nic_host.append(NIC('0A:0C:00:CC:0C:0A',enlacePP[11],host[9]))
    nic_host.append(NIC('0B:0C:00:CC:0C:0B',enlacePP[12],host[10]))
    nic_host.append(NIC('0C:0C:00:CC:0C:0C',enlacePP[13],host[11]))

    # Start Switchs-NICs ( 15th )
    # Nic receved MAC, Enlace and Switch
    # Switch 0
    nic_switch.append(NIC('040A7119SW01',enlacePP[0],switch[0]))
    nic_switch.append(NIC('040A7119SW02',enlacePP[1],switch[0]))
    nic_switch.append(NIC('040A7119SW03',enlacePP[2],switch[0]))
    nic_switch.append(NIC('040A7119SW04',enlacePP[3],switch[0]))
    # Dedicated Router 0 - Network 201.10.0.0
    nic_switch.append(NIC('040A7119SW05',enlacePP[4],switch[0]))# Local Network 201.10.0.0

    # Switch 1
    nic_switch.append(NIC('040A7119SW06',enlacePP[5],switch[1]))
    nic_switch.append(NIC('040A7119SW07',enlacePP[6],switch[1]))
    nic_switch.append(NIC('040A7119SW08',enlacePP[7],switch[1]))
    nic_switch.append(NIC('040A7119SW09',enlacePP[8],switch[1]))
    # Dedicated Router 1 - Network 200.171.0.0
    nic_switch.append(NIC('0040A7119SW10',enlacePP[9],switch[1]))# Local Network 200.171.0.0

    # Switch 2
    nic_switch.append(NIC('040A7119SW11',enlacePP[10],switch[2]))
    nic_switch.append(NIC('040A7119SW12',enlacePP[11],switch[2]))
    nic_switch.append(NIC('040A7119SW13',enlacePP[12],switch[2]))
    nic_switch.append(NIC('040A7119SW14',enlacePP[13],switch[2]))
    # Dedicated Router 2 - 192.168.0.0
    nic_switch.append(NIC('040A7119SW15',enlacePP[14],switch[2]))# Local Network 192.168.0.0

    # Start Routers-NICs ( 12th )
    # Router 0 Networks 10.0.0.0 and 201.10.0.0 
    nic_router.append(NIC('040A7119SR01',enlacePP[4],router[0])) # Network 201.10.0.0 - Local
    nic_router.append(NIC('040A7119SR02',enlacePP[15],router[0])) # Network 10.0.0.0
    nic_router.append(NIC('040A7119SR03',enlacePP[16],router[0])) # unused
    nic_router.append(NIC('040A7119SR04',enlacePP[17],router[0])) # unused

    # Router 1 Networks 10.0.0.0, 11.0.0.0 and 200.171.0.0
    nic_router.append(NIC('040A7119SR05',enlacePP[15],router[1])) # Network 10.0.0.0 - 201.10.0.0
    nic_router.append(NIC('040A7119SR06',enlacePP[18],router[1])) # Network 11.0.0.0 - 192.168.0.0
    nic_router.append(NIC('040A7119SR07',enlacePP[9],router[1])) # Network 200.171.0.0 - Local
    nic_router.append(NIC('040A7119SR08',enlacePP[19],router[1]))  # Internet

    # Router 2 Networks 11.0.0.0 and 192.168.0.0
    nic_router.append(NIC('040A7119SR09',enlacePP[18],router[2])) # Network 11.0.0.0
    nic_router.append(NIC('040A7119SR10',enlacePP[14],router[2])) # Network 192.168.0.0 - Local
    nic_router.append(NIC('040A7119SR11',enlacePP[20],router[2])) # unused
    nic_router.append(NIC('040A7119SR12',enlacePP[21],router[2])) # unused    
    
    # Set Routers IP
    router[0].setIP('201.10.0.1')
    router[1].setIP('200.171.0.1')
    router[2].setIP('192.168.0.1')
    
    # Adding Routes
    #router.setRota(Rota('<destination>','<route>','<mask>', '<metric>', '<MAC>'))
    # Router 0 to Router 1 Network A
    router[0].setRota(Rota('201.10.0.0','201.10.0.1','255.255.0.0', '0', '040A7119SR01')) # Network 201.10.0.0 - Local
    router[0].setRota(Rota('200.171.0.0','200.171.0.1','255.255.0.0', '0', '040A7119SR02'))
    router[0].setRota(Rota('192.168.0.0','192.168.0.1','255.255.0.0', '0', '040A7119SR02'))
    router[0].setRota(Rota('10.0.0.0','10.0.0.1','255.0.0.0', '0', '040A7119SR02'))
    router[0].setRotaDefault(Rota('10.0.0.0','10.0.0.1','255.0.0.0', '0', '040A7119SR02'))

    # Router 1 Network 01, 02 and 04
    router[1].setRota(Rota('200.171.0.0','200.171.0.1','255.255.0.0', '0', '040A7119SR07')) # Network 200.171.0.0 - Local
    router[1].setRota(Rota('201.10.0.0','201.10.0.1','255.255.0.0', '0', '040A7119SR05')) # Network 10.0.0.0 - 201.10.0.0
    router[1].setRota(Rota('10.0.0.0','10.0.0.1','255.0.0.0', '0', '040A7119SR05')) # Network 10.0.0.0 - R05
    router[1].setRota(Rota('192.168.0.0','192.168.0.1','255.255.0.0', '0', '040A7119SR06')) # Network 11.0.0.0 - 192.168.0.0
    router[1].setRota(Rota('11.0.0.0','11.0.0.1','255.0.0.0', '0', '040A7119SR06')) # Network 11.0.0.0 - R06
    router[1].setRotaDefault(Rota('0.0.0.0','0.0.0.0','0.0.0.0', '0', 'INTERNET'))

    # Router 2 Network 02 and 05
    router[2].setRota(Rota('192.168.0.0','192.168.0.1','255.255.0.0', '0', '040A7119SR10')) # Network 192.168.0.0 - Local
    router[2].setRota(Rota('11.0.0.0','11.0.0.1','255.0.0.0', '0', '040A7119SR09'))
    router[2].setRota(Rota('200.171.0.0','200.171.0.1','255.255.0.0', '0', '040A7119SR09'))
    router[2].setRota(Rota('201.10.0.0','201.10.0.1','255.255.0.0', '0', '040A7119SR09'))
    router[2].setRotaDefault(Rota('11.0.0.0','11.0.0.1','255.0.0.0', '0', '040A7119SR09'))

# HOSTs reset IPs#
    for n in range(0,12):
        host[n].setIP('ip-not-found')
        host[n].setMascara('255.255.0.0')
        host[n].setLigado(False)
        nic_host[n].setLigado(False)
        nic_host[n].setTDados(False)
        host[n].resetPing()

    # SWITCHs reset#        
    switch[0].setLigado(False)
    for n in range(0,5):
        nic_switch[n].setLigado(False)
        nic_switch[n].setTDados(False)

    switch[1].setLigado(False)
    for n in range(5,10):
        nic_switch[n].setLigado(False)
        nic_switch[n].setTDados(False)
    
    switch[2].setLigado(False)
    for n in range(10,15):
        nic_switch[n].setLigado(False)
        nic_switch[n].setTDados(False)

    # ROUTERs #
    router[0].setLigado(False)
    for n in range(0,4):
        nic_router[n].setLigado(False)
        nic_router[n].setTDados(False)

    router[1].setLigado(False)
    for n in range(4,8):
        nic_router[n].setLigado(False)
        nic_router[n].setTDados(False)
    
    router[2].setLigado(False)
    for n in range(8,12):
        nic_router[n].setLigado(False)
        nic_router[n].setTDados(False)
