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
		super(Adresse, self).__init__()
		self.no = no
		self.adresse = adresse
		self.code = code
		self.ville = ville

	def __repr__(self):
		"""Représentation de la classe Adresse"""
		return "{} {}, {} - {}".format(self.no, self.adresse, self.code, self.ville)

	def __str__(self):
		"""Affichage de la classe Adresse"""
		return "{} {}, {} - {}".format(self.no, self.adresse, self.code, self.ville)

	def __eq__(self, autre_adresse):
		"""Surcharge de l'opérateur d'égalité"""
		if isinstance(autre_adresse, self.__class__):
			return self.__dict__ == autre_adresse.__dict__
		else:
			return False

	def __ne__(self, autre_adresse):
		return not self.__eq__(autre_adresse)

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
	