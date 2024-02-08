# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend". # Eg. file name is : "letter_for_Aang.txt"

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as starting_letter_data:
    letter_data_list = starting_letter_data.readlines()
first_line = letter_data_list[0]

with open("Input/Names/invited_names.txt") as invited_names_data:
    names_data_list = invited_names_data.readlines()

string = ""
for i in range(1, len(letter_data_list)):
    string += letter_data_list[i]

letters_list = []
new_letters_list = []
for name in names_data_list:
    name = name.strip()
    new_first_line = first_line.replace("[name]", name)
    letters_list = new_first_line + string
    new_letters_list.append(letters_list)


# print(new_letters_list)

def file_name_generator(my_name):
    my_name = my_name.replace(" ", "")
    my_name = my_name.strip()
    return f"letter_for_{my_name}"


# print(file_name_generator(names_data_list[6]))

for name_count in range(0, len(names_data_list)):
    with open(f"Output/ReadyToSend/{file_name_generator(names_data_list[name_count])}.txt", "w") as final_data:
        final_data.write(new_letters_list[name_count])
