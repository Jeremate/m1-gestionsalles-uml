class Demandeur(object):
	"""Classe représentant un demandeur.

	Attributs:
		no_dem : numéro unique du demandeur
		nom : nom du demandeur
		adresse : adresse du demandeur
		reservations : liste des réservations pour le demandeur
	"""
	def __init__(self,no_dem,nom,adresse):
		self.no_dem = no_dem
		self.nom = nom
		self.adresse = adresse

	def __str__(self):
		return eelf._no_dem+" "+self._nom+" "+repr(self.adresse)

	def __repr__(self):
		return self._nom+" "+repr(self.adresse)

	@property
	def no_dem(self):
	    return self._no_dem

	@no_dem.setter
	def no_dem(self, val):
		self._no_dem = val

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val
