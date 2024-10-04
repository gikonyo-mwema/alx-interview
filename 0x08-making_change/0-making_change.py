#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array where dp[i] represents the minimum number of coins for amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0
    
    # Loop through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, return -1 (no solution)
    return dp[total] if dp[total] != float('inf') else -1

