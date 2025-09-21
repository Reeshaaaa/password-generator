from random import choice
from characters import chars
from user_input import UserInput

user_input = UserInput()
length = user_input.length_input()
chosen_chars = user_input.char_select()

# Flatten the list of possible characters
available_chars = [c for group in chosen_chars for c in chars[group]]

# Generate password using random choices
password = ''.join(choice(available_chars) for _ in range(length))

print(password)