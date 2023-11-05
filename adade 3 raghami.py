num = input ("")
if len(num) == 3 and num.isdigit():
    num = int(num)
    reverse_num = int(str(num)[::-1])*2
    print(reverse_num)
else:
    print("wrong number")

