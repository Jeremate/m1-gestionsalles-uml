import m1_gestionsalles_uml.localisation.adresse as loc_adr

class TestAdresse:
	"""Tests pour la classe Adresse"""

	def test_no(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "NANTES")
		assert adresse1.no == 1

	def test_adresse(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "NANTES")
		assert adresse1.adresse == "Boulevard Michelet"

	def test_code(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "NANTES")
		assert adresse1.code == 44000

	def test_ville(self):
		adresse1 = loc_adr.Adresse(1, "Boulevard Michelet", 44000, "nantes")
		assert adresse1.ville == "NANTES"