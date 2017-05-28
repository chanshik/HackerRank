"""
Coin Change Problem

https://www.hackerrank.com/challenges/ctci-coin-change
"""

import sys

"""
D: initialized status
coin/n  0   1   2   3   ..  n
    0   1   0   0   0       0
    1   1
    2   1
    3   1
    ..
    m   1
"""
def make_change(coins, n):
    m = len(coins)
    coins = [0] + coins

    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        D[i][0] = 1

    for i in range(1, n + 1):
        D[0][i] = 0

    for coin in range(1, m + 1):
        for amt in range(1, n + 1):
            can_add_coin = coins[coin] <= amt
            if can_add_coin:
                D[coin][amt] = D[coin - 1][amt] + D[coin][amt - coins[coin]]
            else:
                D[coin][amt] = D[coin - 1][amt]

    return D[m][n]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]

print(make_change(coins, n))

