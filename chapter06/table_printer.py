#!/usr/bin/env python
import numpy as np

def printTable(table):
    t = np.array(table).T
    mylen = np.vectorize(len)
    length = np.amax(mylen(t), axis=0)
    for row in t:
        for element, l in zip(row, length):
            print(element.rjust(l + 1), end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

