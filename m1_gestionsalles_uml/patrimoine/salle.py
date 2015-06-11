class Salle(object):

	def __init__(self, no_bat, no_etage, no_salle, superficie, typesalle):
		super(Salle, self).__init__()
		self.no_etage = no_etage
		self.no_salle = no_salle
		self.no_bat = no_bat
		self.superficie = superficie
		self.typesalle = typesalle
		self.materiels = {}


	@property
	def materiels(self):
	    return self._materiels

	@materiels.setter
	def materiels(self, val):
		self._materiels = val

	@property
	def no_etage(self):
	    return self._no_etage

	@no_etage.setter
	def no_etage(self, val):
		self._no_etage = val

	@property
	def no_salle(self):
	    return self._no_salle

	@no_salle.setter
	def no_salle(self, val):
		self._no_salle = val
		
	@property
	def no_bat(self):
	    return self._no_bat

	@no_bat.setter
	def no_bat(self, val):
		self._no_bat = val

	@property
	def superficie(self):
	    return self._superficie

	@superficie.setter
	def superficie(self, val):
		self._superficie = val

	@property
	def typesalle(self):
	    return self._typesalle

	@typesalle.setter
	def typesalle(self, val):
		self._typesalle = val

	def __repr__(self):
		return "{} {} {} {} {} {}".format(self.no_salle, self.no_bat, self.no_etage, self.superficie, self.typesalle, self.materiels)

	def __str__(self):
		return "{} {} {} {} {} {}".format(self.no_salle, self.no_bat, self.no_etage, self.superficie, self.typesalle, self.materiels)

	def associer_materiel(self, code_inv, mat):
		if code_inv not in self.materiels:
			self.materiels[code_inv] = mat