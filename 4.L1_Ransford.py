# Shaine Ransford
# 3/27/2025
# 4.T1
# Linear Search

# Main program to test the linear_search() method.
def main():
    # Initalize and DisplayArray of Numbers.   
    numbers = [2, 4, 7, 10, 11, 32, 45, 87]
    print('NUMBERS:', numbers)

    # Get key from Input
    key = int(input('Enter an integer value: '))

    # Call Linear Search with args, numbers list and int input.
    key_index = linear_search(numbers, key)

    # Print key not found or key found \
    # based on linear search return statement.
    if (key_index == -1):
        print(f'\n{key} was not found.\n')
    else:
        print(f'\nFound {key} at index {key_index}.\n')

# Iterate of numbers list to find key.
def linear_search(numbers, key):
    for i in range(len(numbers)):
        if (numbers[i] == key):
            # Number found.
            return i
    # Number not found.
    return -1

# Call main
if __name__ == "__main__":
    main()