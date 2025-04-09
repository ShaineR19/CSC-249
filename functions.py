"""
Shaine Ransford
4/9/2023
4.H1
This file contains the functions for a binary search program.
"""
import random

def menu():
    print('\nMain Menu')
    print('1) Binary Search Demo')
    print('2) Binary Search Game')
    print('3) Exit')
    choice = input("Enter a Menu option: ")
    return choice

def binary_search_demo():
    numbers = []
    size = 10
    go = True
    
    for i in range(size):
        random_num = random.randint(1, 100)
        numbers.append(random_num)
    
    numbers.sort()
    print("\nNUMBERS: ")
    for num in numbers:
        print(num)
        
    while go:
        try:
            key = int(input("\nEnter an integer to search for: "))
            go = False
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    keyIndex = BinarySearch(numbers, key)

    if (keyIndex == -1):
        print(f"\n{key} was not found.")
   
    else:
        print(f"\nFound {key} at index {keyIndex}.")
     
def binary_search_game():
    low = 0
    high = 99
    attempts = 0
    max_attempts = 5
    
    print("\nI am going to try to guess your number!!!")
    while attempts < max_attempts:
        mid = (low + high) // 2
        
        print(f"\nIs {mid} your number?")
        choice = input(f"'<'(Less than {mid})\n"
                       f"'>'(Greater than {mid})\n"
                       f"'='(Equal to {mid})\n"
                       "Select One: ")
        
        if choice == '=':
            print(f"\nI guessed your number {mid} :).")
            break
            
        elif choice == '>':
            low = mid + 1
            attempts += 1
            
        elif choice == '<':
            high = mid - 1
            attempts += 1
            
        else:
            print("ERROR: Select a correct symbol....")
            
    if attempts >= max_attempts:
        print("\nI have taken too long :(.")
        
def BinarySearch(numbers, key):
   low = 0
   high = len(numbers) - 1
   
   while (high >= low):
      mid = (high + low) // 2 # integer division
      
      if (numbers[mid] < key):
         low = mid + 1
         
      elif numbers[mid] > key:
         high = mid - 1
         
      else:
         return mid # key found
     
   return -1  # not found
