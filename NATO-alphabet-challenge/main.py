# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df_to_dict = data.to_dict()
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}

entered_word = input("Enter a word: ").upper()
# answer_list = [value for key,value in new_dict.items() if key in entered_word]
answer_list = [new_dict.get(letter) for letter in entered_word]
print(answer_list)
