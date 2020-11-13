# Written for CSC.120 assignment, would like to reuse some work I've already done :P
import sys
sys.path.append(".")
from jessclasses import CharacterManipulation


if __name__ == '__main__':
    user_input = input('Enter a String: ')
    # convert user input to a list of the string items for imported Class
    output = CharacterManipulation([character for character in user_input])
    output.alpha_counter()
    for key in output.alpha_dict.keys():
        if output.alpha_dict[key] > 0:
            print(key, output.alpha_dict[key])
