#!/usr/bin/python3
"""
Module for the makeChange function.
"""


def makeChange(coins, total):
    """
    Given a target amount 'total'
    Return min num of coins
    """
    if total <= 0:
        return 0

    # Initialize dp arr with large value to compare with min
    dp = [float('inf')] * (total + 1)  # (total + 1) to include base case
    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        for x in range(coin, total + 1):
            # Update the dp array for each amount from coin to total
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] still float('inf'),means that total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
