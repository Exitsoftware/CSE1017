#coding: utf-8
# 대출 상환금 계산 서비스 
# 대출금 상환금액을 계산해주는 프로그램 
# 
# 입력: 원금(principal) - 백만이상 정수만 허용 
#       상환기간(years) - 1이상정수만 허용 
#       연이자율(interest rate) - 0.0에서 100.00 사이의 부동소수점수 만 허용 
# 출력: 연상환금액, 월상환금액, 상환금액의 총계 
# 
# 작성자: 홍길동 
# 작성날짜: 2014년 9월 6일 (version 1.0) 
# 입력과 입력확인 

print "대출 상환금 계산 서비스에 오심을 환영합니다." 

# 상환금 계산 
cont = True
while cont:
	p = raw_input("대출원금이 얼마인가요 (백만이상)")
	if p.isdigit() and int(p) >= 1000000:
		p = int(p)
		cont = False
	else:
		print "백만원 이상 숫자로만 입력해주세요."

cont = True
while cont:
	y = raw_input("상환기간을 입력해주세요. (1년 단위)")
	if y.isdigit() and int(y) >= 1:
		y = int(y)
		cont = False
	else:
		print "1년 이상 연단위로 숫자로만 적어주세요"

cont = True
while cont:
	r = raw_input("이쟈율은 몇 % 인가요? (0~100)")
	part = r.partition(".")

	if (part[0].isdigit() or part[2].isdigit()) and float(part[0]) >= 0 and float(part[0]) <= 100 :

		print part[2].isdigit()

		if (part[2].isdigit() and part[1] == '.') or part[1] == '.':
			r = float(r) / 100
			cont = False
		else:
			print "틀림!!"

		# if part[2] == None:
		# 	r = float(r) / 100
		# 	cont = False
		# else:
		# 	print "이자율은 0 ~ 100 사이로 입력하세요."

	# elif part[2].isdigit() == False:
	# 	print "이자율은 0 ~ 100 사이로 입력하세요."

	else:
		print "이자율은 0 ~ 100 사이로 입력하세요."


d = (((1 + r) ** y) * p * r) / (((1 + r) ** y) - 1)




# 계산 출력

print "\n\n대출 상환금 내역을 알려드리겠습니다."
print "대출원금 : " + str(p) + " 원"
print "연 이자율 " + str(r * 100) + "%로 " + str(y) + "년 동안 상환"
print "1년에 한번씩 상환하시면 매년" + str(int(d)) + " 원씩 지불하셔야 합니다. "
print "1에 한번씩 상환하시면 매년" + str(int(d / 12)) + " 원씩 지불하셔야 합니다. "
print "상환 완료시까지 총 상환금액은" + str(int(d * y)) + " 원 입니다. "

# 출력 
print ""
print "저희 서비스를 이용해주셔서 감사합니다." 
print "또 들려주세요."