from EquipamentoRede import EquipamentoRede

class Switch(EquipamentoRede):
	
	def __init__(self):
                self.__nome = ""
		EquipamentoRede.__init__(self)
		self.__filaQuadros = []
		self.__novoQuadro = None
		self.__listaMacsOrigem = [None, None, None, None, None, None]
		self.__nicLista = self.getNicLista()
	
	"@param quadro: frame received"
	"@param nic: self nic"
	def receberQuadro(self, quadro, nic):

		# Learning MACs source
		nicOrigemIndex = self.__nicLista.index(nic)# Descobre o index do NIC que recebeu o quadro na nicLista
		if self.__listaMacsOrigem[nicOrigemIndex] != quadro.getOrigem():# Se o MAC origem for diferente do que estiver guardado
			self.__listaMacsOrigem.pop(nicOrigemIndex)# Retiro da lista
			self.__listaMacsOrigem.insert(nicOrigemIndex, quadro.getOrigem())# Guarda o MAC do NIC no mesmo index
		self.enviarQuadro(quadro)# Envia Quadro
			
	# Envia quadro para NIC destino
	# Caso NIC destino nao seja encontrado, envia a todos os NICs (broadcast)
	def enviarQuadro(self, quadro):
	
                try:
                        # Descobre o index do MAC Destino
                        macDestinoIndex = self.__listaMacsOrigem.index(quadro.getDestino())
                        
                        # Pelo index descobre o NIC do Switch que esta relaciona do ele
                        nicSwitchDestino = self.__nicLista[macDestinoIndex] # Obtem NIC destino
                        
                        nicSwitchDestino.recebeQuadro(quadro)# Envia quandro para NIC_Switch encontrado
                        return nicSwitchDestino.enviaQuadroEnlace()
        
                except (IndexError, ValueError): # Se NIC destino nao encontrado
                        for nics in self.__nicLista: # Envia para todos
                                nics.recebeQuadro(quadro)
                                # Envia quadro para o enlace
                                nics.enviaQuadroEnlace()
                        return "Broadcast"

        def setNome(self, nome):
                self.__nome = nome

        def getNome(self):
                return self.__nome	
			
