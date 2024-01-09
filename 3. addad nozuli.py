

input_expression = input()
numbers = [int(num) for num in input_expression.split('+')]

sorted_numbers = sorted(numbers)

output_expression = '+'.join(map(str, sorted_numbers))
print(output_expression)