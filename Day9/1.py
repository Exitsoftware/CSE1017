#coding: utf-8
import random

def play_blackjack():
	print("Welcome to SMaSH Casino")

	deck = fresh_deck()
	chips = 0
	temp = True
	while(temp):
		print("------------------------")
		dealer = []
		player = []

		card, deck = hit(deck)
		player.append(card)
		card, deck = hit(deck)
		dealer.append(card)
		card, deck = hit(deck)
		player.append(card)
		card, deck = hit(deck)
		dealer.append(card)

		print("My cards are:")
		print(" ", "****", "**")
		print(" ", dealer[1]["suit"], dealer[1]["rank"])

		show_card(player, "Your cards are:")

		score_player = count_score(player)
		score_dealer = count_score(dealer)

		if(score_player == 21):
			chips += 2
			print("Blackjack! You won!")

		else:
			while (score_player < 21 and more("Hit? (y/n)")):
				card, deck = hit(deck)
				print(" ", card["suit"], card["rank"])
				player.append(card)
				score_player = count_score(player)


			if(score_player > 21):
				show_card(dealer, "My cards are:")
				print("You bust! I won.")
				chips -= 1
			else:
				while(score_dealer <= 16):
					card, deck = hit(deck)
					dealer.append(card)
					score_dealer = count_score(dealer)

				if(score_dealer > 21):
					show_card(dealer, "My cards are:")
					print("I bust! You won.")
					chips += 1
				elif(score_player == score_dealer):
					show_card(dealer, "My cards are:")
					print("We Draw.")
				elif(score_player > score_dealer):
					show_card(dealer, "My cards are:")
					print("You won!")
					chips += 1
				else:
					show_card(dealer, "My cards are:")
					print("I won!")
					chips -= 1

			print("chips =", chips)
			if (more("Play more? (y/n)")):
				temp = True
			else:
				temp = False








def fresh_deck():
	suits = {"Spade", "Hearts", "Diamond", "Club"}
	ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
	deck = []

	for i in suits:
		for j in ranks:
			deck.append({"suit":i, "rank":j})

	
	random.shuffle(deck)
	return deck

def hit(deck):
	if deck == []:
		deck = fresh_deck()
	return deck[0], deck[1:]

def count_score(cards):
	score = 0
	# is_a = False;
	a_count = 0;
	for card in cards:
		if(str(card["rank"]).isdigit()):
			score += card["rank"]
		elif(card["rank"] == "A"):
			score += 11
			a_count += 1
			# is_a = True
		else:
			score += 10

	if score > 21 and a_count != 0 :
		while(a_count != 0):
			score -= 10
			a_count -= 1

	return score

def show_card(cards, message):
	print(message)
	for card in cards:
		print(" ", card["suit"], card["rank"])

def more(message):
	answer = input(message)
	while not (answer == 'y' or answer == 'n'):
		answer = input(message)

	return answer == 'y'



play_blackjack();




