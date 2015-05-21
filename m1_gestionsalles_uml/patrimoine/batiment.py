class Batiment(object):
	def __init__(self,nom,adresse):
		self.nom = nom
		self.adresse = adresse
	def __str__(self):
		return self.nom+" "+self.adresse
	def __repr__(self):
		return self.nom+" "+self.adresse