# API create file and create csv

with open('diary.txt', 'w') as f:
    f.write("Day 1: I started learning Python!\n")
    f.write("Day 2: I learned how to write files.")

with open('diary.txt', 'r') as f:
    print(f.read())

with open('diary.txt', 'w') as f:
    f.write("Day 1: I started learning Python!\n")
    f.write("Day 2: I learned how to write files.")


import csv
student_result = [
    ["stuend_name","student_result", "student_result_grade"],
    ["studentA", 60, "B"],
    ["studentB", 65, "B"],
    ["studentC", 85, "A"],
    ["studentD", 70, "A"],
    ["studentE", 50, "C"],
    ["studentF", 40, "C"],
    ["studentG", 55, "C"],
    ["studentH", 50, "C"],
    ["studentI", 10, "F"],

    ]
with open("students_result_file.csv", mode="w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(student_result)


import pandas as pd
data = pd.read_csv("students_result_file.csv")
data.head()
print("\n")
print(data[data['student_result_grade'] == 'C'])
print("\n")
print(data[data['student_result'] <= 60])

# JSON
import json
data = {"b": 22, "a": 100, "d": 46, "c": 89, "dfsdf": 78}
print("\n")
print(json.dumps(data, indent=2, sort_keys=True))

# Step 1: Load JSON data from file
data1 = [
      {"name": "John Doe", "age": 30},
      {"name": "Jane Smith", "age": 25}
    ]

filepath = 'output.json'
with open(filepath, 'w') as f:
      json.dump(data1, f, indent=4)

with open("output.json", "r") as read_file:
    data5 = json.load(read_file)

# Step 2: Access specific values
print(data5)
print("\n")
print("Name:", data5[1])