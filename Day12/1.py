def reverse(xs):
	for i in range(len(xs)//2):
		xs[i], xs[len(xs)-1-i] = xs[len(xs)-1-i], xs[i]
	return xs

def deep_reverse(xs):
	xs = reverse(xs)
	for i in xs:
		if(is_list(i)):
			i = deep_reverse(i)
	return xs

def symmetric_square_matrix(board):
	sw = True
	for i in range(len(board)):
		for j in range(len(board[i])):
			if(board[i][j] != board[j][i]):
				sw = False
	return sw

def list_product(xs):
	result = 1
	for i in xs:
		result = result * i
	return result

def greatest(xs):
	max_num = xs[0]
	for i in xs:
		if max_num < i:
			max_num = i
	return max_num

	# result = sorted(xs)
	# result.reverse()
	# return result[0]

def is_list(xs):
	return isinstance(xs, list)

def sudok_check(board):
	sw = True
	for i in board:
		for j in range(len(board)):
			if(i.count(j+1) != 1):
				sw = False
	board = change(board)

	for i in board:
		for j in range(len(board)):
			if(i.count(j+1) != 1):
				sw = False

	board = change(board)

	return sw	

def change(board):
	changed = [[],[],[],[]]
	for i in range(len(board)):
		for j in range(len(board[i])):
			changed[j].append(board[i][j])
	return changed



def longest_repetition(xs):
	storage = []
	temp = []
	if xs == []:
		return None

	for i in xs:
		if (len(temp) == 0 or temp[0] == i):
			temp.append(i)
		else:
			storage.append(temp)
			temp = []
			temp.append(i)

	storage.append(temp)
	long_len = 0
	temp_num = 0
	for i in range(len(storage)):
		if long_len < len(storage[i]):
			long_len = len(storage[i])
			temp_num = i

	return (storage[temp_num][0], long_len)

def freq_analysis(xs):
	storage = []
	temp = []
	freq = {}
	if xs == []:
		return freq

	for i in xs:
		if (len(temp) == 0 or temp[0] == i):
			temp.append(i)
		else:
			storage.append(temp)
			temp = []
			temp.append(i)

	storage.append(temp)

	for i in storage:
		freq[str(i[0])] = int((100/len(xs))*xs.count(i[0]))

	return freq



def deep_count(xs):
	count = 0
	count = len(xs)
	for i in xs:
		if(is_list(i)):
			count += deep_count(i)
	return count




sudok = [[1,2,3,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]
xs1 = [1,[2,3,[4,[5,6]]]]
xs2 = [5,5,4,4,4,4,4,2,2,2,2,7,8,4,4,3,3,3]
xs3 = [1,2,3,4,5]
board = [[1,9,5,11],[9,4,7,3],[5,7,-7,8],[11,3,4,4]]
print("딥리버스",deep_reverse(xs1))
print("정방행렬",symmetric_square_matrix(board))
print("수도쿠",sudok_check(sudok))
print("리스트 곱셈",list_product([3,5,2,8]))
print("가장 큰 수",greatest([5,2,3,6,4,3,7,5,8,2]))
print("가장 큰 반복수",longest_repetition([2,2,2]))
print("빈도수",freq_analysis(xs2))
print("딥카운트",deep_count(([1,[2,3,[4,5]]])))

