#!usr/bin/python#coding=utf-8
#二分查找
#执行方式: python BinarySearch.py tinyW.txt < tinyT.txt


import sys

sys.path.append(r"../class/")

import StdIn

def BinarySearch(whileList,keyIn):
	print("Binary Search Function")
	#必须是升序序列才能使用二分查找
	whileList.sort()
	print(whileListIn)
	print("keyIn={}".format(keyIn)) 

	lo=0
	hi=len(whileList)-1
	while lo <= hi :
		mid =lo + (hi-lo)//2

		if whileList[mid] == keyIn:
			return mid
		elif whileList[mid] < keyIn:
			lo = mid+1		
		else:
			hi = mid-1 


	else:
		return -1





        
if __name__ == '__main__':

	print("Task excute start...")
	keyIn=0
	whileListIn = StdIn.readInt(sys.argv[1])
	while True:
		try:
			keyIn=int(input())
			result = BinarySearch(whileListIn,keyIn)
			if result != -1:
				print("keyIn found! result = ",result)
			else:	
				print("keyIn not found!")
		except EOFError:
			print("Task excute is finish!")
			break

