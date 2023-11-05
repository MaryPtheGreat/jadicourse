
input_str = input()
result_str = ""

for char in input_str:
    if char.lower() not in 'aeiou' and char.isalpha():
        result_str += f".{char.lower()}"

print(result_str)
