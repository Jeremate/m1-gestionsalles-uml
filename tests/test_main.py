from m1_gestionsalles_uml.main import GestionAPI

class TestGestionAPI(object):
	#Classe représentant le systeme de gestion de salle

	def test_ajouter_adresse(self):
		systeme = GestionAPI()
		systeme.ajouter_adresse("Adresse 1", 101, "rue général buat", "44000", "Nantes")
		assert  systeme.adresses == "{'Adresse 1': 101 rue général buat, 44000 - NANTES}"
