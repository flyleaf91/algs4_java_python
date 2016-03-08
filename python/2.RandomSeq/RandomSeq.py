#!usr/bin/python#coding=utf-8
#产生随机数

#执行方式: python RandomSeq.py N lo hi
# *  Prints N numbers between lo and hi.
# *
# *  % python RandomSeq 5 100.0 200.0
# *  123.43
# *  153.13
# *  144.38
# *  155.18
# *  104.02

import sys
import random


def RandomSeq(n,lo,hi):
	
	for i in range(n):
		print("{0:.2f}".format(random.uniform(lo,hi)))
        
if len(sys.argv) == 2:
	for i in range(int(sys.argv[1])):
		print("{0:.2f}".format(random.random()))
elif 	len(sys.argv) == 4:
	RandomSeq(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
else:
	print("parm error")
