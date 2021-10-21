import csv
with open('D:/001 Interview/internship-test2/input/question-2/main.csv', 'r') as file:
    reader = csv.reader(file)
    for col in reader:
        print(col)
    