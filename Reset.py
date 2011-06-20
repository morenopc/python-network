class Reset():
    def doReset(self, ob):
        
        # HOSTs reset IPs#
        for n in range(0,12):
            ob.host[n].setIP('ip-not-found')
            ob.host[n].setMascara('255.255.0.0')
            ob.host[n].setLigado(False)
            ob.nic_host[n].setLigado(False)
            ob.nic_host[n].setTDados(False)
            ob.host[n].resetPing()

        # SWITCHs reset#        
        ob.switch[0].setLigado(False)
        for n in range(0,5):
            ob.nic_switch[n].setLigado(False)
            ob.nic_switch[n].setTDados(False)

        ob.switch[1].setLigado(False)
        for n in range(5,10):
            ob.nic_switch[n].setLigado(False)
            ob.nic_switch[n].setTDados(False)
        
        ob.switch[2].setLigado(False)
        for n in range(10,15):
            ob.nic_switch[n].setLigado(False)
            ob.nic_switch[n].setTDados(False)

        # ROUTERs #
        ob.router[0].setLigado(False)
        for n in range(0,4):
            ob.nic_router[n].setLigado(False)
            ob.nic_router[n].setTDados(False)

        ob.router[1].setLigado(False)
        for n in range(4,8):
            ob.nic_router[n].setLigado(False)
            ob.nic_router[n].setTDados(False)
        
        ob.router[2].setLigado(False)
        for n in range(8,12):
            ob.nic_router[n].setLigado(False)
            ob.nic_router[n].setTDados(False)
