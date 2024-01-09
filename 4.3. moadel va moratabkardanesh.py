
import csv
from statistics import mean
from collections import OrderedDict

def read_grades_from_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        grades = {}
        for rows in reader:
            if len(rows) > 1:
                grades[rows[0]] = list(map(int, rows[1:]))
    return grades

def calculate_averages(grades):
    return {name: mean(grades) for name, grades in grades.items()}

def save_averages(averages, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for name, avg in averages.items():
            writer.writerow([name, avg])

def task1(grades):
    averages = calculate_averages(grades)
    print()
    for name, avg in averages.items():
        print(f"{name}: {avg}")
    save_averages(averages, 'task1.csv')

def task2(grades):
    averages = calculate_averages(grades)
    sorted_averages = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))
    print()
    for name, avg in sorted_averages.items():
        print(f"{name}: {avg}")
    save_averages(sorted_averages, 'task2.csv')

def task3(grades):
    averages = calculate_averages(grades)
    top_3 = OrderedDict(sorted(averages.items(), key=lambda x: (-x[1], x[0]))[:3])
    print()
    for name, avg in top_3.items():
        print(f"{name}: {avg}")
    save_averages(top_3, 'task3.csv')

def task4(grades):
    averages = calculate_averages(grades)
    bottom_3 = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0]))[:3])
    print()
    for _, avg in bottom_3.items():
        print(avg)
    with open('task4.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for avg in [avg for _, avg in bottom_3.items()]:
            writer.writerow([avg])

def task5(grades):
    averages = calculate_averages(grades)
    all_means = mean(averages.values())
    print(all_means)
    with open('task5.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([all_means])

# Main code
file_path = "C:\\Users\\merse\\PycharmProjects\\jadicourse\\input.csv"
grades = read_grades_from_csv(file_path)
task1(grades)
task2(grades)
task3(grades)
task4(grades)
task5(grades)










