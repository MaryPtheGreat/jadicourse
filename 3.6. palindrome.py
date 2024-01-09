
def ispalindrome (word):
    word = word.lower()
    length = len(word)

    for i in range (length//2):
        if word[i] != word[length-i-1]:
            return "not palindrome"
        return "palindrome"


input_word = input()
print(ispalindrome(input_word))
