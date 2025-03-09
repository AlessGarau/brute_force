from file_handler import FileHandler
from itertools import product

class BruteForce:
    def __init__(self, password_file, file_handler):
        self.password_file = password_file
        self.file = file_handler
        self.passwords = []

    def _get_password_file(self):
        return self.password_file
    
    def _set_password(self, word):
        self.passwords.append(word)
    
    def initialize_password(self):
        self.passwords = []
        password_file = self._get_password_file()
        with open(password_file) as file:
            for line in file:
                word = line.split()
                self._set_password(word)
    
    def generate_password(self, password_length):
        characters_min = "abcdefghijklmnopqrstuvwxyz"
        characters_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_common = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        all_characters = characters_min + characters_maj + numbers + special_common

        for password in product(all_characters, repeat=password_length):
            print(password)
            yield "".join(password)