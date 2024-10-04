#!/usr/bin/python3
"""
Module: coin_change
Provides a function to determine the fewest number of coins needed 
to reach a given total amount using dynamic programming.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    This function uses dynamic programming to find the optimal solution
    by building up the solution to smaller subproblems and using that 
    information to solve the overall problem.

    Args:
        coins (List[int]): List of available coin denominations.
        total (int): The total amount we want to make using the coins.

    Returns:
        int: The fewest number of coins needed to reach the total. 
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the available coins.
    
    Example:
        >>> makeChange([1, 2, 5], 11)
        3  # (5 + 5 + 1)

        >>> makeChange([2], 3)
        -1  # impossible to make 3 with only coin of 2
    """
    
    # Handle base case where total is 0 or less
    if total <= 0:
        return 0
    
    # Initialize dp array where dp[i] will hold the minimum number of coins
    # needed for amount 'i'. Set dp[0] to 0 since 0 coins are needed for 0 total.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0

    # Loop through all coin denominations
    for coin in coins:
        # Update the dp array for each amount from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            # dp[amount] is the minimum coins needed to make 'amount'

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    # Test cases
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1

