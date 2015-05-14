from patrimoine import batiment


''' variables  '''
batiments = {}

''' fonctionnalitées '''
def ajouter_batiment(no_bat,nom,adresse):
	nouveau_bat = batiment.batiment(nom,adresse)
	if no_bat not in batiments.keys():
		batiments[no_bat] = nouveau_bat


def rechercher_batiment(no_bat):
	print(no_bat," ",batiments[no_bat])


def supprimer_batiment(no_bat):
	if no_bat not in batiments.keys():
		del batiments[no_bat]

def main():
	ajouter_batiment(1,"bat_1","adresse_1")
	ajouter_batiment(2,"bat_2","adresse_2")
	rechercher_batiment(1)

if __name__ == '__main__':
	main()
