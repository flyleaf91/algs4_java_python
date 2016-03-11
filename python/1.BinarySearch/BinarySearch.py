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

	lo=0
	hi=len(whileList)-1
	while lo < hi :
		mid = (hi+lo)//2
		print("lo={0},hi={1},mid={2}".format(lo,hi,mid))
		print("keyIn={},whileListIn[mid]={}".format(keyIn,whileListIn[mid]))

		if whileList[mid] == keyIn:
			print("keyIn found! mid = ",mid)
			return mid
		elif whileList[mid] < keyIn:
			print("<")
			lo = mid		
		else:
			print(">")
			hi = mid 

		print(lo,hi,mid)

	else:
		print("keyIn not found!")
		return -1





        
if __name__ == '__main__':

	print("Task excute start...")
	keyIn=0
	whileListIn = StdIn.readInt(sys.argv[1])
	while True:
		try:
			keyIn=int(input())
			t = BinarySearch(whileListIn,keyIn)
		except EOFError:
			print("Task excute is finish!")
			break

