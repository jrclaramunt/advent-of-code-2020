import re

from utils.base import Day


class Day2(Day):

    def __init__(self, password_file):
        self.password_file = password_file
        self.regex = r'^(\d+)-(\d+) ([a-z]): ([a-z]*)$'

    def part1(self):
        valid_passwords = 0

        for entry in self.password_file:
            tmp = re.search(self.regex, entry).groups()
            min = int(tmp[0])
            max = int(tmp[1])
            character = tmp[2]
            password = tmp[3]
            if min <= password.count(character) <= max:
                valid_passwords += 1

        return valid_passwords

    def part2(self):
        valid_passwords = 0

        for entry in self.password_file:
            tmp = re.search(self.regex, entry).groups()
            first_index = int(tmp[0]) - 1
            second_index = int(tmp[1]) - 1
            character = tmp[2]
            password = tmp[3]
            if (password[first_index] == character) ^ (password[second_index] == character):
                valid_passwords += 1

        return valid_passwords
