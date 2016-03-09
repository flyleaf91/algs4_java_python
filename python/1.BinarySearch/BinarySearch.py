#!usr/bin/python#coding=utf-8
#二分查找
#执行方式: python BinarySearch.py tinyW.txt < tinyT.txt

import sys

def gcd(q,p):

    r=q%p 
    if r==0:
        return p
    else:       
        return gcd(q,r)    
        

t = gcd(int(sys.argv[1]),int(sys.argv[2]))
print(t)    