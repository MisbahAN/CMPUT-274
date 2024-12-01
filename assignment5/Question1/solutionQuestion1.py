# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: Windows 11
# python version: Python 3.11.9

def min_coins(coins, S):
    # Initialize a very large value to represent impossible sums (acts as "infinity")
    large_value = 9999999
    
    # Create a dynamic programming array to store the minimum number of coins for every amount from 0 to S. Initialize all values to large_value
    dynamic_array = [large_value] * (S + 1)
    
    # Base case: It takes 0 coins to make the sum 0
    dynamic_array[0] = 0
    
    # Loop through each coin denomination
    for coin in coins:
        # Update the dynamic array for every amount from 'coin' to 'S'
        for i in range(coin, S + 1):
            # Calculate the minimum coins required:
            # Option 1: Don't use this coin (keep the current value of dynamic_array[i])
            # Option 2: Use this coin (1 + the value for the remaining amount: dynamic_array[i - coin])
            dynamic_array[i] = min(dynamic_array[i], dynamic_array[i - coin] + 1)
    
    # After filling  dynamic_array, check if the value for 'S' is still the large_value
    if dynamic_array[S] != large_value:
        return dynamic_array[S]  # minimum number of coins required for sum S
    else:
        return -1  # not possible to form the sum

def main():
    coins = list(map(int, input().split()))
    S = int(input())
    print(min_coins(coins, S))

if __name__ == "__main__":
    main()