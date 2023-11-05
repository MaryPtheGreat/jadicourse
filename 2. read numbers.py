
def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

numbers = []
divisor_counts = []

for _ in range(20):
    num = int(input())
    numbers.append(num)
    divisor_counts.append(count_divisors(num))

max_divisor_count = max(divisor_counts)
max_divisor_index = divisor_counts.index(max_divisor_count)
max_divisor_number = numbers[max_divisor_index]


print(max_divisor_number, max_divisor_count)
