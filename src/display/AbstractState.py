from abc import ABC, abstractmethod

class AbstractState:
	def __init__(self):
		pass

	@abstractmethod
	def run(self):
		raise NotImplementedError