#coding: utf-8
import random

def play_blackjack():
	print("Welcome to SMaSH Casino")

	username, passwd, tries, wins, chips, members = login(load_members())

	deck = fresh_deck()
	# chips = 0
	temp = True
	while(temp):
		tries += 1
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
			wins += 1
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
					wins += 1
				elif(score_player == score_dealer):
					show_card(dealer, "My cards are:")
					print("We Draw.")
				elif(score_player > score_dealer):
					show_card(dealer, "My cards are:")
					print("You won!")
					chips += 1
					wins +=1
				else:
					show_card(dealer, "My cards are:")
					print("I won!")
					chips -= 1

			print("chips =", chips)
			if (more("Play more? (y/n)")):
				temp = True
			else:
				# members[username][1].replace(tries)
				# members[username][2].replace(wins)
				# members[username][3].replace(chips)
				members[username] = (passwd, tries, wins, chips)
				store_members(tries, wins, chips, members)
				# print("Your played",members[username][1],"games and won",members[username][2],"of them.")
				print("Your played",tries,"games and won",int(wins),"of them.")
				rate = (divide(wins,tries)) * 100
				print("Your winning percentage today is","{0:.2f}".format(rate),"%")
				# print(chips)
				# print(members[username][3])

				show_top5(members)

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

def load_members():
		file = open("members.txt", "r")
		members = {}
		for line in file:
			name, passwd, tries, wins, chips = line.strip('\n').split(',')
			members[name] = (passwd, int(tries), float(wins), int(chips))

		file.close()
		return members

def store_members(co_tries, co_wins, co_chips, members):
	file = open("members.txt","w")
	names = members.keys()
	for name in names:
		passwd, tries, wins, chips = members[name]
		# tries = co_tries
		# wins = co_wins
		# chips = co_chips
		line = name + ',' + passwd + ',' + str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'

		file.write(line)
	file.close()

def login(members):

	username = input("Enter your name : (4 letters max)")
	while len(username) > 4:
		username = input("Enter your name : (4 letters max)")
	trypasswd = input("Enter your password : ")


	if(username in members.keys() ):
		while(members[username][0] != trypasswd):
			trypasswd = input("Enter your password : ")

		print("Your played",members[username][1],"games and won",int(members[username][2]),"of them.")
		rate = (divide(members[username][2],members[username][1])) * 100
		print("Your all-time winning percentage is","{0:.2f}".format(rate),"%")
		print("You have",members[username][3],"chips")

		return username, members[username][0], members[username][1], members[username][2], members[username][3], members

	else:
		members[username] = (trypasswd, 0, 0, 0)
		return username, trypasswd, 0, 0, 0, members


def divide(x, y):
	if(y > 0):
		return x / y
	else:
		return 0


def show_top5(members):
	print("all-time Top 5 based on the number of chips earned")
	s_list = sorted(members.items(), key=lambda x: x[1][3], reverse=True)

	if(len(s_list) < 5):
		for i in range(len(s_list)):
				if(s_list[i][1][3] > 0):
					print(i+1,".",s_list[i][0])
	else:
		for i in range(5):
			if(s_list[i][1][3] > 0):
				print(i+1,".",s_list[i][0])







play_blackjack();




