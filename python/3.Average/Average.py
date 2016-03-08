#!usr/bin/python#coding=utf-8
#计算平均值

# /******************************************************************************
#  *  Compilation:  pythoncAverage.py
#  *  Execution:    python Average < data.txt
#  *
#  *  Reads in a sequence of real numbers, and computes their average.
#  *
#  *  % python Average
#  *  10.0 5.0 6.0
#  *  3.0 7.0 32.0
#  *  [Ctrl-d]
#  *  Average is 10.5
#  *
#  *  Note [Ctrl-d] signifies the end of file on Unix.
#  *  On windows use [Ctrl-z].
#  *
#  ******************************************************************************/

__author__ = 'Administrator'

import  sys

reply=[]
sumd=0

while True:
    try:
        reply.append(float(input()))
    except EOFError:
        for x in reply:
            sumd += x
        average = sumd/len(reply)
        print("Average is",average)
        break





