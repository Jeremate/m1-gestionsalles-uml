class Adresse(object):
	"""Classe représentant une adresse postale en France.

	Attributs:
		no : le numéro de l'adresse
		adresse : le type et le nom de la rue
		code : le code postal
		ville : la ville de cette adresse

	"""

	def __init__(self, no, adresse, code, ville):
		"""Init Adresse, aucun attribut par défaut"""
		self.no = no
		self.adresse = adresse
		self.code = code
		self.ville = ville

	def __repr__(self):
		"""Représentation de la classe Adresse"""
		return "{no} {adresse}, {code} - {ville}".format()

	@property
	def no(self):
	    return self._no
	
	@no.setter
	def no(self, val):
		if val < 1:
			self._no = 1
		else:
			self._no = val

	@property
	def adresse(self):
	    return self._adresse

	@adresse.setter
	def adresse(self, val):
		self._adresse = val
	
	@property
	def code(self):
	    return self._code

	@code.setter
	def code(self, val):
		self._code = val
	
	@property
	def ville(self):
	    return self._ville

	@ville.setter
	def ville(self, val):
		self._ville = val.upper()
	