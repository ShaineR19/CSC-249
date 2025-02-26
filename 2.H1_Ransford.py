def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def fibonacci_recursive(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    return memo[n]


def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example Usage
n = 10
print("Fibonacci Series (Iterative):", fibonacci_iterative(n))
print("Fibonacci Series (Recursive, nth term):", [fibonacci_recursive(i) for i in range(n)])

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print("Binary Search (Iterative):", binary_search_iterative(arr, target))
print("Binary Search (Recursive):", binary_search_recursive(arr, target, 0, len(arr) - 1))
