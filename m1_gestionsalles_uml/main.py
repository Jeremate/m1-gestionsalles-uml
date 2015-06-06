from patrimoine.gestionpatrimoine import GestionPatrimoine
from demandeur.gestiondemandeur import GestionDemandeur
from localisation.gestionlocalisation import GestionLocalisation
from reservation.gestionreservation import GestionReservation


class GestionAPI(object):
	#Classe représentant le systeme de gestion de salle
	
	def __init__(self):
		super(GestionAPI, self).__init__()
		GP = GestionPatrimoine()
		GD = GestionDemandeur()
		GL = GestionLocalisation()
		GR = GestionReservation()

	def adresses(self):
		return GL.adresses

	def ajouter_adresse(self, id_adresse, no, adresse, code, ville):
		GL.ajouter_adresse(id_adresse, no, adresse, code, ville)

	def supprimer_adresse(self, id_adresse):
		GL.supprimer_adresse(id_adresse)

	adresses = property(adresses)

	def titres(self):
		return GD.titres

	def ajouter_titre(self, code, libelle, montant):
		GD.ajouter_titre(code, libelle, montant)

	def supprimer_titre(self, code):
		GD.supprimer_titre(code)

	titres = property(titres)

	def manifestations(self):
		return GR.manifestations

	def ajouter_manifestation(self, code, libelle, montant):
		GR.ajouter_manifestation(code, libelle, montant)

	def supprimer_manifestation(self, code):
		GR.supprimer_manifestation(code)

	manifestations = property(manifestations)


	def durees(self):
		return GR.durees

	def ajouter_duree(self, code, libelle, montant):
		GR.ajouter_duree(code, libelle, montant)

	def supprimer_duree(self, code):
		GR.supprimer_duree(code)

	durees = property(durees)

	def origines(self):
		return GD.origines

	def ajouter_origine(self, code, libelle, montant):
		GD.ajouter_origine(code, libelle, montant)

	def supprimer_origine(self, code):
		GD.supprimer_origine(code)

	origines = property(origines)

	def batiments(self):
	    return GP.batiments

	def ajouter_batiment(self,no_bat, nom, adresse):
		GP.ajouter_batiment(no_bat, nom, adresse)

	batiments = property(batiments)
	
	def rechercher_batiment(self, no_bat):
		GP.rechercher_batiment(no_bat)

	def modifier_batiment(self, no_bat, nom, adresse):
		GP.modifier_batiment(no_bat, nom, adresse)

	def supprimer_batiment(self, no_bat):
		GP.supprimer_batiment(no_bat)
	#------------------------------------------

	#fonctionnalitées typesalle
	def typesalles(self):
	    return GP.typesalles

	def ajouter_typesalle(self, code, libelle, montant):
		GP.ajouter_typesalle(code, libelle, montant)

	def supprimer_typesalle(self, code):
		GP.supprimer_typesalle(code)

	def consulter_typesalle(self, code):
		GP.consulter_typesalle(code)

	typesalles = property(typesalles)
	#-------------------------------------------

	#fonctionnalitées materiel
	def materiels(self):
	    return GP.materiels

	def ajouter_materiel(self, code_inv, libelle, montant):
		GP.ajouter_materiel(code_inv, libelle, montant)

	def supprimer_materiel(self, code_inv):
		GP.supprimer_materiel(code_inv)

	def consulter_materiel(self, code_inv):
		GP.consulter_materiel(code_inv)

	materiels = property(materiels)
	#------------------------------------------

	#fonctionnalitées typemateriel
	def typemateriels(self):
	    return GP.typemateriels

	def ajouter_typemateriel(self, code, libelle, montant):
		GP.ajouter_typemateriel(code, libelle, montant)

	def supprimer_typemateriel(self, nom):
		GP.supprimer_typemateriel(nom)

	def consulter_typemateriel(self, nom):
		GP.consulter_typemateriel(nom)

	typemateriels = property(typemateriels)

	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
		GP.associer_materiel(no_bat, no_etage, no_salle, code_inv)

	def salles(self):
		return GP.salles

	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
		GP.ajouter_salle(no_bat, no_etage, no_salle, superficie, nom_typesalle)

	#fonction pour supprimer une salle
	def supprimer_salle(self, no_bat, no_etage, no_salle):
		GP.supprimer_salle(no_bat, no_etage, no_salle)

	salles = property(salles)
	#-------------------------------

	#fonctionnalitées pour la classe demandeur
	def demandeurs(self):
		return GD.demandeurs

	def ajouter_demandeur(self, no_dem, nom, id_adresse, nom_origine, id_titre):
		GD.ajouter_demandeur(no_dem, nom, id_adresse, nom_origine, id_titre)

	def supprimer_demandeur(self, no_dem):
		GD.supprimer_demandeur(no_dem)

	demandeurs = property(demandeurs)
	#--------------------------------

	#fonctionnalitées pour la classe réservation
	def reservations(self):
		return GR.reservations

	def calculer_montant(self, ref_resa):
		GR.calculer_montant(ref_resa)

	def ajouter_reservation(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
		GR.ajouter_reservation(ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree)

	def consulter_reservation(self, ref_resa):
		GR.consulter_reservation(ref_resa)

	reservations = property(reservations)

	
	#----------------------------------------

def main():

	systeme = GestionAPI()
	"""systeme.ajouter_adresse("Adresse 1", 10, "Rue des Landes", "44300", "Nantes")
				systeme.ajouter_batiment(1,"Batiment 1","Adresse 1")
				#systeme.supprimer_batiment(1)
				#print (systeme.rechercher_batiment(1))
				systeme.ajouter_typemateriel("Télévision","télévision HD LCD",100)
				print (systeme.typemateriels)
				systeme.ajouter_typesalle("Classe", "salle de classe", 200)
				systeme.ajouter_salle(1,1,1,10,"Classe")
				#systeme.supprimer_salle(1,1,1)
				print(systeme.batiments)
				systeme.associer_materiel(1,1,1,"Télévision")
				systeme.ajouter_origine("Resident","résident",100)
				systeme.ajouter_titre("Etudiant", "Etudiant", 100)
				systeme.ajouter_manifestation("Gratuit","Evenement gratuit", 0)
				systeme.ajouter_duree("2","2 heures minutes",50)
				print(systeme.durees)
				systeme.ajouter_demandeur(1, "Boceno", "Adresse 1", "Resident", "Etudiant")
				print(systeme.demandeurs)
				systeme.ajouter_reservation(1, "31/05/2015", 1, 1, 1, 1, "Gratuit", "2")
				print(systeme.reservations)"""

if __name__ == '__main__':
	main()
