#coding: utf-8

import random

def creat_board():
	seed = [1,2,3,4]
	random.shuffle(seed)
	row0 = seed[:]
	row1 = seed[2:] + seed[:2]
	seed.reverse()
	row2 = seed[2:] + seed[:2]
	row3 = seed[:]
	seed.reverse()
	return [row0, row1, row2, row3]

def shuffle_ribons(board):
	top, bottom = board[:2], board[2:]
	random.shuffle(top)
	random.shuffle(bottom)
	board = top + bottom
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
		return 6
	elif level == "중":
		return 8
	elif level == "상":
		return 10

def copy_board(board):
	board_clone = []
	for row in board:
		row_clone = row[:]
		board_clone.append(row_clone)
	return board_clone


def make_holes(board, no_of_holes):
	holeset = set()
	while no_of_holes > 0:
		i = random.randrange(0,4)
		j = random.randrange(0,4)
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

def sudokumini():
	solution = creae_solution_board()
	no_of_holes = get_level()
	puzzle = copy_board(solution)
	(puzzle, holeset) = make_holes(puzzle, no_of_holes)
	# print(holeset)
	showboard(puzzle)
	while True:
		i = get_integer("가로줄 번호 (0~3) : ", 0, 3)
		j = get_integer("세로줄 번호 (0~3) : ", 0, 3)
		# print((i,j))
		if (i, j) not in holeset:
			print("빈칸이 아닙니다.")
			continue
		n = get_integer("숫자(1~4) : ", 1, 4)
		sol = solution[i][j]
		if n == sol:
			puzzle[i][j] = sol
			showboard(puzzle)
			holeset.remove((i,j))
			no_of_holes -= 1
		else:
			print(n,"가 아닙니다. 다시 해보세요.")
		if no_of_holes == 0:
			print("잘 하셨습니다. 또 들리세요.")
			break




sudokumini()
