class EquipamentoRede:
#"Classe Pai de todos os equipamentos contidos no jogo" 
	__ligado = None
	__Quadro = None
	__NICs = None
	
	def __init__(self):
		self.__ligado = False
		self.__Quadro = None
		self.__NICs = []

	def setLigado(self, ligado):
		self.__ligado = ligado	
	
	def getLigado(self):
		return self.__ligado
	
	#Retorna quadro
	def enviarQuadro(self):
		if self.__ligado == True:
			if self.__Quadro != None:
				return self.__Quadro
			else:
				return None
		
	def receberQuadro(self, Quadro, nic):
		self.__Quadro = Quadro
	
	# Guarda NIC a lista de NICs
	def setNIC(self, nic):
		self.__NICs.append(nic)
	
	# Retorna a lista dos NICs		
	def getNicLista(self):
		return self.__NICs