from patrimoine.salle import Salle

class Batiment(object):
	"""Classe représentant un batiment.

	Attributs:
		no_bat : Le numéro du batiement
		nom : Le nom du batiment
		adresse : L'objet contenant l'adresse du batiment
	"""
	def __init__(self,no_bat,nom,adresse):
		super(Batiment, self).__init__()
		self.no_bat = no_bat
		self.nom = nom
		self.adresse = adresse
		self.salles = {}


	def associer_materiel(self, no_bat, no_etage, no_salle, code_inv, mat):
		id_salle = str(no_bat)+" "+str(no_etage)+" "+str(no_salle)
		self.salles[id_salle].associer_materiel(code_inv, mat)

	def __str__(self):
		return "{} {} {} {}".format(self.no_bat, self.nom, self.adresse, self.salles)

	def __repr__(self):
		return "{} {} {} {}".format(self.no_bat, self.nom, self.adresse, self.salles)


	def salle_presente(self, no_bat, no_etage, no_salle):
		id_salle = str(no_bat)+" "+str(no_etage)+" "+str(no_salle)
		return id_salle in self.salles

	@property
	def nom(self):
	    return self._nom

	@nom.setter
	def nom(self, val):
		self._nom = val

	@property
	def no_bat(self):
	    return self._no_bat

	@no_bat.setter
	def no_bat(self, val):
		self._no_bat = val

	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, typesalle):
		id_salle = str(no_bat)+" "+str(no_etage)+" "+str(no_salle)
		self.salles[id_salle] = Salle(no_etage, no_salle, no_bat, superficie, typesalle)

	def supprimer_salle(self, no_bat, no_etage, no_salle):
		id_salle = str(no_bat)+" "+str(no_etage)+" "+str(no_salle)
		if id_salle in self.salles:
			del self.salles[id_salle]

		