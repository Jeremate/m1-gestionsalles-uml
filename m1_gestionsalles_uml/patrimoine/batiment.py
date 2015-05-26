class Batiment(object):
	"""Classe représentant un batiment.

	Attributs:
		no_bat : Le numéro du batiement
		nom : Le nom du batiment
		adresse : L'objet contenant l'adresse du batiment
	"""
	def __init__(self,no_bat,nom,adresse):
		self.no_bat = no_bat
		self.nom = nom
		self.adresse = adresse

	def __str__(self):
		return "{} {} {}".format(self.no_bat, self.nom, self.adresse)

	def __repr__(self):
		return "{} {} {}".format(self.no_bat, self.nom, self.adresse)

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val

	@property
	def no_bat(self):
	    return self._no_bat

	@no_bat.setter
	def no_bat(self, val):
		self._no_bat = val