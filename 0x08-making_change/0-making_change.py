#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet a given total."""
    if total <= 0:
        return 0
    coin = total
    count = 0
    ind = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while coin > 0:
        if ind >= n:
            return -1
        if coin - sorted_coins[ind] >= 0:
            coin -= sorted_coins[ind]
            count += 1
        else:
            ind += 1
    return count
