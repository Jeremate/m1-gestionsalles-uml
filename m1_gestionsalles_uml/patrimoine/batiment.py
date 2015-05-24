class Batiment(object):
	"""Classe représentant un batiment.

	Attributs:
		nom : Le nom du batiment
		adresse : L'objet contenant l'adresse du batiment
	"""
	def __init__(self,nom,adresse):
		self.nom = nom
		self.adresse = adresse

	def __str__(self):
		return "{nom} {adresse}".format()

	def __repr__(self):
		return self._nom+" "+repr(self.adresse)

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val