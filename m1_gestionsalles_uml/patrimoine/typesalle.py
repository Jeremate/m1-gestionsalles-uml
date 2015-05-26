class Typesalle(object):
	"""Classe représentant un type de salle.

	Attributs:
		description : description du type de salle
	"""

	def __init__(self,description):
		self.description = description

	def __str__(self):
		return "{}".format(self.description)
	
	def __repr__(self):
		return "{}".format(self.description)

	@property
	def description(self):
	    return self._description

	@description.setter
	def description(self, val):
		self._description = val