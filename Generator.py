#!/usr/bin/env python
import csv
from random import *
import sys

file = "hej" + ".csv"
Roww = 0
Coll = 0
RandomRangeOne = 0
RandomeRangeTwo = 0
Numbe = 0
inp = ""

def Numbers():
    print("How big should the range of the numbers be? (From x to y)")
    print("x")
    RandomRangeOne = int(input())
    print("y")
    RandomRangeTwo = int(input())
    Numbe = randrange(RandomRangeOne,RandomRangeTwo)

def RowCol():
    print("How many coloums do you want? ")
    Coll = int(input())
    print("How many rows do you want?")
    Roww = int(input())
    for i in range(Coll):
        for i in range(Roww):
            print(Numbe, end="")
        print()

def DoTheCool():
    print("What you want? ")
    Numbers()
    RowCol()
DoTheCool()