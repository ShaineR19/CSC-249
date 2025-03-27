# Shaine Ransford
# 3/27/2025
# 4.T1
# Find Max Value (learn about )

import random 

def main():

    # Random list 
    min_val = 0
    max_val = 1000
    size = 10
    randomlist = [random.randint(min_val, max_val) for _ in range(size)]

    # Initalize current_max to first index of list
    current_max = randomlist[0]

    # Compare each n with current_max
    for index_value in randomlist:
        if index_value > current_max:
            # Print and update current_max if index_value is larger than current_max
            print(f"\nCurrent Max = {current_max}")
            print(f"Index Value = {index_value}")
            current_max = index_value
            print(f"New Max = {current_max}")
        else:
            # Print Index Value if smaller than current_max
            print(f"\nIndex Value: {index_value}")

    print(f"\nGlobal Max = {current_max}")

if __name__ == "__main__":
    main()