#coding: utf-8
import time

def countdown(count):
	if(count == 0):
		print("발사!")
	else:
		print(count)
		time.sleep(1)
		countdown(count - 1)


s = input("몇 초 카운트?")
countdown(int(s))