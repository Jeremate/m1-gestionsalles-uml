from m1_gestionsalles_uml.main import GestionAPI

class TestGestionAPI(object):
	#Classe représentant le systeme de gestion de salle

	def test_ajouter_adresse(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		test_adresses = "{'Adresse 1': 101 rue général buat, 44000 - NANTES}"
		assert str(systeme.adresses) == test_adresses

	def test_supprimer_adresse(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.supprimer_adresse("Adresse 1")
		assert systeme.adresses == {}

	def test_ajouter_titre(self):
	 	systeme = GestionAPI()
	 	systeme.ajouter_titre(1, "Maitre de conférence", 100)
	 	assert str(systeme.titres) == "{1: 1 Maitre de conférence 100}"

	def test_supprimer_titre(self):
	 	systeme = GestionAPI()
	 	systeme.ajouter_titre(1, "Résident", 100)
	 	systeme.supprimer_titre(1)
	 	assert systeme.titres == {}

	def test_ajouter_manifestation(self):
		systeme = GestionAPI()
		systeme.ajouter_manifestation(1, "Convention", 100)
		assert str(systeme.manifestations) == "{1: 1 Convention 100}"

	def test_supprimer_manifestation(self):
		systeme = GestionAPI()
		systeme.ajouter_manifestation(1, "Convention", 100)
		systeme.supprimer_manifestation(1)
		assert systeme.manifestations == {}

	def test_ajouter_duree(self):
		systeme = GestionAPI()
		systeme.ajouter_duree(1, "1 journée", 100)
		assert str(systeme.durees) == "{1: 1 1 journée 100}"

	def test_supprimer_duree(self):
		systeme = GestionAPI()
		systeme.ajouter_duree(1, "1 journée", 100)
		systeme.supprimer_duree(1)
		assert systeme.durees == {}

	def test_ajouter_origine(self):
		systeme = GestionAPI()
		systeme.ajouter_origine(1, "Résident", 100)
		assert str(systeme.origines) == "{1: 1 Résident 100}"

	def test_supprimer_origine(self):
		systeme = GestionAPI()
		systeme.ajouter_origine(1, "Résident", 100)
		systeme.supprimer_origine(1)
		assert systeme.origines == {}

	# origines = property(origines)

	# def batiments(self):
	#     return self.GP.batiments

	# def ajouter_batiment(self,no_bat, nom, adresse):
	# 	self.GP.ajouter_batiment(no_bat, nom, adresse)

	# batiments = property(batiments)
	
	# def rechercher_batiment(self, no_bat):
	# 	self.GP.rechercher_batiment(no_bat)

	# def modifier_batiment(self, no_bat, nom, adresse):
	# 	self.GP.modifier_batiment(no_bat, nom, adresse)

	# def supprimer_batiment(self, no_bat):
	# 	self.GP.supprimer_batiment(no_bat)
	# #------------------------------------------

	# #fonctionnalitées typesalle
	# def typesalles(self):
	#     return self.GP.typesalles

	# def ajouter_typesalle(self, code, libelle, montant):
	# 	self.GP.ajouter_typesalle(code, libelle, montant)

	# def supprimer_typesalle(self, code):
	# 	self.GP.supprimer_typesalle(code)

	# def consulter_typesalle(self, code):
	# 	self.GP.consulter_typesalle(code)

	# typesalles = property(typesalles)
	# #-------------------------------------------

	# #fonctionnalitées materiel
	# def materiels(self):
	#     return self.GP.materiels

	# def ajouter_materiel(self, code_inv, libelle, montant):
	# 	self.GP.ajouter_materiel(code_inv, libelle, montant)

	# def supprimer_materiel(self, code_inv):
	# 	self.GP.supprimer_materiel(code_inv)

	# def consulter_materiel(self, code_inv):
	# 	self.GP.consulter_materiel(code_inv)

	# materiels = property(materiels)
	# #------------------------------------------

	# #fonctionnalitées typemateriel
	# def typemateriels(self):
	#     return self.GP.typemateriels

	# def ajouter_typemateriel(self, code, libelle, montant):
	# 	self.GP.ajouter_typemateriel(code, libelle, montant)

	# def supprimer_typemateriel(self, nom):
	# 	self.GP.supprimer_typemateriel(nom)

	# def consulter_typemateriel(self, nom):
	# 	self.GP.consulter_typemateriel(nom)

	# typemateriels = property(typemateriels)

	# #fonctionnalitées salle
	# #fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	# def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
	# 	self.GP.associer_materiel(no_bat, no_etage, no_salle, code_inv)

	# def salles(self):
	# 	return self.GP.salles

	# def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
	# 	self.GP.ajouter_salle(no_bat, no_etage, no_salle, superficie, nom_typesalle)

	# #fonction pour supprimer une salle
	# def supprimer_salle(self, no_bat, no_etage, no_salle):
	# 	self.GP.supprimer_salle(no_bat, no_etage, no_salle)

	# salles = property(salles)
	# #-------------------------------

	# #fonctionnalitées pour la classe demandeur
	# def demandeurs(self):
	# 	return self.GD.demandeurs

	# def ajouter_demandeur(self, no_dem, nom, id_adresse, nom_origine, id_titre):
	# 	self.GD.ajouter_demandeur(no_dem, nom, id_adresse, nom_origine, id_titre)

	# def supprimer_demandeur(self, no_dem):
	# 	self.GD.supprimer_demandeur(no_dem)

	# demandeurs = property(demandeurs)
	# #--------------------------------

	# #fonctionnalitées pour la classe réservation
	# def reservations(self):
	# 	return self.GR.reservations

	# def calculer_montant(self, ref_resa):
	# 	self.GR.calculer_montant(ref_resa)

	# def ajouter_reservation(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
	# 	self.GR.ajouter_reservation(ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree)

	# def consulter_reservation(self, ref_resa):
	# 	self.GR.consulter_reservation(ref_resa)

	# reservations = property(reservations)

	
	# #----------------------------------------
