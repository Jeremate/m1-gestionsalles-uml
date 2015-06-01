from demandeur.titre import Titre
from demandeur.origine import Origine
from demandeur.demandeur import Demandeur
from localisation.gestionlocalisation import GestionLocalisation

class GestionDemandeur(object):

	def __init__(self):
		self.demandeurs = {}
		self.titres = {}
		self.origines = {}

	#fonctionnalitées pour la classe demandeur
	def demandeurs(self):
		return self._demandeurs

	def ajouter_demandeur(self, no_dem, nom, id_adresse, code_origine, code_titre):
		if no_dem not in self._demandeurs:
			if code_origine in self._origines:
				if code_titre in self._titres:
					if id_adresse in self._adresses:
						self._demandeurs[no_dem] = Demandeur(no_dem, nom , id_adresse, code_origine, code_titre)

	def supprimer_demandeur(self, no_dem):
		if no_dem in self._demandeurs:
			del self._demandeurs[no_dem]

	demandeurs = property(demandeurs, ajouter_demandeur)
	#---------------------------------------------
	
	#fonctionnalitées titre
	def titres(self):
		return self._titres

	def ajouter_titre(self, code, libelle, montant):
		if code not in self._titres:
			self._titres[code] = Titre(code, libelle, montant)

	def supprimer_titre(self, code):
		if code in self._titres:
			del self._titres[code]

	titres = property(titres, ajouter_titre)

	#fonctionnalitées origines
	def origines(self):
		return self._origines

	def ajouter_origine(self, code, libelle, montant):
		if code not in self._origines:
			self._origines[code] = Origine(code, libelle, montant)

	def supprimer_origine(self, code):
		if code in self._origines:
			del self._origines[code]

	origines = property(origines,ajouter_origine)
	#------------------------------------------

