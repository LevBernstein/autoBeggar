def penalty_value_of(card):
	values = {"J": 1 ,"Q": 2, "K": 3, "A": 4}
	return values[card]

def play(hands):
	a, b = hands
	word = a + b
	if word.count("J") != 4 or word.count("Q") != 4 or word.count("K") != 4 or word.count("A") != 4 or word.count("-") != 36:
		return hands, -1, -1
	stack = ""
	turns = 0
	tricks = 0
	player = 1
	while a != "" and b != "":
		battle_in_progress = False
		cards_to_play = 1
		while cards_to_play > 0:
			try:
				if player == 1:
					next_card = a[0]
					a = a[1:]
				else:
					next_card = b[0]
					b = b[1:]
			except IndexError:
				break
			
			turns += 1
			stack += next_card

			if next_card == "-":
				if battle_in_progress:
					cards_to_play -= 1
				else:
					player *= -1
			else:
				battle_in_progress = True
				cards_to_play = penalty_value_of(next_card)
				player *= -1

		tricks += 1
		if player == 1:
			b += stack
		else:
			a += stack
		stack = ""

		player *= -1

	return hands, turns, tricks
