from m1_gestionsalles_uml.localisation.gestionlocalisation import GestionLocalisation
from m1_gestionsalles_uml.patrimoine.gestionpatrimoine import GestionPatrimoine
from m1_gestionsalles_uml.demandeur.gestiondemandeur import GestionDemandeur
from m1_gestionsalles_uml.reservation.gestionreservation import GestionReservation


class GestionAPI(object):
	#Classe représentant le systeme de gestion de salle
	
	def __init__(self):
		super(GestionAPI, self).__init__()
		self.GP = GestionPatrimoine()
		self.GD = GestionDemandeur()
		self.GL = GestionLocalisation()
		self.GR = GestionReservation()

	def adresses(self):
		return self.GL.adresses

	def ajouter_adresse(self, id_adresse, no, adresse, code, ville):
		self.GL.ajouter_adresse(id_adresse, no, adresse, code, ville)

	def supprimer_adresse(self, id_adresse):
		self.GL.supprimer_adresse(id_adresse)

	adresses = property(adresses)

	def titres(self):
		return self.GD.titres

	def ajouter_titre(self, code, libelle, montant):
		self.GD.ajouter_titre(code, libelle, montant)

	def supprimer_titre(self, code):
		self.GD.supprimer_titre(code)

	titres = property(titres)

	def manifestations(self):
		return self.GR.manifestations

	def ajouter_manifestation(self, code, libelle, montant):
		self.GR.ajouter_manifestation(code, libelle, montant)

	def supprimer_manifestation(self, code):
		self.GR.supprimer_manifestation(code)

	manifestations = property(manifestations)


	def durees(self):
		return self.GR.durees

	def ajouter_duree(self, code, libelle, montant):
		self.GR.ajouter_duree(code, libelle, montant)

	def supprimer_duree(self, code):
		self.GR.supprimer_duree(code)

	durees = property(durees)

	def origines(self):
		return self.GD.origines

	def ajouter_origine(self, code, libelle, montant):
		self.GD.ajouter_origine(code, libelle, montant)

	def supprimer_origine(self, code):
		self.GD.supprimer_origine(code)

	origines = property(origines)

	def batiments(self):
	    return self.GP.batiments

	def ajouter_batiment(self,no_bat, nom, adresse):
		self.GP.ajouter_batiment(no_bat, nom, adresse)

	batiments = property(batiments)
	
	def rechercher_batiment(self, no_bat):
		return self.GP.rechercher_batiment(no_bat)

	def modifier_batiment(self, no_bat, nom, adresse):
		self.GP.modifier_batiment(no_bat, nom, adresse)

	def supprimer_batiment(self, no_bat):
		self.GP.supprimer_batiment(no_bat)
	#------------------------------------------

	#fonctionnalitées typesalle
	def typesalles(self):
	    return self.GP.typesalles

	def ajouter_typesalle(self, code, libelle, montant):
		self.GP.ajouter_typesalle(code, libelle, montant)

	def supprimer_typesalle(self, code):
		self.GP.supprimer_typesalle(code)

	def consulter_typesalle(self, code):
		self.GP.consulter_typesalle(code)

	typesalles = property(typesalles)
	#-------------------------------------------

	#fonctionnalitées materiel
	def materiels(self):
	    return self.GP.materiels

	def ajouter_materiel(self, code_inv, typemateriel):
		self.GP.ajouter_materiel(code_inv, typemateriel)

	def supprimer_materiel(self, code_inv):
		self.GP.supprimer_materiel(code_inv)

	def consulter_materiel(self, code_inv):
		self.GP.consulter_materiel(code_inv)

	materiels = property(materiels)
	#------------------------------------------

	#fonctionnalitées typemateriel
	def typemateriels(self):
	    return self.GP.typemateriels

	def ajouter_typemateriel(self, code, libelle, montant):
		self.GP.ajouter_typemateriel(code, libelle, montant)

	def supprimer_typemateriel(self, nom):
		self.GP.supprimer_typemateriel(nom)

	def consulter_typemateriel(self, nom):
		self.GP.consulter_typemateriel(nom)

	typemateriels = property(typemateriels)

	#fonctionnalitées salle
	#fonction d'ajout d'une salle si le batiment ou le typesalle n'existe pas alors la fonction est abandonné
	def associer_materiel(self, no_bat, no_etage, no_salle, code_inv):
		self.GP.associer_materiel(no_bat, no_etage, no_salle, code_inv)

	def salles(self):
		return self.GP.salles

	def ajouter_salle(self, no_bat, no_etage, no_salle, superficie, nom_typesalle):
		self.GP.ajouter_salle(no_bat, no_etage, no_salle, superficie, nom_typesalle)

	#fonction pour supprimer une salle
	def supprimer_salle(self, no_bat, no_etage, no_salle):
		self.GP.supprimer_salle(no_bat, no_etage, no_salle)

	salles = property(salles)
	#-------------------------------

	#fonctionnalitées pour la classe demandeur
	def demandeurs(self):
		return self.GD.demandeurs

	def ajouter_demandeur(self, no_dem, nom, id_adresse, nom_origine, id_titre):
		self.GD.ajouter_demandeur(no_dem, nom, id_adresse, nom_origine, id_titre)

	def supprimer_demandeur(self, no_dem):
		self.GD.supprimer_demandeur(no_dem)

	demandeurs = property(demandeurs)
	#--------------------------------

	#fonctionnalitées pour la classe réservation
	def reservations(self):
		return self.GR.reservations

	def ajouter_reservation(self, ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree):
		self.GR.ajouter_reservation(ref_resa, date, no_dem, no_bat, no_etage, no_salle, code_manifestation, code_duree)

	def consulter_reservation(self, ref_resa):
		return self.GR.consulter_reservation(ref_resa)

	reservations = property(reservations)

	
	#----------------------------------------
