#coding:utf-8

import os
import random
import time

def create_board(board):
	for i in range(10):
		board.append([])
		for j in range(10):
			board[i].append(0)

	for i in range(10):
		board[0][i] = 9
		board[9][i] = 9
		board[i][0] = 9
		board[i][9] = 9

def show_board():
	os.system("clear")
	for i in range(len(board) - 1):
		if(i == 0):
			print("+", end = " ")
		else:
			print(i, end = " ")
	print("")
	for i in range(1, len(board) - 1):
		print(i, end = " ")
		for j in range(1, len(board[i]) - 1 ):
			if(board[i][j] == 0 and ((i + j) % 2 == 0)):
				print("□", end = " ")
			elif(board[i][j] == 0 and ((i + j) % 2 == 1)):
				print("■", end = " ")
			elif(board[i][j] == 1 or board[i][j] == 2):
				print("⊙", end = " ")
			else:
				print(board[i][j], end = " ")
		print("")

# def show_board():
# 	os.system("clear")
# 	for i in range(1,len(board)-1):
# 		for j in range(1,len(board[i])-1):
# 			if(board[i][j] == 0 and ((i + j) % 2 == 0)):
# 				print("□", end = " ")
# 			elif(board[i][j] == 0 and ((i + j) % 2 == 1)):
# 				print("■", end = " ")
# 			elif(board[i][j] == 1 or board[i][j] == 2):
# 				print("⊙", end = " ")
# 			else:
# 				print(board[i][j], end = " ")
# 		print("")

def board_setting():

	# computer Pone setting
	for i in range(1, len(board) - 1):
		board[2][i] = "♟"
	# computer Castle setting
	board[1][1], board[1][8] = "♜", "♜"
	# computer Night setting
	board[1][2], board[1][7] = "♞", "♞"
	# computer Bishop setting
	board[1][3], board[1][6] = "♝", "♝"
	# computer Queen setting
	board[1][4] = "♛"
	# computer King setting
	board[1][5] = "♚"

	# player Pone setting
	for i in range(1, len(board) - 1):
		board[7][i] = "♙"
	# player Castle setting
	board[8][1], board[8][8] = "♖", "♖"
	# player Night setting
	board[8][2], board[8][7] = "♘", "♘"
	# player Bishop setting
	board[8][3], board[8][6] = "♗", "♗"
	# player Queen setting
	board[8][4] = "♕"
	# player King setting
	board[8][5] = "♔"

def choose():
	temp = True
	while(temp):
		temp2 = True
		while(temp2):
			input_text = input("x좌표와 y좌표를 입력해주세요.")
			if(input_text.find(" ") != -1):					
				input_text = input_text.partition(" ")
				if(input_text[0].isdigit() and input_text[2].isdigit()):
					pos_x = int(input_text[0])
					pos_y = int(input_text[2])


					if(pos_x >= 0 and pos_x < 9 and pos_y >= 0 and pos_y < 9):
						temp2 = False
					else:
						print("좌표 값이 잘못되었습니다.")
			else:
				print("x좌표와 y좌표를 제대로 입력해 주세요.")


		if(board[pos_x][pos_y] == "♙"):
			select = "Pone"
			answer = input("선택하신 말은 폰 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_pone(pos_x, pos_y)
				temp = False
				
		elif(board[pos_x][pos_y] == "♖"):
			select = "Castle"

			answer = input("선택하신 말은 룩 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_castle(pos_x, pos_y)
				temp = False
			
		elif(board[pos_x][pos_y] == "♘"):
			select = "Night"
			answer = input("선택하신 말은 나이트 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_night(pos_x,pos_y)
				temp = False

		elif(board[pos_x][pos_y] == "♗"):
			select = "Bishop"
			answer = input("선택하신 말은 비숍 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_bishop(pos_x, pos_y)
				temp = False
		elif(board[pos_x][pos_y] == "♕"):
			select = "Queen"
			answer = input("선택하신 말은 퀸 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_queen(pos_x, pos_y)
				temp = False
		elif(board[pos_x][pos_y] == "♔"):
			select = "King"
			answer = input("선택하신 말은 킹 입니다 맞습니까? (Y/N)")
			if(answer == 'y' or answer == 'Y'):
				move_king(pos_x,pos_y)
				temp = False
		else:
			print("선택할 수 없습니다.")

	return select

def is_enemy(pos_x, pos_y):
	if(board[pos_x][pos_y] == "♚" or board[pos_x][pos_y] ==  "♛" or board[pos_x][pos_y] ==  "♜" or board[pos_x][pos_y] == "♝" or board[pos_x][pos_y] == "♞" or board[pos_x][pos_y] ==  "♟"):
		return True
	else:
		return False	

def is_player(pos_x, pos_y):
	if(board[pos_x][pos_y] == "♔" or board[pos_x][pos_y] ==  "♕" or board[pos_x][pos_y] ==  "♖" or board[pos_x][pos_y] == "♗" or board[pos_x][pos_y] == "♘" or board[pos_x][pos_y] ==  "♙"):
		return True
	else:
		return False	

def is_board_in(index_x, index_y):
	if(index_x >= 1 and index_x <= 8 and index_y >= 1 and index_y <= 8):
		return True
	else:
		return False

def move_pone(pos_x, pos_y):
	two_move = False
	front = 0
	double_front = 0

	front = board[pos_x - 1][pos_y]
	double_front = board[pos_x - 2][pos_y]
	left_temp_enemy = board[pos_x-1][pos_y-1]
	right_temp_enemy = board[pos_x-1][pos_y + 1]



	if(pos_x == 7):
		two_move = True
		# front = board[pos_x - 1][pos_y]
		# double_front = board[pos_x - 2][pos_y]
		if(board[pos_x - 1][pos_y] == 0):
			board[pos_x - 1][pos_y] = 1
		if(board[pos_x - 2][pos_y] == 0):
			board[pos_x - 2][pos_y] = 1

	elif(pos_x <= 6 and pos_x >= 2 and board[pos_x - 1][pos_y] == 0):
		# front = board[pos_x - 1][pos_y]
		board[pos_x - 1][pos_y] = 1

	# front = board[pos_x - 1][pos_y]

	if(is_enemy((pos_x - 1), (pos_y - 1)) or is_enemy((pos_x - 1), (pos_y + 1))):
		# print("!!")
		if(is_enemy((pos_x - 1), (pos_y - 1))):
			# left_temp_enemy = board[pos_x-1][pos_y-1]
			board[pos_x-1][pos_y-1] = 2

		if(is_enemy((pos_x - 1), (pos_y + 1))):
			# right_temp_enemy = board[pos_x-1][pos_y + 1]
			board[pos_x-1][pos_y + 1] = 2


	show_board()
	print("선택하신 말은 폰입니다.")
	# print(is_enemy(pos_x-1,pos_y-1))
	# print("Front",front)
	# print(board[pos_x-1][pos_y])

	temp = True
	while(temp):
		# attack = False
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])

			# if(pos_x == 6 and move_x == 4):
			# 	two_move = True

			# if(is_enemy((pos_x - 1), (pos_y -1))):
			# 	print("!!")
			# 	temp_enemy = board[pos_x-1][pos_y-1]
			# 	board[pos_x-1][pos_y-1] = 2


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					board[pos_x][pos_y] = 0
					board[pos_x - 1][pos_y] = front
					if(board[move_x][move_y] == 2):
						board[pos_x-1][pos_y-1] = left_temp_enemy
						board[pos_x-1][pos_y+1] = right_temp_enemy
					if(two_move):
						board[pos_x - 2][pos_y] = double_front

					board[move_x][move_y] = "♙"
					
					temp = False
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()
	
def move_castle(pos_x, pos_y):
	row = []
	col = []
	index_x = pos_x
	index_y = pos_y



	while(True):
		index_x -= 1
		if(board[index_x][pos_y] != 0):
			front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
			if(is_enemy(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1

	index_x = pos_x

	while(True):
		index_x += 1
		if(board[index_x][pos_y] != 0):
			back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
			if(is_enemy(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
				row.append(index_x)
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1
		

	index_y = pos_y

	while(True):
		index_y -= 1
		if(board[pos_x][index_y] != 0):
			left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_enemy(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])
			col.append(index_y)
			board[pos_x][index_y] = 1
		
	# print("loop?")
	index_y = pos_y

	while(True):
		index_y += 1
		if(board[pos_x][index_y] != 0):
			right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_enemy(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])	
			col.append(index_y)
			board[pos_x][index_y] = 1
		
	show_board()
	print("선택하신 말은 룩입니다.")
	temp = True
	while(temp):
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					for i in row:
						board[i][pos_y] = 0
					for i in col:
						board[pos_x][i] = 0

					board[front_enemy[1]][front_enemy[2]] = front_enemy[0]
					board[back_enemy[1]][back_enemy[2]] = back_enemy[0]
					board[left_enemy[1]][left_enemy[2]] = left_enemy[0]
					board[right_enemy[1]][right_enemy[2]] = right_enemy[0]



					board[pos_x][pos_y] = 0
					# board[pos_x - 1][pos_y] = front

					board[move_x][move_y] = "♖"
					
					temp = False
				# else:
				# 	print("x좌표와 y좌표를 제대로 입력해 주세요.")
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()

def move_night(pos_x, pos_y):

	enemy = []
	check_position =[[pos_x-2, pos_y-1], [pos_x - 2, pos_y + 1], [pos_x-1, pos_y -2], [pos_x-1, pos_y+2], [pos_x+1, pos_y-2], [pos_x+1, pos_y+2], [pos_x+2, pos_y-1], [pos_x+2, pos_y+1]]

	for i in range(8):
		enemy.append([])


	for i in range(8):
		if(is_board_in(check_position[i][0], check_position[i][1])):
			enemy[i].append(board[check_position[i][0]][check_position[i][1]])
			if(board[check_position[i][0]][check_position[i][1]] == 0):
				board[check_position[i][0]][check_position[i][1]] = 1
			elif (is_enemy(check_position[i][0], check_position[i][1])):
				board[check_position[i][0]][check_position[i][1]] = 2

	show_board()
	print("선택하신 말은 나이트입니다.")
	temp = True
	while(temp):
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					

					for i in range(8):
						if(is_board_in(check_position[i][0], check_position[i][1])):
							board[check_position[i][0]][check_position[i][1]] = enemy[i][0]


					board[pos_x][pos_y] = 0

					board[move_x][move_y] = "♘"
					
					temp = False
				else:
					print("x좌표와 y좌표를 제대로 입력해 주세요.")
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()

def move_bishop(pos_x, pos_y):

	enemy = []
	position = []

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	show_board()
	print("선택하신 말은 비숍입니다.")
	temp = True
	while(temp):
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					

					for i in range(len(position)):
						board[position[i][0]][position[i][1]] = 0

					for i in range(len(enemy)):
						if(is_board_in(enemy[i][1], enemy[i][2])):
							board[enemy[i][1]][enemy[i][2]] = enemy[i][0]


					board[pos_x][pos_y] = 0

					board[move_x][move_y] = "♗"
					
					temp = False
				else:
					print("x좌표와 y좌표를 제대로 입력해 주세요.")
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()

def move_queen(pos_x, pos_y):

	enemy = []
	position = []

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_enemy(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1


	row = []
	col = []


	index_x = pos_x
	index_y = pos_y



	while(True):
		index_x -= 1
		if(board[index_x][pos_y] != 0):
			front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
			if(is_enemy(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1

	index_x = pos_x

	while(True):
		index_x += 1
		if(board[index_x][pos_y] != 0):
			back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
			if(is_enemy(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
				row.append(index_x)
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1
		

	index_y = pos_y

	while(True):
		index_y -= 1
		if(board[pos_x][index_y] != 0):
			left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_enemy(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])
			col.append(index_y)
			board[pos_x][index_y] = 1
		
	# print("loop?")
	index_y = pos_y

	while(True):
		index_y += 1
		if(board[pos_x][index_y] != 0):
			right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_enemy(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])	
			col.append(index_y)
			board[pos_x][index_y] = 1

	show_board()
	print("선택하신 말은 퀸입니다.")
	temp = True
	while(temp):
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					

					for i in range(len(position)):
						board[position[i][0]][position[i][1]] = 0

					for i in range(len(enemy)):
						if(is_board_in(enemy[i][1], enemy[i][2])):
							board[enemy[i][1]][enemy[i][2]] = enemy[i][0]

					for i in row:
						board[i][pos_y] = 0
					for i in col:
						board[pos_x][i] = 0

					board[front_enemy[1]][front_enemy[2]] = front_enemy[0]
					board[back_enemy[1]][back_enemy[2]] = back_enemy[0]
					board[left_enemy[1]][left_enemy[2]] = left_enemy[0]
					board[right_enemy[1]][right_enemy[2]] = right_enemy[0]

					board[pos_x][pos_y] = 0

					board[move_x][move_y] = "♕"
					
					temp = False
				else:
					print("x좌표와 y좌표를 제대로 입력해 주세요.")
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()

def move_king(pos_x, pos_y):

	enemy = []

	# for i in range(3):
	# 	enemy.append([])

	for i in range(pos_x-1, pos_x+2):
		for j in range(pos_y-1, pos_y+2):
			if(is_board_in(i, j)):
				if(board[i][j] == 0):
					board[i][j] = 1
				elif(is_enemy(i,j)):
					enemy.append([board[i][j], i, j])
					board[i][j] = 2
				# else:
				# 	board[i][j] = 1

	print("선택하신 말은 킹입니다.")
	show_board()
	temp = True
	while(temp):
		input_text = input("이동하실 x좌표와 y좌표를 입력해주세요.")
		if(input_text.find(" ") != -1):					
			input_text = input_text.partition(" ")
			if(input_text[0].isdigit() and input_text[2].isdigit()):
				move_x = int(input_text[0])
				move_y = int(input_text[2])


				if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
					

					for i in range(pos_x-1, pos_x+2):
						for j in range(pos_y-1, pos_y+2):
							if(board[i][j] == 1):
								board[i][j] = 0

					for i in range(len(enemy)):
						if(is_board_in(enemy[i][1], enemy[i][2])):
							board[enemy[i][1]][enemy[i][2]] = enemy[i][0]


					board[pos_x][pos_y] = 0

					board[move_x][move_y] = "♔"
					
					temp = False
				else:
					print("x좌표와 y좌표를 제대로 입력해 주세요.")
			else:
				print("좌표 값이 잘못되었습니다.")
		else:
			print("x좌표와 y좌표를 제대로 입력해 주세요.")

	show_board()

def computer_choose():
	print("컴퓨터가 생각 중입니다.")
	time.sleep(0.2)
	show_board()
	print("컴퓨터가 생각 중입니다..")
	time.sleep(0.2)
	show_board()
	print("컴퓨터가 생각 중입니다...")
	time.sleep(0.2)
	show_board()
	print("컴퓨터가 생각 중입니다....")
	time.sleep(0.2)
	show_board()
	print("컴퓨터가 생각 중입니다.....")
	time.sleep(0.6)
	li = [1, 2, 3, 4, 5, 6]
	temp = True
	while(temp):
		# li = [1, 2, 3]
		choice = random.choice(li)
		print("choice",choice)
		if(choice == 1):
			pos_x , pos_y = search_pone()
			if(pos_x == 9 and pos_y == 9):
				li.remove(1)
			else:
				while(True):
					if(computer_pone(pos_x, pos_y)):
						# print("컴퓨터가 폰을 움직였습니다.")
						temp = False
					break
			# break
		elif(choice == 2):
			pos_x , pos_y = search_night()
			if(pos_x == 9 and pos_y == 9):
				li.remove(2)
			else:
				while(True):
					if(computer_night(pos_x, pos_y)):
						# print("컴퓨터가 나이트를 움직였습니다.")
						temp = False
					break
		elif(choice == 3):
			pos_x , pos_y = search_bishop()
			if(pos_x == 9 and pos_y == 9):
				li.remove(3)
			else:
				while(True):
					if(computer_bishop(pos_x, pos_y)):
						# print("컴퓨터가 비숍을 움직였습니다.")
						temp = False
					break
			# break
		elif(choice == 4):
			pos_x , pos_y = search_castle()
			if(pos_x == 9 and pos_y == 9):
				li.remove(4)
			else:
				while(True):
					if(computer_castle(pos_x, pos_y)):
						# print("컴퓨터가 룩을 움직였습니다.")
						temp = False
					break

		elif(choice == 5):
			pos_x , pos_y = search_queen()
			if(pos_x == 9 and pos_y == 9):
				li.remove(5)
			else:
				while(True):
					if(computer_queen(pos_x, pos_y)):
						# print("컴퓨터가 퀸을 움직였습니다.")
						temp = False
					break
		elif(choice == 6):
			pos_x , pos_y = search_king()
			if(pos_x == 9 and pos_y == 9):
				# gameover = True
				li.remove(6)
			else:
				while(True):
					if(computer_king(pos_x, pos_y)):
						# print("컴퓨터가 킹을 움직였습니다.")
						temp = False
					break

def search_pone():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♟"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def search_night():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♞"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def search_bishop():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♝"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def search_castle():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♜"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def search_queen():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♛"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def search_king():
	position = []
	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == "♚"):
				position.append([i,j])

	if(position == []):
		return 9, 9

	return random.choice(position)

def computer_pone(pos_x, pos_y):

	rand_position = []

	left_unit = board[pos_x + 1][pos_y - 1]
	right_unit = board[pos_x + 1][pos_y + 1]


	if(pos_x == 2):
		if(board[pos_x + 1][pos_y] == 0):
			board[pos_x + 1][pos_y] = 1
		if(board[pos_x + 2][pos_y] == 0):
			board[pos_x + 2][pos_y] = 1

		if(is_board_in(pos_x + 1, pos_y - 1) and is_player(pos_x + 1, pos_y - 1)):
			board[pos_x + 1][pos_y - 1] = 2
		if(is_board_in(pos_x + 1, pos_y + 1) and is_player(pos_x + 1, pos_y + 1)):
			board[pos_x + 1][pos_y + 1] = 2

	else:
		if(board[pos_x + 1][pos_y] == 0):
			board[pos_x + 1][pos_y] = 1
		if(is_board_in(pos_x + 1, pos_y - 1) and is_player(pos_x + 1, pos_y - 1)):
			board[pos_x + 1][pos_y - 1] = 2
		if(is_board_in(pos_x + 1, pos_y + 1) and is_player(pos_x + 1, pos_y + 1)):
			board[pos_x + 1][pos_y + 1] = 2

	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				board[i][j] = 0
				rand_position.append([i,j])

	board[pos_x + 1][pos_y - 1] = left_unit
	board[pos_x + 1][pos_y + 1] = right_unit


	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]


	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♟"



	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♟을",str(move_x)+",",move_y,"로 움직였습니다.")

	return True

def computer_night(pos_x, pos_y):

	enemy = []
	check_position =[[pos_x-2, pos_y-1], [pos_x - 2, pos_y + 1], [pos_x-1, pos_y -2], [pos_x-1, pos_y+2], [pos_x+1, pos_y-2], [pos_x+1, pos_y+2], [pos_x+2, pos_y-1], [pos_x+2, pos_y+1]]
	rand_position = []
	for i in range(8):
		enemy.append([])


	for i in range(8):
		if(is_board_in(check_position[i][0], check_position[i][1])):
			enemy[i].append(board[check_position[i][0]][check_position[i][1]])
			if(board[check_position[i][0]][check_position[i][1]] == 0):
				board[check_position[i][0]][check_position[i][1]] = 1
			elif (is_player(check_position[i][0], check_position[i][1])):
				board[check_position[i][0]][check_position[i][1]] = 2

	show_board()
	# temp = True

	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				rand_position.append([i,j])


	for i in range(8):
		if(is_board_in(check_position[i][0], check_position[i][1])):
			board[check_position[i][0]][check_position[i][1]] = enemy[i][0]

	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]

	# for i in range(8):
	# 	if(is_board_in(check_position[i][0], check_position[i][1])):
	# 		board[check_position[i][0]][check_position[i][1]] = enemy[i][0]


	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♞"

	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♞을",str(move_x)+",",move_y,"로 움직였습니다.")

	return True

def computer_bishop(pos_x, pos_y):
	rand_position = []

	enemy = []
	position = []

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1


	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				rand_position.append([i,j])


	for i in range(len(position)):
		board[position[i][0]][position[i][1]] = 0

	for i in range(len(enemy)):
		if(is_board_in(enemy[i][1], enemy[i][2])):
			board[enemy[i][1]][enemy[i][2]] = enemy[i][0]


	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]

	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♝"

	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♝을",str(move_x)+",",move_y,"로 움직였습니다.")


	return True

def computer_castle(pos_x, pos_y):
	rand_position = []

	row = []
	col = []
	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		if(board[index_x][pos_y] != 0):
			front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
			if(is_player(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1

	index_x = pos_x

	while(True):
		index_x += 1
		if(board[index_x][pos_y] != 0):
			back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
			if(is_player(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
				row.append(index_x)
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1
		

	index_y = pos_y

	while(True):
		index_y -= 1
		if(board[pos_x][index_y] != 0):
			left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_player(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])
			col.append(index_y)
			board[pos_x][index_y] = 1
		
	# print("loop?")
	index_y = pos_y

	while(True):
		index_y += 1
		if(board[pos_x][index_y] != 0):
			right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_player(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])	
			col.append(index_y)
			board[pos_x][index_y] = 1

	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				rand_position.append([i,j])
	
	# if(board[move_x][move_y] == 1 or board[move_x][move_y] == 2):
	for i in row:
		board[i][pos_y] = 0
	for i in col:
		board[pos_x][i] = 0

	board[front_enemy[1]][front_enemy[2]] = front_enemy[0]
	board[back_enemy[1]][back_enemy[2]] = back_enemy[0]
	board[left_enemy[1]][left_enemy[2]] = left_enemy[0]
	board[right_enemy[1]][right_enemy[2]] = right_enemy[0]

	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]

	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♜"	

	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♜을",str(move_x)+",",move_y,"로 움직였습니다.")


	return True

def computer_queen(pos_x, pos_y):

	rand_position = []

	enemy = []
	position = []

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x -= 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y += 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1

	index_x = pos_x
	index_y = pos_y

	while(True):
		index_x += 1
		index_y -= 1

		if(board[index_x][index_y] != 0):
			if(is_player(index_x, index_y)):
				enemy.append([board[index_x][index_y], index_x, index_y])
				board[index_x][index_y] = 2
			break
		else:
			position.append([index_x, index_y])
			board[index_x][index_y] = 1


	row = []
	col = []


	index_x = pos_x
	index_y = pos_y



	while(True):
		index_x -= 1
		if(board[index_x][pos_y] != 0):
			front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
			if(is_player(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# front_enemy = [ (board[index_x][pos_y]) , index_x, pos_y]
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1

	index_x = pos_x

	while(True):
		index_x += 1
		if(board[index_x][pos_y] != 0):
			back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
			if(is_player(index_x, pos_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# back_enemy = [ (board[index_x][pos_y]), index_x, pos_y]
				row.append(index_x)
				board[index_x][pos_y] = 2
			break
		else:
			# row.append(board[index_x][index_y])
			row.append(index_x)
			board[index_x][pos_y] = 1
		

	index_y = pos_y

	while(True):
		index_y -= 1
		if(board[pos_x][index_y] != 0):
			left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_player(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# left_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])
			col.append(index_y)
			board[pos_x][index_y] = 1
		
	# print("loop?")
	index_y = pos_y

	while(True):
		index_y += 1
		if(board[pos_x][index_y] != 0):
			right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
			if(is_player(pos_x, index_y)):
				# 적의 값, 적의 x좌표, 적의 y좌표
				# right_enemy = [(board[pos_x][index_y]), pos_x, index_y]
				col.append(index_y)
				board[pos_x][index_y] = 2
			break
		else:
			# col.append(board[index_x][index_y])	
			col.append(index_y)
			board[pos_x][index_y] = 1

	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				rand_position.append([i,j])

	for i in range(len(position)):
		board[position[i][0]][position[i][1]] = 0

	for i in range(len(enemy)):
		if(is_board_in(enemy[i][1], enemy[i][2])):
			board[enemy[i][1]][enemy[i][2]] = enemy[i][0]

	for i in row:
		board[i][pos_y] = 0
	for i in col:
		board[pos_x][i] = 0

	board[front_enemy[1]][front_enemy[2]] = front_enemy[0]
	board[back_enemy[1]][back_enemy[2]] = back_enemy[0]
	board[left_enemy[1]][left_enemy[2]] = left_enemy[0]
	board[right_enemy[1]][right_enemy[2]] = right_enemy[0]

	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]

	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♛"	

	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♛을",str(move_x)+",",move_y,"로 움직였습니다.")


	return True

def computer_king(pos_x, pos_y):
	rand_position = []
	enemy = []

	# for i in range(3):
	# 	enemy.append([])

	for i in range(pos_x-1, pos_x+2):
		for j in range(pos_y-1, pos_y+2):
			if(is_board_in(i, j)):
				if(board[i][j] == 0):
					board[i][j] = 1
				elif(is_player(i,j)):
					enemy.append([board[i][j], i, j])
					board[i][j] = 2
				# else:
				# 	board[i][j] = 1


	for i in range(1, len(board)-1):
		for j in range(1, len(board)-1):
			if(board[i][j] == 1 or board[i][j] == 2):
				rand_position.append([i,j])


	for i in range(pos_x-1, pos_x+2):
		for j in range(pos_y-1, pos_y+2):
			if(board[i][j] == 1):
				board[i][j] = 0

	for i in range(len(enemy)):
		if(is_board_in(enemy[i][1], enemy[i][2])):
			board[enemy[i][1]][enemy[i][2]] = enemy[i][0]


	if (rand_position == []):
		return False

	choice_num = random.choice(rand_position)
	move_x = choice_num[0]
	move_y = choice_num[1]

	board[pos_x][pos_y] = 0

	board[move_x][move_y] = "♚"	

	show_board()
	print("컴퓨터가",str(pos_x)+",",pos_y,"에 있던 ♚을",str(move_x)+",",move_y,"로 움직였습니다.")


	return True


board = []
gameover = False
create_board(board)
board_setting()
show_board()
while(True):
	choose()
	king_x, king_y = search_king()
	if(king_x == 9 and king_y == 9):
		print("You Win!")
		break
	computer_choose()

