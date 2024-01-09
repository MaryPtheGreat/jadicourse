import csv
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        grades = [(row[0], mean(map(float, row[1:]))) for row in reader]

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, average in grades:
            writer.writerow([name, average])

def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        grades = sorted([(row[0], mean(map(float, row[1:]))) for row in reader], key=lambda x: (x[1], x[0]))

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, average in grades:
            writer.writerow([name, average])

def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        grades = sorted([(row[0], mean(map(float, row[1:]))) for row in reader], key=lambda x: x[1], reverse=True)[:3]

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, average in grades:
            writer.writerow([name, average])

def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        grades = sorted([(row[0], mean(map(float, row[1:]))) for row in reader], key=lambda x: x[1])[:3]

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _, average in grades:
            writer.writerow([average])

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        all_averages = [mean(map(float, row[1:])) for row in reader]

    overall_average = mean(all_averages)

    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([overall_average])


