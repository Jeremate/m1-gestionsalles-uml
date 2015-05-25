class Titre(object):
	"""Classe représentant le titre d'un demandeur.

	Attributs:
		desc : La desc du titre
	"""

	def __init__(self,desc):
		self.desc = desc


	def __str__(self):
		return self._desc

	def __repr__(self):
		return self._desc

	@property
	def desc(self):
	    return self._desc

	@desc.setter
	def desc(self, val):
		self._desc = val