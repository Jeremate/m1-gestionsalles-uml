from demandeur.titre import Titre
from demandeur.origine import Origine
from demandeur.demandeur import Demandeur
from localisation.gestionlocalisation import GestionLocalisation

class GestionDemandeur(object):

	__instance = None
	def __new__(cls):
		if GestionDemandeur.__instance is None:
			GestionDemandeur.__instance = object.__new__(cls)
			GestionDemandeur.__instance._titres = {}
			GestionDemandeur.__instance._origines = {}
			GestionDemandeur.__instance._demandeurs = {}
			GestionDemandeur.__instance._adresses = GestionLocalisation()
		return GestionDemandeur.__instance

	

	def adresses(self):
		return GestionDemandeur.__instance._adresses.adresses

	adresses = property(adresses)

	#fonctionnalitées titre
	def titres(self):
		return GestionDemandeur.__instance._titres

	def ajouter_titre(self, code, libelle, montant):
		if code not in self.titres:
			self._titres[code] = Titre(code, libelle, montant)

	def supprimer_titre(self, code):
		if code in self.titres:
			del self._titres[code]

	titres = property(titres)

	#fonctionnalitées origines
	def origines(self):
		return GestionDemandeur.__instance._origines

	def ajouter_origine(self, code, libelle, montant):
		if code not in self.origines:
			self.origines[code] = Origine(code, libelle, montant)

	def supprimer_origine(self, code):
		if code in self.origines:
			del self.origines[code]

	origines = property(origines)
	#------------------------------------------

	#fonctionnalitées pour la classe demandeur
	def demandeurs(self):
		return GestionDemandeur.__instance._demandeurs

	def ajouter_demandeur(self, no_dem, nom, id_adresse, code_origine, code_titre):
		print(self.adresses)
		if no_dem not in self.demandeurs:
			if code_origine in self.origines:
				if code_titre in self.titres:
					if id_adresse in self.adresses:
						self.demandeurs[no_dem] = Demandeur(no_dem, nom , id_adresse, code_origine, code_titre)

	def supprimer_demandeur(self, no_dem):
		if no_dem in self.demandeurs:
			del self.demandeurs[no_dem]

	demandeurs = property(demandeurs)
	#---------------------------------------------

a = GestionDemandeur()
b = GestionLocalisation()
b.ajouter_adresse(1,1,1,1,"a")
#a.ajouter_adresse(1,1,1,1,"a")
a.ajouter_origine(1,"resident",100)
a.ajouter_titre(1,"etudiant",100)
a.ajouter_demandeur(1,"Boceno",1,1,1)
print(a.demandeurs)
#print(a.adresses)
