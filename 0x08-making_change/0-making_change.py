#!/usr/bin/python3
"""
determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    '''Return: fewest number of coins needed'''
    if total < 1:
        return 0
    coins.sort()
    coins.reverse()
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
