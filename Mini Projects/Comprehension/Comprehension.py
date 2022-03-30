# List Comprehension

# numbers

numbers = [1, 2, 3]

# new_number = [new_item for item in list]

new_number = [n + 1 for n in numbers]

print(new_number)

# alphabets

name = "Kishore"

# new_list = [letter for letter in name]

new_list = [letter for letter in name]

print(new_list)

# Range

range_list = [num * 2 for num in range(1, 5)]

print(range_list)

# Conditional

names = ["Alex", "Beth", " Caroline", "Dave", "Eleanor", "Freddie"]

# short_name = [new_item for item in list if test]

short_names = [name for name in names if len(name) < 5]
print(short_names)

# long_name = [new_item for item in list if test]

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Exercise 1

number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_number = [n ** 2 for n in number]

print(squared_number)

# Exercise 2

number = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in number if num % 2 == 0]

print(result)

# # Dictionary

# new_dict ={new_key:new_value for (key, value) in dict.items()}

names = ["Alex", "Beth", " Caroline", "Dave", "Eleanor", "Freddie"]

import random

# new_dict ={new_key:new_value for item in list}

students_scores = {student: random.randint(1, 100) for student in names}

print(students_scores)

# # Dictionary from Dictionary

# passed_student = {new_key:new_value for (key, value) in dictionary.item() if test}

passed_student = {student: score for (student, score) in students_scores.items() if score >= 60}

print(passed_student)

# Iteration with Pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries

# for (key, value) in student_dict.items():
#     print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)


# # Looping through DataFrame
#
# for(key, value) in student_data_frame.items():
#     print(key, value)

# Loop through rows of DataFrame

for (index, row) in student_data_frame.iterrows():
    print(index, row)