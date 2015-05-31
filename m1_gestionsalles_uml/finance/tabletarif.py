import abc

class TableTarif(object):
	"""Classe abstraite

	Attributs:
		code : code du montant
		libelle : libelle du montant
		montant : montant

	"""
	__metaclass__ = abc.ABCMeta


	@abc.abstractmethod
	def initialisation(self, code, libelle, montant):
		self.code = code
		self.libelle = libelle
		self.montant = montant

	def __repr__(self):
		return "{} {} {}".format(self.code, self.libelle, self.montant)
	
	def __str__(self):
		return "{} {} {}".format(self.code, self.libelle, self.montant)

	def recuperer_code(self):
		return self._code

	def indiquer_code(self, val):
		self._code = val 

	code = abc.abstractproperty(recuperer_code,indiquer_code)

	def recuperer_libelle(self):
		return self._libelle

	def indiquer_libelle(self, val):
		self._libelle = val

	libelle = abc.abstractproperty(recuperer_libelle,indiquer_libelle)

	def recuperer_montant(self):
		return self._montant

	def indiquer_montant(self, val):
		self._montant = val

	montant = abc.abstractproperty(recuperer_montant, indiquer_montant)