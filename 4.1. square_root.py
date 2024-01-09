
import math

n = int(input())

numbers = [float(input()) for _ in range(n)]

for num in numbers:
    square_root = math.sqrt(num)
    square_root_str = "{:.8f}".format(square_root)
    print(square_root_str[:-4])

