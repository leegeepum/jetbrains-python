prime_numbers = [num for num in range(2, 1001) if not any(num % n == 0 for n in range(2, num))]
print(prime_numbers)
