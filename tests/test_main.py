import m1_gestionsalles_uml.main as m


class TestMain:
	"""Tests pour la classe main"""


	def test_ajouter_salle(self):
		m.systeme.ajouter_typesalle("Classe", "Classe", "Salle de classe", 100)
		m.systeme.ajouter_batiments(1, "Batiment 1", "Adresse 1")
		m.systeme.ajouter_salle(1, 1, 1 ,10 , "Classe")
		assert m.systeme.batiments == {1: 1 Batiment 1 Adresse 1 {'1 1 1': 1 1 1 10 Classe}}
