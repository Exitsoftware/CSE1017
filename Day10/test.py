# def load_members():
# 		file = open("members.txt", "r")
# 		members = {}
# 		for line in file:
# 			name, passwd, tries, wins, chips = line.strip('\n').split(',')
# 			print("F")
# 			members[name] = (passwd, int(tries), float(wins), int(chips))
# 		file.close()
# 		return members

# def store_members(members):
# 	file = open("members.txt","w")
# 	names = members.keys()
# 	print(names)
# 	for name in names:
# 		passwd, tries, wins, chips = members[name]
# 		line = name + ',' + passwd + ',' + str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'

# 		file.write(line)
# 	file.close()

# members = load_members()
# store_members(members)
# username = "doh"
# keys = members.keys()
# print(username in members.keys())


a= 0.24644433
print("{0:.2f}".format(rate))
print(a)