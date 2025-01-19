# Function to display the list elements
def display_list(lst):
    print("List elements:", " ".join(map(str, lst)))

# Function to search for an element in the list
def search_element(lst, key):
    for i, value in enumerate(lst):
        if value == key:
            return i  # Return the index if found
    return -1  # Return -1 if not found

def main():
    lst = []  # Initialize an empty list

    # Inserting elements into the list
    print("Adding elements to the list...")
    for i in range(1, 11):  # Insert multiples of 2
        lst.append(i * 2)

    # Display the list
    display_list(lst)

    # Search for an element
    key = int(input("Enter an element to search: "))
    index = search_element(lst, key)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
