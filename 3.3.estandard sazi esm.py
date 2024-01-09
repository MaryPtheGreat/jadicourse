
def standardize_name(name):
    # استانداردسازی نام با تبدیل حرف اول به بزرگ و سایر حروف به کوچک
    return name.capitalize()

# خواندن ۱۰ اسم از ورودی
names = []
for i in range(10):
    name = input().format(i + 1)
    names.append(standardize_name(name))

# چاپ نتیجه استانداردسازی
print()
for standardized_name in names:
    print(standardized_name)

