# import sys
# sys.path.append(".")
from jessclasses import CharacterManipulation

if __name__ == '__main__':
    user_input = input("Enter a string: ")
    output = CharacterManipulation([character for character in user_input])
    user_letter = input("Choose a letter: ").upper()
    alpha_dict_count = output.alpha_counter()
    alpha_dict_nonzero = CharacterManipulation.alpha_used(alpha_dict_count)
    frequency = CharacterManipulation.letter_frequency(alpha_dict_nonzero, user_letter)
    print(f"Frequency count of letter {user_letter.upper()}: {frequency[0]}")
    print(f"Dictionary after that letter removed: {frequency[1]}")
    print(f"Letters sorted: {[key for key, val in frequency[1].items()]}")


