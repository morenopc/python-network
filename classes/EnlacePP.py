class EnlacePP:
#Classe de ligacao entre NICs
	
	def __init__(self):
		self.__nic_1 = None
		self.__nic_2 = None
		#self.__quadro = None Debug

	"@param NIC: NIC de umas das pontas do enlace"
	def setEnlacePP(self, NIC):
        # Armazena os NICs nas variaveis
		if self.__nic_1 == None:
			self.__nic_1 = NIC
		elif self.__nic_2 == None:
			self.__nic_2 = NIC
	
	"@param NIC: NIC de umas das pontas do enlace"
	def getEnlacePP(self, NIC):
        # Testa se NIC A esta ligado ao outro NIC B
		try:
			if self.__nic_1 == NIC:
				if self.__nic_2.getLigado() == True:
					if self.__nic_2.getTDados() == True:
						return True
			elif self.__nic_2 == NIC:
				if self.__nic_1.getLigado() == True:
					if self.__nic_1.getTDados() == True:
						return True
		except AttributeError:
			return False
		return False
	
	"@param quadro: quandro recebido do eq. de rede"
	"@param nic: NIC de umas das pontas do enlace"
	def encaminhaDados(self, quadro, nic):
        # Encaminha o quadro ao NIC que esta na ponta oposta
	#de Enlace e encaminha para Equipamento de rede
		#self.__quadro = quadro Degub
		if nic == self.__nic_1:
			self.__nic_2.recebeQuadro(quadro)
			self.__nic_2.enviaQuadroEqRede()
		elif nic == self.__nic_2:
			self.__nic_1.recebeQuadro(quadro)
			self.__nic_1.enviaQuadroEqRede()
