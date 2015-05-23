class Batiment(object):
	"""Classe représentant un batiment.

	Attributs:
		nom : Le nom du batiment
		adresse : L'objet contenant l'adresse du batiment
	"""
	def __init__(self,nom,adresse):
		self.nom = nom
		self.adresse = adresse

	def __repr__(self):
		return "{nom} {adresse}".format()

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val