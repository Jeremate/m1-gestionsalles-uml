import m1_gestionsalles_uml.localisation.adresse as loc_adr
import m1_gestionsalles_uml.patrimoine.batiment as bat
import m1_gestionsalles_uml.patrimoine.typesalle as ts
import m1_gestionsalles_uml.patrimoine.materiel as mat
import m1_gestionsalles_uml.patrimoine.typemateriel as tm
import m1_gestionsalles_uml.patrimoine.salle as sal
import m1_gestionsalles_uml.patrimoine.typesalle as ts
import m1_gestionsalles_uml.main


class TestMain:
	"""Tests pour la classe main"""


	#fonctionnalitées batiment
	def test_ajouter_batiment(self):
		ajouter_batiment(1,"Batiment1","adresse")
		nouveau_bat = bat.Batiment("Batiment1","adresse")
		assert batiments == {1:nouveau_bat}


	def test_rechercher_batiment(self):
		assert rechercher_batiment(1) == "1 Batmiment1 adresse"


	def test_modifier_batiment(self):
		modifier_batiment(1,"BatimentR","adresse")
		nouveau_bat = bat.Batiment("BatimentR","adresse")
		assert batiments == {1:nouveau_bat}

	def test_supprimer_batiment(self):
		supprimer_batiment(1)
		assert batiments == []

	#fonctionnalitées typesalle
	def test_ajouter_typesalle(self):
		ajouter_typesalle("classe")
		assert typesalles == ["classe"]


	def test_supprimer_typesalle(self):
		supprimer_typesalle("classe")
		assert typesalles == []


	def test_consulter_typesalle(self):
		ajouter_typesalle("garage")
		assert consulter_typesalle("garage") == ts.Typesalle("garage")


	#fonctionnalitées materiel
	def test_ajouter_materiel(self):
		ajouter_materiel(1)
		assert materiels == [1]

	def test_supprimer_materiel(self):
		supprimer_materiel(1)
		assert materiels == []


	#fonctionnalitées typemateriel
	def test_ajouter_typemateriel(self):
		ajouter_typemateriel("television")
		assert typemateriels == ["television"]

	def test_supprimer_typemateriel(self):
		for tm in typemateriels:
			if tm.nom == nom:
				"""typemateriels.remove(tm)
													break"""

	def test_consulter_typemateriel(nom):
		for tm in typemateriels:
			if tm.nom == nom:
				return tm


	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def test_ajouter_salle(self):
		ajouter_typesalle("vestiaire")
		ajouter_salle(1,1,1,10,typesalles[1])
		assert salles == [1,1,1,10,"vestiaire"]

	#fonction pour supprimer une salle
	def test_supprimer_salle(self):
		supprimer_salle(salles[0])
		assert salles == []