class NIC:
# Classe que representa as placas de rede

	"@param mac: MAC do NIC"
	"@param enlace: Enlace em que o NIC se conecta"
	"@param eqRede: Equipamento de rede base"
	def __init__(self, mac, enlace, eqRede):
		self.__mac = mac
		self.__ligado = False
		self.__tDados = False
		self.__EnlacePP = enlace
		self.__eqRede = eqRede
		self.__quadro = None
		#Diz para enlace que e o seu NIC
		self.__EnlacePP.setEnlacePP(self)
		#Diz para equipamento de rede que e o seu NIC
		self.__eqRede.setNIC(self)
	          
	# Retorna o MAC de Nic
	def getMac(self):
		return self.__mac
	
	# Retorna o estado de Nic
	def getTDados(self):
		return self.__tDados
	
	"@param tdados: confirma se NIC transmite dados"
	def setTDados(self, tdados):
  # Nic transmite dados com o Enlace
		self.__tDados = tdados
	
	# Retorna o estado de Nic
	def getLigado(self):
		return self.__ligado
	
	"@param ligado: confirma se NIC esta ligado"
	def setLigado(self, ligado):
    # Liga Nic
		self.__ligado = ligado
		
	"@param quadro: Quadro recebido do Eq. de Rede"
	def recebeQuadro(self, quadro):
  	# Recebe quadro do Equipamento de rede
		self.__quadro = quadro
	
	# Testa se NIC esta ligado ao outro NIC
	#atraves de enlacePP e encaminha quadro
	def enviaQuadroEnlace(self):		
		if self.__EnlacePP.getEnlacePP(self) == True:
			self.__EnlacePP.encaminhaDados(self.__quadro, self)
			return True
		else:
			return False
	
	# Entrega ao Equipamento de Rede o quadro de dados.
	def enviaQuadroEqRede(self):
		self.__eqRede.receberQuadro(self.__quadro, self)