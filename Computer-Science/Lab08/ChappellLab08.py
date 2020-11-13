class CharacterManipulation:
    """General manipulation of characters and strings in lists"""
    def __init__(self, list1):
        from string import ascii_uppercase
        self.names = list1
        self.vowels = ["A", "E", "I", "O", "U"]
        self.alpha_dict = {alpha: 0 for alpha in ascii_uppercase}
        self.characters = 0

    def first_last_character(self):
        """Used to return the first and last character from a each item in a list of strings as a new string"""
        # returns new string as output_string
        output_string = ""
        for item in self.names:
            output_string = output_string + item[0] + item[-1]
        return output_string

    def reverse_string_in_list(self):
        """Used to reverse strings in a list without disrupting list ordering"""
        # returns new list as output_list
        output_list = []
        for item in self.names:
            output_list.append(item[::-1])
        return output_list

    def character_count(self):
        """Used to count the number of characters in each item of a list and sum the whole"""
        # returns character count as output_num
        for item in self.names:
            self.characters = self.characters + len(item)
        return self.characters

    def consonant_counter(self):
        """Used to count the number of consonants in an item of a list and sum the whole"""
        # returns consonant count as consonants
        consonants = 0
        for item in self.names:
            for character in item:
                if character.upper() in self.vowels:
                    pass
                elif character.upper() not in self.vowels:
                    consonants += 1
        return consonants

    def vowel_counter(self):
        """Used to count the number of vowels in a string in a list of strings and sum the whole"""
        # returns vowel_count
        vowel_count = 0
        for item in self.names:
            for character in item:
                if character.upper() in self.vowels:
                    vowel_count += 1
                else:
                    pass
        return vowel_count

    def alpha_counter(self):
        # used only with dictionaries
        # returns self.alpha_dict
        for item in self.names:
            for character in item:
                self.alpha_dict[character.upper()] += 1
        return self.alpha_dict

    def alpha_zeroes(self, diction):
        # used only with dictionaries
        # returns which keys have values of zero
        return {item: diction[item] for item in diction if diction[item] == 0}

    def median_name(self):
        """Used to determine the median entry of a list"""
        from math import ceil
        start = 0
        end = len(self.names) - 1
        out = sorted(self.names[::])
        return out[ceil((start + end) / 2)]


if __name__ == '__main__':
    names = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat", "Turing", "Euler", "Einstein", "Boole",
             "Fibonacci", "Lovelace", "Noether", "Nash", "Wiles", "Cantor", "Gauss", "Plato"]
    answers = CharacterManipulation(names)

    print("Answer 1: The first and last characters from each name in the list are", answers.first_last_character())
    print("Answer 2: The list with the characters in each name reversed is", answers.reverse_string_in_list())
    print("Answer 3: The total number of characters in the list is", answers.character_count())
    print("Answer 4: The total number of consonants in the list is", answers.consonant_counter())
    answers.alpha_counter()
    print("Answer 5:")
    for key in answers.alpha_dict:
        print(f"\t\t\tThere are {answers.alpha_dict[key]} {key}'s")
    print("Answer 6: The Average length of each name in the list of names is:",
          format(answers.characters / len(names), '.2f'), "characters")
    print("Answer 7: The letter that appears the most is", max(answers.alpha_dict.items(), key=lambda x: x[1])[0],
          "and it appears", max(answers.alpha_dict.items(), key=lambda x: x[1])[1], "times")
    print("Answer 8: The following letters appear 0 times in the list of names")
    for key in answers.alpha_zeroes(answers.alpha_dict):
        print(f"\t\t\t{key}")
    print("Answer 9: The median name in the sorted list is", answers.median_name())
    print("Answer 10: The number of vowels in the list of names is", answers.vowel_counter())





