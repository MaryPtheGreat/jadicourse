
largest_age = -1
second_largest_age = -1


while True:
    age = int(input())

    if age < 0:
        break

    if age > largest_age:
        second_largest_age = largest_age
        largest_age = age
    elif age > second_largest_age:
        second_largest_age = age


print(largest_age, second_largest_age)
