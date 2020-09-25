#from business.actors.AbstractUser import AbstractUser
from business.GameOfCard import GameOfCard
from display.StateMenu import StateMenu

liste_des_jeux_de_carte = [GameOfCard('Solitaire'), GameOfCard('Tarot'), GameOfCard('Belote'), GameOfCard('Poker')]

class Guest: #(AbstractUser):
	def __init__(self):
		pass

	def playOffline(self, pState):
		question = 'À quel jeu voulez vous jouer ?'
		choices = [game.nom for game in liste_des_jeux_de_carte]
		actions = [game.run for game in liste_des_jeux_de_carte]
		return StateMenu(question, choices, actions, pState)
3