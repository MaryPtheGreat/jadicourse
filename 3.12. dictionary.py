
from collections import OrderedDict

def translate(dictionary, sentence):
    translated_words = []
    for word in sentence.split():
        translated_words.append(dictionary.get(word, word))
    return ' '.join(translated_words)

# خواندن تعداد کلمات دیکشنری
n = int(input())

# ساخت دیکشنری (یا OrderedDict)
dictionary = OrderedDict()

# خواندن کلمات دیکشنری و ذخیره آنها
for _ in range(n):
    word_pair = input().split()
    dictionary[word_pair[0]] = word_pair[1]

# خواندن جمله و ترجمه آن
input_sentence = input()
output_sentence = translate(dictionary, input_sentence)
print(output_sentence)
