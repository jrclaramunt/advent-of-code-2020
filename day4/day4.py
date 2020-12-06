import re

from day4.passport import PasswordFields, Byr, Iyr, Eyr, Hgt, Hcl, Ecl, PasswordField
from utils.base import Day


class Day4(Day):

    def __init__(self, passports):
        self.passports = passports
        self.regex = r'([a-z]{3}):([a-zA-Z#0-9]+)[ |\n]'

    def is_passport_valid(self, field_list):
        return (len(field_list) == 7 and PasswordFields.COUNTRY_ID.value not in field_list) \
               or len(field_list) == 8

    def part1(self):
        valid_passports = 0
        present_fields = []

        for line in self.passports:
            fields = list(map(lambda x: x[0], re.findall(self.regex, line)))
            present_fields += fields

            if not fields:
                if self.is_passport_valid(present_fields):
                    valid_passports += 1

                present_fields = []

        if self.is_passport_valid(present_fields):
            valid_passports += 1

        return valid_passports

    def get_valid_field_name(self, x):
        p = PasswordField(x)
        if p.is_valid():
            return p.name

    def part2(self):
        valid_passports = 0
        passport_valid_fields = []

        for line in self.passports:
            fields = list(map(self.get_valid_field_name, re.findall(self.regex, line)))
            passport_valid_fields += fields

            if not fields:
                filtered_list = list(filter(lambda x: x is not None, passport_valid_fields))
                if self.is_passport_valid(filtered_list):
                    valid_passports += 1

                passport_valid_fields = []

        filtered_list = list(filter(lambda x: x is not None, passport_valid_fields))
        if self.is_passport_valid(filtered_list):
            valid_passports += 1

        return valid_passports
