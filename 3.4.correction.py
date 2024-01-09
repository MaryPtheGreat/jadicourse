
from collections import Counter
def check_hello(word):
    word_counter = Counter(word)
    hello_counter = Counter("hello")

    for char, count in hello_counter.items():
        if word_counter[char] < count:
            return "NO"

    return "YES"

word = input()
result = check_hello(word)
print(result)
