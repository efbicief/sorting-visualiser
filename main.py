import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

def bubbleSort(ls):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(ls)), ls)
    plt.title("Bubble Sort")

    change = True

    while change:
        change = False

        for i in range(len(ls)-1):
            currel = ls[i]
            nextel = ls[i+1]

            if currel > nextel:
                change = True
                ls[i] = nextel
                ls[i+1] = currel

                for rect,h in zip(rects,ls):
                    rect.set_height(h)
                fig.canvas.draw()
                plt.pause(0.001)

def cocktailSort(ls):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(ls)), ls)
    plt.title("Cocktail Shaker Sort")

    change = True

    while change:
        change = False

        for i in range(len(ls)-1): #going up
            currel = ls[i]
            nextel = ls[i+1]

            if currel > nextel:
                change = True
                ls[i] = nextel
                ls[i+1] = currel

                for rect,h in zip(rects,ls):
                    rect.set_height(h)
                fig.canvas.draw()
                plt.pause(0.001)
        
        for i in range(len(ls)-1): #going down
            currel = ls[(len(ls)-i)-1]
            nextel = ls[(len(ls)-i)-2]

            if currel < nextel:
                change = True
                ls[(len(ls)-i)-1] = nextel
                ls[(len(ls)-i)-2] = currel

                for rect,h in zip(rects,ls):
                    rect.set_height(h)
                fig.canvas.draw()
                plt.pause(0.001)

nums = []
for i in range(1,51):
    nums.append(i)
shuffle(nums)
print('shuffled')

menuitem = input("Which sort?\n(B)ubble sort\n(C)ocktail Shaker sort\n > ").lower()
if menuitem == 'b':
    bubbleSort(nums)
elif menuitem == 'c':
    cocktailSort(nums)
