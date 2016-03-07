#!usr/bin/python#coding=utf-8
#最大公约数
#执行方式: python gcd.py 数字1 数字2

import sys

def gcd(q,p):

    r=q%p 
    if r==0:
        return p
    else:       
        return gcd(q,r)    
        

t = gcd(int(sys.argv[1]),int(sys.argv[2]))
print(t)    