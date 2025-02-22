def binary_search(numbers, key):
    # Variables to hold the low, middle and high indices
    # of the area being searched. Starts with entire range.
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    # Loop until "low" passes "high"
    while (high >= low):
        # calculate the middle index
        mid = (high + low) // 2

        # Cut the range to either the left or right half,
        # unless numbers[mid] is the key
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid   
   
    return -1 # not found


# Main program to test the binary_search() function   
numbers = [1.8, 2.6, 3.4, 4.1, 5.6, 6.3, 7.5, 8.7, 9.2, 10.0]
print('NUMBERS:', numbers)
     
key = float(input('Enter an integer value: '))
key_index = binary_search(numbers, key)
     
if (key_index == -1):
    print(f'{key} was not found.')
else:
    print(f'Found {key} at index {key_index}.')
