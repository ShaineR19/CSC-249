"""
Shaine Ransford
4/9/2023
4.H1 - Gold
This file contains the menu for a binary search program.
"""
import functions as f

def main():
    go = True
    while go:
        
        choice = f.menu()
        if choice == '1':
            f.binary_search_demo()
            
        elif choice == '2':
            f.binary_search_game()
            
        elif choice == '3':
            print('\nProgram Shutting Down...')
            go = False
            
        else:
            print('\nERROR: Select an option from the menu...')
            
if __name__ == "__main__":
    main()