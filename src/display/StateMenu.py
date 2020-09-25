from display.AbstractState import AbstractState
from display.StateClose import StateClose

class StateMenu(AbstractState):
	def __init__(self, question, choices, actions, previousState=None, closeOpt=True):
		assert len(choices) == len(actions)
		self.question = question
		self.choices = choices
		self.actions = actions
		self.options = []
		self.nbChoices = len(choices)

		if previousState:
			self.options.append(['Retour', 'R'])
			self.actions.append(lambda actualState : previousState)

		if closeOpt:
			self.options.append(['Quitter', 'Q'])
			self.actions.append(lambda actualState : StateClose())

	def run(self):  # La méthode run permet d'afficher le menu et d'interagir avec l'utilisateur.
		choices = self.choices
		options = self.options
		nbChoices = self.nbChoices
		actions = self.actions
		keys = [opt[1] for opt in options] # Liste des codes des options basiques

		while True:  # On demande à l'utilisateur de choisir une option.

			print('\n\t{}\n'.format(self.question))  # On affiche la question du menu.

			for i, choice in enumerate(choices):  # On affiche les options du menu.
				print('[{}] {}'.format(i + 1, choice))

			if len(options) > 0: print('')

			for opt in options:  # On affiche les options de base : QUITTER, RETOUR...
				print('[{}] {}'.format(opt[1], opt[0]))

			choice = input('\n> ')
			try:
				choice = int(choice)
			except ValueError:
				if choice.upper() not in keys:
					print('\nVotre réponse ne correspond à aucune option.')
				else:
					choice = choice.upper()
					break
				continue
			if choice <= 0 or choice > nbChoices:
				print('\nVotre réponse ne correspond à aucune option.')
				continue
			break

		if choice in keys:
			index = keys.index(choice)
			return actions[nbChoices + index](self)
		else:
			return actions[choice - 1](self)  # On applique la fonction qui correspond au choix de l'utilisateur.