def linear_search(numbers, key):
    for i in range(len(numbers)):
       if (numbers[i] == key):
           return i
    return -1  # not found

# Main program to test the linear_search() method   
numbers = [1.8, 2.6, 3.4, 4.1, 5.6, 6.3, 7.5, 8.7, 9.2, 10.0]
print('NUMBERS:', numbers)
     
key = float(input('Enter a value from the list: '))
key_index = linear_search(numbers, key)
     
if (key_index == -1):
    print(f'{key} was not found.')
else:
    print(f'Found {key} at index {key_index}.')
