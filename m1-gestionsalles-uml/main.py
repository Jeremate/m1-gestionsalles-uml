from patrimoine import batiment
from patrimoine import typesalle

''' variables  '''
''' liste des batiment'''
batiments = {}
typesalles = []

''' fonctionnalitées batiment'''
def ajouter_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.batiment(nom,adresse)
	if no_bat not in batiments.keys():
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	print(no_bat," ",batiments[no_bat])


def modifier_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.batiment(nom,adresse)
	if no_bat in batiments.keys():
		batiments[no_bat] = nouveau_bat

def supprimer_batiment(no_bat):
	if no_bat not in batiments.keys():
		del batiments[no_bat]

'''fonctionnalitées typesalle'''
def ajouter_typesalle(nom):
	var_ajout = 1
	for ts in typesalles:
		if ts.getnom() == nom:
			var_ajout = 0
	if var_ajout:
		nouveau_typesalle = typesalle.typesalle(nom)
		typesalles.append(nouveau_typesalle)

def main():
	ajouter_batiment(1,"bat_1","adresse_1")
	'''ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)'''
	ajouter_typesalle("wow")
	print(typesalles)
	print(batiments)

if __name__ == '__main__':
	main()
