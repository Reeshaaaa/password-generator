from random import randrange, choice
from characters import chars
from user_input import UserInput

user_input = UserInput()
length = user_input.length_input()
chosen_chars = user_input.char_select()
password = []
output = ""

for character in range(length):
    #appends random characters
    char_list = choice(chosen_chars)
    password.append(chars[char_list][randrange(0, len(chars[char_list]))])

for character in password:
    #rewrites the password into string
    output += character

print(output)