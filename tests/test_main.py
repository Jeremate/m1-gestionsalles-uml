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

	def test_ajouter_batiment(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Université sciences et techniques", "Adresse 1")
		assert str(systeme.batiments) == "{1: 1 Université sciences et techniques Adresse 1 {}}"
	
	def test_rechercher_batiment(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Université sciences et techniques", "Adresse 1")
		assert systeme.rechercher_batiment(1) == systeme.batiments[1]

	def test_modifier_batiment(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Université sciences et techniques", "Adresse 1")
		systeme.modifier_batiment(1,"Changement description", "Adresse 1")
		assert str(systeme.batiments) == "{1: 1 Changement description Adresse 1 {}}"

	def test_supprimer_batiment(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Université sciences et techniques", "Adresse 1")
		systeme.supprimer_batiment(1)
		assert systeme.batiments == {}

	def test_ajouter_typesalle(self):
		systeme = GestionAPI()
		systeme.ajouter_typesalle(1,"Classe",100)
		assert str(systeme.typesalles) == "{1: 1 Classe 100}"

	def test_supprimer_typesalle(self):
		systeme = GestionAPI()
		systeme.ajouter_typesalle(1,"Classe",100)
		systeme.supprimer_typesalle(1)
		assert systeme.typesalles == {}

	def test_ajouter_materiel(self):
		systeme = GestionAPI()
		systeme.ajouter_typemateriel(1, "TV", 100)
		systeme.ajouter_materiel(1, 1)
		assert str(systeme.materiels) == "{1: 1}"

	def supprimer_materiel(self, code_inv):
		systeme = GestionAPI()
		systeme.ajouter_typemateriel(1, "TV", 100)
		systeme.ajouter_materiel(1, 1)
		systeme.supprimer_materiel(1)
		assert systeme.materiels == {}

	def test_ajouter_typemateriel(self):
		systeme = GestionAPI()
		systeme.ajouter_typemateriel(1, "TV", 100)
		assert str(systeme.typemateriels) == "{1: 1 TV 100}"

	def supprimer_typemateriel(self, nom):
		ssysteme = GestionAPI()
		systeme.ajouter_typemateriel(1, "TV", 100)
		systeme.supprimer_typemateriel(1)
		assert systeme.typemateriels == {}

	def test_ajouter_salle(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Batiment 1", "Adresse 1")
		systeme.ajouter_typesalle(1,"Classe",100)
		systeme.ajouter_salle(1,1,1,10,1)
		assert str(systeme.batiments) == "{1: 1 Batiment 1 Adresse 1 {'1 1 1': 1 1 1 10 1}}"

	def test_supprimer_salle(self):
		#suppression d'une salle
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Batiment 1", "Adresse 1")
		systeme.ajouter_typesalle(1,"Classe",100)
		systeme.ajouter_salle(1,1,1,10,1)
		systeme.supprimer_salle(1,1,1)
		assert str(systeme.batiments) == "{1: 1 Batiment 1 Adresse 1 {}}"
		#test de suppression d'une réservation associer a une salle lors de la suppression de celle ci
		systeme.ajouter_salle(1,1,1,10,1)
		systeme.ajouter_titre(1,"etudiant", 100)
		systeme.ajouter_origine(1, "résident", 100)
		systeme.ajouter_manifestation(1,"convention", 100)
		systeme.ajouter_duree(1, "1 journée", 100)
		systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", 1, 1)
		systeme.ajouter_reservation(1,"09/06/2015",1,1,1,1,1,1)
		systeme.supprimer_salle(1,1,1)
		assert systeme.reservations == {}

	#def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
	# 	self.GP.associer_materiel(no_bat, no_etage, no_salle, code_inv)

	def test_ajouter_demandeur(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_titre(1,"etudiant", 100)
		systeme.ajouter_origine(1, "résident", 100)
		systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", 1, 1)
		assert str(systeme.demandeurs) == "{1: 1 Boceno Adresse 1 1 1}"

	def test_supprimer_demandeur(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_titre(1,"etudiant", 100)
		systeme.ajouter_origine(1, "résident", 100)
		systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", 1, 1)
		systeme.supprimer_demandeur(1)
		assert systeme.demandeurs == {}

	def test_ajouter_reservation(self):
		systeme = GestionAPI()
		assert systeme.reservations == {}
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Batiment 1", "Adresse 1")
		systeme.ajouter_typesalle(1,"Classe",100)
		systeme.ajouter_salle(1,1,1,10,1)
		systeme.ajouter_titre(1,"etudiant", 100)
		systeme.ajouter_origine(1, "résident", 100)
		systeme.ajouter_manifestation(1,"convention", 100)
		systeme.ajouter_duree(1, "1 journée", 100)
		systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", 1, 1)
		systeme.ajouter_reservation(1,"09/06/2015",1,1,1,1,1,1)
		assert str(systeme.reservations) == "{1: 1 09/06/2015 500 1 1 1 1 1 1}"
		#test d'ajout d'une deuxieme reservation pour une salle a une date donnée
		systeme.ajouter_reservation(2,"09/06/2015",1,1,1,1,1,1)
		assert str(systeme.reservations) == "{1: 1 09/06/2015 500 1 1 1 1 1 1}"

	def test_consulter_reservation(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		systeme.ajouter_batiment(1,"Batiment 1", "Adresse 1")
		systeme.ajouter_typesalle(1,"Classe",100)
		systeme.ajouter_salle(1,1,1,10,1)
		systeme.ajouter_titre(1,"etudiant", 100)
		systeme.ajouter_origine(1, "résident", 100)
		systeme.ajouter_manifestation(1,"convention", 100)
		systeme.ajouter_duree(1, "1 journée", 100)
		systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", 1, 1)
		systeme.ajouter_reservation(1,"09/06/2015",1,1,1,1,1,1)
		assert str(systeme.consulter_reservation(1)) == "1 09/06/2015 500 1 1 1 1 1 1"
