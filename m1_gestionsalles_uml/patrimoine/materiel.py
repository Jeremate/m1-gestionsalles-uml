class Materiel(object):
	"""Classe représentant un Materiel.

	Attributs:
		code_inv : Le code inventaire du materiel
		typemateriel : L'identifiant du type du matériel
	"""

	def __init__(self, code_inv, id_typemateriel):
		super(Materiel, self).__init__()
		self.code_inv = code_inv
		self.typemateriel = id_typemateriel

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

	@property
	def typemateriel(self):
	    return self._typemateriel

	@code_inv.setter
	def typemateriel(self, val):
		self._typemateriel = val