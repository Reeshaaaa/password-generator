import sys

class UserInput:
    def length_input(self):
        try:
            length = int(input("Enter the password length: "))
        except ValueError:
            sys.exit()
        return length

    def char_select(self):
        chosen_chars = []
        nums = input("Do you want to add numbers? (y/n) ")
        if nums == "y":
            chosen_chars.append(0)

        lower = input("Do you want to add lowercase letters? (y/n) ")
        if lower == "y":
            chosen_chars.append(1)

        upper = input("Do you want to add uppercase letters? (y/n) ")
        if upper == "y":
            chosen_chars.append(2)

        specials = input("Do you want to add special characters? (y/n) ")
        if specials == "y":
            chosen_chars.append(3)

        if chosen_chars == []:
            print("You've chosen nothing. Do you even want to make a password?")
            sys.exit()
        else:
            return chosen_chars