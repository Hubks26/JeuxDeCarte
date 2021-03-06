from display.StateManager import StateManager

def main():
	try:
		sm = StateManager()

		sm.welcome()
		sm.run()
		sm.goodbye()

	except NotImplementedError:
		print("\nCette fonctionnalité n'est pas encore implémentée")

if __name__ == '__main__':
	main()