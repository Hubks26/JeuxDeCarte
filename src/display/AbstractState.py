from abc import ABC, abstractmethod

class AbstractState(ABC):
	def __init__(self):
		pass

	@abstractmethod
	def run(self):
		raise NotImplemented