#coding: utf-8

def sliding_puzzle():
	board = create_init_board()
	goal = set_goal_board()
	opened = find_position(0,board)
	while True:
		print_board(board)
		if board == goal:
			print("Congratulations!")
			break
		num = get_number()
		if num == 0:
			break
		pos = find_position(num,board)
		(opened,board) = move(pos,opened,board)
	print("Please come again.")

def create_init_board():
	return [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]]

def set_goal_board():
	return [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

def get_number():
	temp = True
	while(temp):
		num = input("Type the number you want to move (Type 0 to quit)")
		if (num.isdigit() and (int(num) >= 0 and int(num) <= 15) ):
			temp = False
	print(num)
	return int(num)


def print_board(board):
	for i in board:
		count = 0
		for j in i:
			count = count + 1
			if(j == 0):
				print("  ",end="")
			else:
				print(str(j).rjust(2), end="")
			if not (count%4 == 0):
				print("  ", end="")

		print("")

def find_position(num,board):
	x_pos = 0
	for i in board:
		y_pos = 0
		for j in i:
			if(j == num):
				# print("("+str(x_pos)+", "+str(y_pos)+")")
				return (x_pos,y_pos)
			y_pos = y_pos + 1
		x_pos = x_pos + 1

def move(pos,opened,board):
	pos_num = position_num(pos,board)
	opened_num = position_num(opened,board)
	if(isright(pos,opened)):
		pos_num, opened_num = position_num(opened,board), position_num(pos,board)

		trasrate(pos,pos_num,board)
		trasrate(opened,opened_num,board)		

		return (find_position(0,board), board)

	else:
		print("Can't Move Try Again!")
		print("")
		return (opened, board)

def trasrate(pos, num, board):
	x_pos = 0
	for i in board:
		y_pos = 0
		for j in i:
			if(x_pos == pos[0] and y_pos == pos[1]):
				board[x_pos][y_pos] = num
			y_pos = y_pos + 1
		x_pos = x_pos + 1
	return board

def position_num(pos, board):
	x_pos = 0
	for i in board:
		y_pos = 0
		for j in i:
			if(x_pos == pos[0] and y_pos == pos[1]):
				return j
			y_pos = y_pos + 1
		x_pos = x_pos + 1



def isright(pos,opened):
	if( (pos[0] == (opened[0] - 1) and pos[1] == opened[1]) or
		(pos[0] == (opened[0] + 1) and pos[1] == opened[1]) or
		(pos[0] == opened[0] and pos[1] == (opened[1] - 1)) or
		(pos[0] == opened[0] and pos[1] == (opened[1] + 1)) ):
		return True
	else:
		return False


sliding_puzzle()