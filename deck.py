import random

class PlayerCards:
	"""docstring for PlayerCards"""
	aces, total = 0, 0
	cards = []

	def __init__(self):
		super(PlayerCards, self).__init__()

	def add_card(self, card):
		self.aces += 1 if card == 11 else 0
		self.total += card
		self.cards.append(card)

		return True

	def get_subtotal(self):
		totals = [self.total]
		for ace in range(1, self.aces + 1):
			totals.append(self.total - 10*ace)

		return totals


class PlayerOperation:
	"""docstring for PlayerOperation"""
	def __init__(self):
		super(PlayerOperation, self).__init__()

	def is_continue(self):
		return self.input('Do you want to take one more? y/n \n')

	def input(self, sentenses):
		return input(sentenses)

	def print(self, sentenses):
		print(sentenses, '\n')


class Player(PlayerCards, PlayerOperation):
	"""Class Player. Constructor takes the Player Name"""
	def __init__(self, name, *args):
		super(Player, self).__init__()
		self.name = name


class Table:
	"""docstring for Table"""
	raw = []

	def __init__(self):
		super(Table, self).__init__()

	def header(self):
		self.raw.append('Name            | Points ')
		self.raw.append('----------------|---------')

	def row(self, player):
		self.raw.append(player['name'] + '   | ' + str(player['points']))

	def footer(self):
		self.raw.append('--------------------------')		


class Engine:
	"""docstring for Engine"""
	players, deck = [], []
	results = []

	def __init__(self):
		super(Engine, self).__init__()
		print('Welcome to SuperDeck Game 21!')
		self.setting()

	def setting(self):
		# Generate Deck
		cards = [2, 3, 4, 6, 7, 8, 9, 10, 11]
		[self.deck.extend(cards) for c in range(0, 4)]

	def add_player(self, player):
		#if int(self.count_players) < len(self.players):
		self.players.append(player)

	def run(self):
		start = input('\nStart game? (y/n) \n')
		if start != 'y':
			return False

		for player in self.players:
			self.results.append(self.play(player))

		table = Table()
		table.header()
		for player in self.results:
			table.row(player)
		table.footer()
		table.raw.append(self.finish())

		for player in self.players:
			player.print('\n'.join(table.raw))

	def play(self, player):
		answer = 'y'
		while answer == 'y':
			# make pull of the card
			drop = random.choice(self.deck)
			self.deck.remove(drop)
			player.add_card(drop)

			player.print(player.name + ' got the card: ' + str(drop))

			totals = player.get_subtotal()
			player.print('Current points: ' + '/'.join([str(x) for x in totals]))

			answer = player.is_continue()

		final = False
		for temp in totals:
			if (final == False or (final < temp <= 21) or (temp < final > 21)):
				final = temp

		return {'name': player.name, 'points': final, 'cards': len(player.cards)}

	def finish(self):		
		# Depend winner
		winner = {'name': '', 'points': False, 'cards': 0}

		# sorting
		for player in self.results:
			if (winner['points'] == False
				or (winner['points'] < player['points'] <= 21)
				or (player['points'] < winner['points'] > 21)
				or (player['points'] == winner['points'] and player['cards'] < winner['cards'])
			   ):
				winner = player

		return 'Congratulations ' + winner['name'] + ' is win. With score ' + str(winner['points']) + ' points'


if __name__ == "__main__":
	game = Engine()
	game.add_player(Player('Player John'))
	game.add_player(Player('Player Asia'))
	game.run()