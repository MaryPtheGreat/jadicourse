
max_age = -1

while True:
    age = int(input())
    if age <= 0:
        break
    elif 10 <= age <= 90:
        if age > max_age:
            max_age = age

if max_age == -1:
    print("wrong number")
else:
    print(max_age)