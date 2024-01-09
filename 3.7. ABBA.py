
def order(words):
    words = words.upper()
    if "AB" in words or "BA" in words:
        index_ab = words.find("AB")
        index_ba = words.find("BA")

        if abs(index_ab - index_ba) > 1:
            return "YES"
    return "NO"

user_input = input()
print(order(user_input)

