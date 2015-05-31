class Demandeur(object):
	"""Classe représentant un demandeur.

	Attributs:
		no_dem : numéro unique du demandeur
		nom : nom du demandeur
		adresse : identifiant de l'adresse du demandeur
		origine : origine du demandeur
		titre : titre du deandeur

	"""
	def __init__(self,no_dem,nom,id_adresse,origine,titre):
		super(Demandeur, self).__init__()
		self.no_dem = no_dem
		self.nom = nom
		self.adresse = id_adresse
		self.origine = origine
		self.titre = titre 

	def __str__(self):
		return "{} {} {} {} {}".format(self.no_dem,self.nom,self.adresse,self.origine,self.titre)

	def __repr__(self):
		return "{} {} {} {} {}".format(self.no_dem,self.nom,self.adresse,self.origine,self.titre)

	@property
	def no_dem(self):
	    return self._no_dem

	@no_dem.setter
	def no_dem(self, val):
		self._no_dem = val

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val
