
def infinite(n):
    print(n)
    infinite(n+1)

infinite(1)

def factorial(n):
    value = 1

    while n >= 1:
        value *= n
        n -= 1

    return value

def factorial_recursive(n):

    if n < 0:
        raise ValueError("N can't be negative")

    if n == 0:
        return 1

    return n * factorial_recursive(n-1)

# works on sorted lists
def binary_search(some_list, value_to_find, start_index, end_index):
    if start_index > end_index:
        return -1 # means not found

    index_to_search = (start_index + end_index) // 2
    if some_list[index_to_search] == value_to_find:
        return index_to_search
    if some_list[index_to_search] < value_to_find:
        return binary_search(some_list, value_to_find, index_to_search + 1, end_index)
    return binary_search(some_list, value_to_find, start_index, index_to_search - 1)


print(factorial_recursive(5))


some_numbers = [ 7, 18, 4, 12, 22 ]

some_numbers.sort()

print(binary_search(some_numbers, 2, 0, 4))
for number in some_numbers:
    print(f'{number} is at index {binary_search(some_numbers, number, 0, len(some_numbers) - 1)}')


 # https://en.wikipedia.org/wiki/Fibonacci_sequence
def fibonacci(nth):
    if nth <= 0:
        return 0
    if nth == 1:
        return 1
    return fibonacci(nth-1) + fibonacci(nth-2)

for nth in range(100):
    print(f'{nth}: {fibonacci(nth):,d}')

