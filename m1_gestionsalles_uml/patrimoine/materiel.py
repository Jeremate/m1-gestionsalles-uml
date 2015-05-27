from finance.tabletarif import TableTarif

class Materiel(TableTarif):
	"""Classe représentant un Materiel.

	Attributs:
		code_inv : Le code inventaire du materiel
	"""

	def __init__(self,code_inv):
		self._code_inv = code_inv


	def __str__(self):
		return "{}".format(self._code_inv)

	def __repr__(self):
		return "{}".format(self._code_inv)

	@property
	def code_inv(self):
	    return self._code_inv

	@code_inv.setter
	def code_inv(self, val):
		self._code_inv = val