
def count_distinct_prime_factors(n):
    """Count the number of distinct prime factors of a given number."""
    distinct_count = 0
    # Check for 2s
    if n % 2 == 0:
        distinct_count += 1
        while n % 2 == 0:
            n = n // 2

    # Check for other primes
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            distinct_count += 1
            while n % i == 0:
                n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        distinct_count += 1

    return distinct_count

# Read 10 numbers from the user, each on a new line
print()
numbers = [int(input()) for _ in range(10)]

# Initialize variables for the maximum distinct count and corresponding number
max_distinct_count = 0
number_with_max_distinct_factors = 0

# Check each number for its distinct prime factors
for number in numbers:
    current_distinct_count = count_distinct_prime_factors(number)
    if current_distinct_count > max_distinct_count or (current_distinct_count == max_distinct_count and number > number_with_max_distinct_factors):
        max_distinct_count = current_distinct_count
        number_with_max_distinct_factors = number

# Print the result
print(f"{number_with_max_distinct_factors} {max_distinct_count}")
# print(f"Number with the most distinct prime factors: {number_with_max_distinct_factors}, Distinct prime factors count: {max_distinct_count}")



