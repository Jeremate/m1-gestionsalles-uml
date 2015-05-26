class Titre(object):
	"""Classe représentant le titre d'un demandeur.

	Attributs:
		description : La description du titre
	"""

	def __init__(self,description):
		self.description = description


	def __str__(self):
		return "{}".format(self.description)

	def __repr__(self):
		return self._description

	@property
	def description(self):
	    return self._description

	@description.setter
	def description(self, val):
		self._description = val