def print_numbers(n):
    if n == 0:          # base case
        return

    print(n)
    print_numbers(n - 1)   # recursive call


# Test
print_numbers(5)