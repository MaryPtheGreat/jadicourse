import random


def main():
  print("بازی حدس عدد!")
  print("لطفاً عدد خود را انتخاب کنید (بین 1 تا 99) و به کامپیوتر نگویید.")

  min_number = 1
  max_number = 99
  guessed_number = None

  while True:
    # حدس زدن یک عدد تصادفی بین min_number و max_number
    if guessed_number is None:
      guessed_number = random.randint(min_number, max_number)

    print("کامپیوتر حدس زده: {}".format(guessed_number))

    user_input = input("آیا حدس کامپیوتر درست است؟ (k: کمتر، b: بیشتر، d: درست): ")

    if user_input == 'k':
      max_number = guessed_number - 1
      guessed_number = None
    elif user_input == 'b':
      min_number = guessed_number + 1
      guessed_number = None
    elif user_input == 'd':
      print("کامپیوتر حدس را درست زده. بازی تمام شد!")
      break
    else:
      print("لطفاً یکی از k، b، یا d را انتخاب کنید.")


if __name__ == "__main__":
  main()

