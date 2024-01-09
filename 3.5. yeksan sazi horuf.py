
def modify_word(word):
    uppercase_count = sum(1 for char in word if char.isupper())
    lowercase_count = len(word) - uppercase_count

    if uppercase_count > lowercase_count:
        return word.upper()
    else:
        return word.lower()


user_input = input()
result = modify_word(user_input)
print(result)

