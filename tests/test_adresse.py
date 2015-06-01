import m1_gestionsalles_uml.localisation.adresse as loc_adr
import m1_gestionsalles_uml.localisation.gestionlocalisation as gesloc

class TestAdresse:
	"""Tests pour la classe Adresse"""

	def test_init(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "nantes")
		assert adresse1.no == 1
		assert adresse1.adresse == "Boulevard Michelet"
		assert adresse1.code == 44000
		assert adresse1.ville == "NANTES"

	def test_affichage(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "nantes")
		assert repr(adresse1) == "1 Boulevard Michelet, 44000 - NANTES"

	def test_comparaison(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "nantes")
		adresse2 = loc_adr.Adresse(3, "Boulevard Michelet", 44000, "Nantes")
		assert adresse1 != adresse2

class TestGestionLocalisation:
	""" Tests pour la classe gestionlocalisation """
	def test_init(self):
		api = gesloc.GestionLocalisation()
		assert api.adresses == {}