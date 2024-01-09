#
# import random
#
# def generate_random_number():
#     return random.randint(1, 20)
#
# # Example usage
# random_number = generate_random_number()
# print("Random Number:", random_number)


!pip install pillow
python3
from PIL import Image
im = Image.open("bridge.jpg")
im.rotate(45).show()