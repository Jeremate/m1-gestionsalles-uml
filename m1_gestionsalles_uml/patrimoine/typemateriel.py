from finance.tabletarif import TableTarif

class Typemateriel(TableTarif):
	"""Classe représentant un type de materiel.

	Attributs:
		nom : nom du type de matériel
	"""

	def __init__(self, nom , code, libelle, montant):
		self.code = code
		self.libelle = libelle
		self.montant = montant
	
	def __str__(self):
		return "{nom}".format()

	def __repr__(self):
		return "{nom}".format()


	def recuperer_code(self):
		return self._code

	def indiquer_code(self, val):
		self._code = val

	code = property(recuperer_code,indiquer_code)

	def recuperer_libelle(self):
		return self._libelle

	def indiquer_libelle(self, val):
		self._libelle = val

	libelle = property(recuperer_libelle,indiquer_libelle)

	def recuperer_montant(self):
		return self._montant

	def indiquer_montant(self, val):
		self._montant = val

	montant = property(recuperer_montant,indiquer_montant)