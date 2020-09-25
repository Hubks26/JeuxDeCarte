
class GameOfCard:
	def __init__(self, nom, rules=None):
		self.nom = nom
		self.rules = rules

	def run(self, info):
		raise NotImplementedError