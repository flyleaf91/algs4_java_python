#!usr/bin/python#coding=utf-8

import sys

result=[]
def readInt(filename):
    with open(filename,'r')as f:
        for line in f:
            result.append(int(line))
        print(result)

readInt(sys.argv[1])
