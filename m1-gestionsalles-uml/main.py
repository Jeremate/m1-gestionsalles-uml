from patrimoine import batiment


''' variables  '''
''' liste des batiment'''
batiments = {}

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

def main():
	ajouter_batiment(1,"bat_1","adresse_1")
	ajouter_batiment(2,"bat_2","adresse_2")
	modifier_batiment(2,"bat_3","adresse_3")
	rechercher_batiment(2)

if __name__ == '__main__':
	main()
