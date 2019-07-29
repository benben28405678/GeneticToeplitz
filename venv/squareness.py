"""
This program takes in four 2-dimensional points, finds the distance between those points, and lets the user know
whether those points form a square.

Created by Ben Myers on July 29, 2019.
"""

import sys
import os
import math
from Point import Point
from colorama import Fore, Back, Style

TEST = True


def squareness(point1, point2, point3, point4):
    x1, y1 = point1.x, point1.y
    x2, y2 = point2.x, point2.y
    x3, y3 = point3.x, point3.y
    x4, y4 = point4.x, point4.y

    len12 = dist(x1, y1, x2, y2)
    len23 = dist(x2, y2, x3, y3)
    len34 = dist(x3, y3, x4, y4)
    len41 = dist(x4, y4, x1, y1)

    average = avg([len12, len23, len34, len41])

    offset = [len12 - average, len23 - avg, len34 - avg, len41]

    return avg(offset)


def dist(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    return math.sqrt(dx ** 2 + dy ** 2)


def avg(l):
    count = 0

    for i in l:
        count += i

    return count / len(l)


def is_square(l, margin=0):
    for i in l:
        if abs(i) > margin:
            return False
    return True


if TEST:
    print(Style.RESET_ALL)
    print(Fore.BLUE + '-- Welcome to Squareness simulator --')
    print(Style.RESET_ALL)

    testX1 = int(input('Enter your ' + Fore.YELLOW + 'first point\'s ' + Fore.GREEN + 'x-coordinate' + Fore.RESET + ': '))
    testY1 = int(input('Enter your ' + Fore.YELLOW + 'first point\'s ' + Fore.GREEN + 'y-coordinate' + Fore.RESET + ': '))
    print('First point is A := (' + str(testX1) + ',' + str(testY1) + ')')

    testX2 = int(input('Enter your ' + Fore.YELLOW + 'second point\'s ' + Fore.GREEN + 'x-coordinate' + Fore.RESET + ': '))
    testY2 = int(input('Enter your ' + Fore.YELLOW + 'second point\'s ' + Fore.GREEN + 'y-coordinate' + Fore.RESET + ': '))
    print('Second point is B := (' + str(testX2) + ',' + str(testY2) + ')')

    testX3 = int(input('Enter your ' + Fore.YELLOW + 'third point\'s ' + Fore.GREEN + 'x-coordinate' + Fore.RESET + ': '))
    testY3 = int(input('Enter your ' + Fore.YELLOW + 'third point\'s ' + Fore.GREEN + 'y-coordinate' + Fore.RESET + ': '))
    print('Third point is C := (' + str(testX3) + ',' + str(testY3) + ')')

    testX4 = int(input('Enter your ' + Fore.YELLOW + 'fourth point\'s ' + Fore.GREEN + 'x-coordinate' + Fore.RESET + ': '))
    testY4 = int(input('Enter your ' + Fore.YELLOW + 'fourth point\'s ' + Fore.GREEN + 'y-coordinate' + Fore.RESET + ': '))
    print('Fourth point is D := (' + str(testX4) + ',' + str(testY4) + ')')

    print('\nAll Points have been assigned! We now have a quadrilateral ' + Fore.MAGENTA + 'ABCD.' + Fore.RESET)

    len12 = dist(testX1, testY1, testX2, testY2)
    len23 = dist(testX2, testY2, testX3, testY3)
    len34 = dist(testX3, testY3, testX4, testY4)
    len41 = dist(testX4, testY4, testX1, testY1)

    lengths = [len12, len23, len34, len41]

    print(Style.RESET_ALL + Style.BRIGHT + Fore.RED + '\nRESULTS ' + Style.RESET_ALL)

    print('Side lengths of polygon: ' + Fore.MAGENTA + str(lengths) + Fore.RESET)

    averageLen = avg(lengths)

    print('Average side lengths of polygon: ' + Fore.MAGENTA + str(averageLen) + Fore.RESET)

    offsetLen = [len12 - averageLen, len23 - averageLen, len34 - averageLen, len41 - averageLen]

    print('Differences between side lengths and average side length: ' + Fore.MAGENTA + str(offsetLen) + Fore.RESET)

    print('The result! The set of points forms a square: ' + Style.BRIGHT + Fore.BLUE + str(is_square(offsetLen)))
