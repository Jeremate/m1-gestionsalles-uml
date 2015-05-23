class Materiel(object):
	"""Classe représentant un Materiel.

	Attributs:
		code_inv : Le code inventaire du materiel
	"""

	def __init__(self,code_inv):
		self.code_inv = code_inv

	def __repr__(self):
		return "{code_inv}".format()

	@property
	def code_inv(self):
	    return self._code_inv

	@code_inv.setter
	def code_inv(self, val):
		self._code_inv = val