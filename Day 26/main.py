# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# new_numbers = [n + 1 for n in numbers if n % 3 == 0]
# print(new_numbers)


# name = "Hermanni"
# name_list = [letter for letter in name]
# print(name_list)


# range_list = [num * 2 for num in range(1, 5)]
# print(range_list)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)
# print(long_names)


# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# scores = {name:random.randint(1, 100) for name in names}
# passed_students = {name:score for (name, score) in scores.items() if score > 60}
# print(passed_students)


# import pandas
# student_dict = {"student": ["Angela", "James", "Lily"],"score": [56, 76, 96]}
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}






#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")
df_dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
result = [df_dict[letters] for letters in user_input if letters in df_dict]
print(result)