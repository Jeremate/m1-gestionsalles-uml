from m1_gestionsalles_uml.localisation.adresse import Adresse

class GestionLocalisation(object):

	__instance = None

	def __new__(cls):
		if GestionLocalisation.__instance is None:
			GestionLocalisation.__instance = object.__new__(cls)
			GestionLocalisation.__instance._adresses = {}
		return GestionLocalisation.__instance

	def adresses(self):
		return GestionLocalisation.__instance._adresses

	def ajouter_adresse(self, id_adresse, no, adresse, code, ville):
		if id_adresse not in self.adresses:
			self.adresses[id_adresse] = Adresse(no, adresse, code, ville)

	def supprimer_adresse(self, id_adresse):
		if id_adresse in self.adresses:
			del self.adresses[id_adresse]

	adresses = property(adresses)