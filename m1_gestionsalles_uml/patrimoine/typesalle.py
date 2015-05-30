from finance.tabletarif import TableTarif

class Typesalle(TableTarif):
	"""Classe représentant un type de salle.

	Attributs:
		id_titre : identifiant du type de salle
	"""

	def __init__(self, id_titre , code, libelle, montant):
		super(Typesalle, self).initialisation(code, libelle, montant)
		self.id_titre = id_titre


	def __str__(self):
		return "{}".format(self.id_titre)

	def __repr__(self):
		return self._id_titre

	@property
	def id_titre(self):
	    return self._id_titre

	@id_titre.setter
	def id_titre(self, val):
		self._id_titre = val