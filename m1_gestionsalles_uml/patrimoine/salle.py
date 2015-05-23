class Salle(object):
	def __init__(self,no_etage,no_salle,no_bat,superficie,typesalle):
		self.no_etage = no_etage
		self.no_salle = no_salle
		self.no_bat = no_bat
		self.superficie = superficie
		self.typesalle = typesalle

	def getno_etage():
		return self.no_etage

	def getno_salle():
		return self.no_salle

	def getno_bat():
		return self.no_bat

	def __str__(self):
		return self.no_etage+" "+self.no_salle+" "+self.no_bat+" "+self.superficie+" "+self.typesalle
		
	def __repr__(self):
		return str(self.no_etage)+" "+str(self.no_salle)+" "+str(self.no_bat)+" "+str(self.superficie)+" "+str(self.typesalle)