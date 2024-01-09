
import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    password_hashes = OrderedDict()
    for number in range(1000, 10000):
        hash_object = hashlib.sha256(str(number).encode())
        hashed_number = hash_object.hexdigest()
        password_hashes[hashed_number] = str(number)

    with open(input_file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        cracked_passwords = []

        for row in csv_reader:
            username, hashed_password = row
            plain_password = password_hashes.get(hashed_password, None)
            if plain_password:
                cracked_passwords.append([username, plain_password])

    with open(output_file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for item in cracked_passwords:
            csv_writer.writerow(item)
