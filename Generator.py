#!/usr/bin/env python
import csv
from random import *
import sys

file = "hej" + ".csv"
Row = 0
Col = 0
RandomRangeOne = 0
RandomeRangeTwo = 0

def Generate():
    print("Hello, first of, thanks for using this software. Second, you should be aware that")
    print(" even though this software is really light weight and simple, it is able to really")
    print("mess up your system if you don't have much space left.")
    print("I did some tests. And the results show that this tool is capable of generating files")
    print("that use multible gigabytes in few minuts.")
    print("How big should the range of the numbers be? (From x to y)")
    print("x")
    RandomRangeOne = int(input())
    print("y")
    RandomRangeTwo = int(input())

    print("How many rows do you want?")
    Row = int(input())
    print("How many coloums do you want? ")
    Col = int(input())

    for i in range(Col):
        for i in range(Row):
            with open('test.csv', 'w') as f:
                print(randrange(RandomRangeOne, RandomRangeTwo), end=",")
        print()

Generate()