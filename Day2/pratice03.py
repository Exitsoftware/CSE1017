#coding: utf-8
# 동전합산 서비스 
# 가지고 있는 동전의 총액을 계산해주는 프로그램 
# 입력: 각 동전의 개수 
# 출력: 총액 
# 작성자: 도경구
# 작성일: 2014년 9월 1일 (version 0.3) 
# 사용자 입력받기 

cont = True
while Cont :
	coin500 = raw_input("500원짜리는 몇개 입니까?\n")
	if coin500.isdigit():
		cont = False
	else:
		print "다시 입력해주세요\n"

cont = True
while True:
	coin100 = raw_input("100원짜리는 몇개 입니까?\n") 
	if coin100.isdigit():
		break
	else:
		print "다시 입력해주세요\n"
		
while True:
	coin50 = raw_input("50원짜리는 몇개 입니까?\n") 
	if coin50.isdigit():
		break
	else:
		print "다시 입력해주세요\n"	

while True:
	coin10 = raw_input("10원짜리는 몇개 입니까?\n")
	if coin10.isdigit():
		break
	else:	
		print "다시 입력해주세요\n"	

# 계산 
total = 500 * int(coin500) + 100 * int(coin100) + 50 * int(coin50) + 10 * int(coin10)

# 결과 출력 
print "\n손님의 동전은 총", total, "원 입니다." 
print "저희 서비스를 이용해주셔서 감사합니다." 
print "또 들려주세요.\n"
