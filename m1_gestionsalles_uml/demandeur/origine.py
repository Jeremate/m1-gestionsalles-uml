class Origine(object):
	"""Classe représentant l'origine d'un demandeur.

	Attributs:
		nom : Le nom de l'origine
	"""

	def __init__(self,nom):
		self.nom = nom


	def __str__(self):
		return self._nom

	def __repr__(self):
		return self._nom

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val