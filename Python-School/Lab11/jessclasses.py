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
                if str(character).isalpha():
                    self.alpha_dict[character.upper()] += 1
        return self.alpha_dict

    @staticmethod
    def alpha_zeroes(diction):
        # used only with dictionaries
        # returns which keys have values of zero
        return {item: diction[item] for item in diction if diction[item] == 0}

    @staticmethod
    def alpha_used(diction):
        # used only with dictionaries
        # returns which keys have values greater than zero
        return {item: diction[item] for item in diction if diction[item] > 0}

    @staticmethod
    def letter_frequency(diction, letter):
        frequency = diction[letter]
        output_dict = {key: val for key, val in diction.items() if key != letter}
        return frequency, output_dict

    def median_name(self):
        """Used to determine the median entry of a list"""
        from math import ceil
        start = 0
        end = len(self.names) - 1
        out = sorted(self.names[::])
        return out[ceil((start + end) / 2)]