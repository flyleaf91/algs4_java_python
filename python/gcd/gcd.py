#!usr/bin/python#coding=utf-8
#���Լ��
#ִ�з�ʽ: python gcd.py ����1 ����2

import sys

def gcd(q,p):

    r=q%p 
    if r==0:
        return p
    else:       
        return gcd(q,r)    
        

t = gcd(int(sys.argv[1]),int(sys.argv[2]))
print(t)    