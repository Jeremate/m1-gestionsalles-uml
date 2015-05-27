import abc

class TableTarif(object):
	"""Classe abstraite

	Attributs:
		code : code du tarif
		libelle : libelle du tarif
		montant : montant du tarif

	"""
	__metaclass__ = abc.ABCMeta


	@abc.abstractmethod
	def initialisation(self, code, libelle, tarif):
		self.code = code
		self.libelle = libelle
		self.tarif = tarif

	def __repr__(self):
		return "{} {} {}".format(self.code, self.libelle, self.tarif)
	
	def __str__(self):
		return "{} {} {}".format(self.code, self.libelle, self.tarif)

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

	def recuperer_tarif(self):
		return self._tarif

	def indiquer_tarif(self, val):
		self._tarif = val

	tarif = abc.abstractproperty(recuperer_tarif, indiquer_tarif)