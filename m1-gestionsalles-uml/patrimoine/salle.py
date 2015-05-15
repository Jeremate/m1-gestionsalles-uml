class salle:
	def __init__(self,no_etage,no_salle,no_bat,supercifie):
		self.no_etage = no_etage
		self.no_salle = no_salle
		self.no_bat = no_bat
		self.supercifie = supercifie

	def getno_etage():
		return self.no_etage

	def getno_salle():
		return self.no_salle

	def getno_bat():
		return self.no_bat

	def __str__(self):
		return self.nom+" "+self.adresse
		
	def __repr__(self):
		return self.nom+" "+self.adresse