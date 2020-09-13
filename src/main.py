from display.StateManager import StateManager


def main():
	try:
		sm = StateManager()

		sm.welcome()
		sm.run()
		sm.goodbye()

	except:
		print("Une erreur est survenue")


if __name__ == '__main__':
	main()