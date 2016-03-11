#!usr/bin/python#coding=utf-8
# readInt 读取文件中的所有整数

import sys

result=[]
def readInt(filename):
    with open(filename,'r')as f:
        for line in f:
            result.append(int(line))
        return result

if __name__ == "__main__":

	print(readInt(sys.argv[1]))
