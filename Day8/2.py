#coding: utf-8

import random

def creat_board():
	seed = [1,2,3,4,5,6,7,8,9]
	random.shuffle(seed)
	row0 = seed[:]
	row1 = seed[3:6] + seed[6:] + seed[:3]
	row2 = seed[6:] + seed[:3] + seed[3:6]

	# seed.reverse()
	row3 = (seed[1:3] + [seed[0]]) + (seed[4:6] + [seed[3]]) + (seed[7:] + [seed[6]])
	row4 = row3[3:6] + row3[6:] + row3[:3]
	row5 = row3[6:] + row3[:3] + row3[3:6]

	# seed.reverse()

	row6 = (row3[1:3] + [row3[0]]) + (row3[4:6] + [row3[3]]) + (row3[7:] + [row3[6]])
	row7 = row6[3:6] + row6[6:] + row6[:3]
	row8 = row6[6:] + row6[:3] + row6[3:6]


	return [row0, row1, row2, row3, row4, row5, row6, row7, row8]

def shuffle_ribons(board):

	top, mid, bottom = board[:3], board[3:6], board[6:]

	# print(top[0])
	# print(top[1])
	# print(top[2])
	# print(top)
	# top = [top[0]] + [top[1]] + [top[2]]
	# print(top)
	# print(mid)
	# print(bottom)

	# top = [top[2]] + [top[1]] + [top[0]]
	# mid = [mid[2]] + [mid[1]] + [mid[0]]
	# bottom = [bottom[2]] + [bottom[1]] + [bottom[0]]

	# top = [top[1]] + [top[0]] + [top[2]]
	# mid = [mid[1]] + [mid[0]] + [mid[2]]
	# bottom = [bottom[1]] + [bottom[0]] + [bottom[2]]

	# top = [top[0]] + [top[2]] + [top[1]]
	# mid = [mid[0]] + [mid[2]] + [mid[1]]
	# bottom = [bottom[0]] + [bottom[2]] + [bottom[1]]

	random.shuffle(top)
	random.shuffle(mid)
	random.shuffle(bottom)
	board = top + mid + bottom
	return board

def transpose(board):
	transposed = []

	for i in range(len(board)):
		transposed.append([])
	for i in range(len(board)):
		for j in range(len(board)):
			transposed[i].append(board[j][i])

	return transposed

def creae_solution_board():
	return transpose(shuffle_ribons(transpose(shuffle_ribons(creat_board()))))

def get_level():
	level = input("난이도 (상,중,하) 중에서 하나를 선택해서 입력 : ")
	while level not in {"상", "중", "하"}:
		level = input("난이도 (상,중,하) 중에서 하나를 선택해서 입력 : ")

	if level == "하":
		return 40
	elif level == "중":
		return 34
	elif level == "상":
		return 28

def copy_board(board):
	board_clone = []
	for row in board:
		row_clone = row[:]
		board_clone.append(row_clone)
	return board_clone


def make_holes(board, no_of_holes):
	holeset = set()
	while no_of_holes > 0:
		i = random.randrange(0,9)
		j = random.randrange(0,9)
		if not board[i][j] == 0:
			board[i][j] = 0
			holeset.add((i,j))
			no_of_holes = no_of_holes - 1
		# print(no_of_holes)

	return board, holeset

def showboard(board):
	for i in range(len(board) + 1):
		if i == 0:
			print("+", end=" ")
		else:
			print(i - 1, end=" ")
			if(i == len(board)):
				print("")

	for i in range(len(board)):
		print(i, end=" ")
		for j in range(len(board[i])):
			if(board[i][j] == 0):
				print(".", end=" ")
			else:
				print(board[i][j], end=" ")

			if(j == (len(board[i]) - 1) ):
				print("")

def get_integer(text, min_num, max_num):
	num = input(text)
	while not (num.isdigit() and (int(num) >= min_num and int(num) <= max_num)):
		num = input(text)

	return int(num)

def sudok():
	solution = creae_solution_board()
	no_of_holes = get_level()
	puzzle = copy_board(solution)
	(puzzle, holeset) = make_holes(puzzle, no_of_holes)
	showboard(puzzle)
	print("")
	while True:
		i = get_integer("가로줄 번호 (0~8) : ", 0, 8)
		j = get_integer("세로줄 번호 (0~8) : ", 0, 8)

		if (i, j) not in holeset:
			print("빈칸이 아닙니다.")
			continue
		n = get_integer("숫자(1~9) : ", 1, 9)
		sol = solution[i][j]
		if n == sol:
			puzzle[i][j] = sol
			showboard(puzzle)
			print("")
			holeset.remove((i,j))
			no_of_holes -= 1
		else:
			print(n,"가 아닙니다. 다시 해보세요.")
		if no_of_holes == 0:
			print("잘 하셨습니다. 또 들리세요.")
			break

sudok()
