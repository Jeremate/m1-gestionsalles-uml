from patrimoine import batiment
from patrimoine import typesalle
from patrimoine import materiel
from patrimoine import typemateriel
from patrimoine import salle
from patrimoine import typesalle

#variables
#liste des batiment
batiments = {}
typesalles = []
materiels = []
typemateriels = []
salles = []

#fonctionnalitées batiment
def ajouter_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.Batiment(nom,adresse)
	if no_bat not in batiments.keys():
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	print(no_bat," ",batiments[no_bat])


def modifier_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.Batiment(nom,adresse)
	if no_bat in batiments.keys():
		batiments[no_bat] = nouveau_bat

def supprimer_batiment(no_bat):
	if no_bat not in batiments.keys():
		del batiments[no_bat]

#fonctionnalitées typesalle
def ajouter_typesalle(nom):
	var_ajout = 1
	for ts in typesalles:
		if ts.getnom() == nom:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_typesalle = typesalle.Typesalle(nom)
		typesalles.append(nouveau_typesalle)

def supprimer_typesalle(nom):
	for ts in typsalles:
		if ts.getnom() == nom:
			typesalle.remove(ts)

def consulter_typesalle(nom):
	for ts in typesalles:
		if ts.getnom() == nom:
			print(ts)

#fonctionnalitées materiel
def ajouter_materiel(code_inv):
	var_ajout = 1
	for m in materiels:
		if m.get_id() == code_inv:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_materiel = materiel.Materiel(code_inv)
		materiels.append(nouveau_materiel)

def supprimer_materiel(code_inv):
	for m in materiels:
		if m.get_id() == code_inv:
			materiels.remove(m)
			break


"""#fonctionnalitées typemateriel
def ajouter_typemateriel(nom):
	var_ajout = 1
	for tm in typemateriels:
		if ts.getnom() == nom:
			var_ajout = 0
			break
	if var_ajout:
		nouveau_typemateriel = typemateriel.Typemateriel(nom)
		typemateriels.append(nouveau_typemateriel)

def supprimer_typemateriel(nom):
	for tm in typemateriels:
		if tm.getnom() == nom:
			typemateriels.remove(ts)

def consulter_typemateriel(nom):
	for tm in typemateriels:
		if tm.getnom() == nom:
			print(ts)"""


#fonctionnalitées salle


def main():
	ajouter_batiment(1,"bat_1","adresse_1")
	"""ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)"""
	#ajouter_typemateriel("wow")
	#supprimer_typemateriel("wow")
	#supprimer_typesalle()
	print(typemateriels)
	print(batiments)

if __name__ == '__main__':
	main()
