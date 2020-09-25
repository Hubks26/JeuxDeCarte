from display.StateMenu import StateMenu
from display.StateClose import StateClose
from business.actors.Guest import Guest

initialMenu = StateMenu('Que voulez vous faire ?',
                        ['Se connecter',
                         'Créer un compte',
                         "Jouer hors ligne en tant qu'invité"],
                        [lambda actualState : StateClose(),
                         lambda actualState : StateClose(),
                         Guest().playOffline])

class StateManager:

	@staticmethod
	def welcome():
		print('\n\tBonjour !\n')

	@staticmethod
	def goodbye():
		print('\n\tAu revoir !\n')

	@staticmethod
	def border():
		print('--------------------------------------------------------')

	@staticmethod
	def run():
		actualState = initialMenu
		while actualState:
			# La boucle s'arrête après être tombée sur un état fermé. En effet, le fait
			# de "run" un état fermé renvoie None, ce qui permet de sortir de la boucle.

			StateManager.border()  # On affiche une bordure pour séparer les menus

			actualState = actualState.run()