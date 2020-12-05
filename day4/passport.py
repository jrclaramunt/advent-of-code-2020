import re
from enum import Enum


class PasswordFields(Enum):
    BIRTH_YEAR = 'byr'
    ISSUE_YEAR = 'iyr'
    EXPIRATION_YEAR = 'eyr'
    HEIGHT = 'hgt'
    HAIR_COLOR = 'hcl'
    EYE_COLOR = 'ecl'
    PASSPORT_ID = 'pid'
    COUNTRY_ID = 'cid'


class Byr:
    def __init__(self, value):
        self.value = int(value)

    def is_valid(self):
        return 1920 <= self.value <= 2002


class Iyr:
    def __init__(self, value):
        self.value = int(value)

    def is_valid(self):
        return 2010 <= self.value <= 2020


class Eyr:
    def __init__(self, value):
        self.value = int(value)

    def is_valid(self):
        return 2020 <= self.value <= 2030


class Hgt:
    def __init__(self, value):
        self.value = value
        self.regex_cm = r'^(\d{3})cm$'
        self.regex_in = r'^(\d{2})in$'

    def is_valid(self):
        if re.search(self.regex_cm, self.value) is not None:
            return 150 <= int(re.search(self.regex_cm, self.value).groups()[0]) <= 193
        elif re.search(self.regex_in, self.value) is not None:
            return 59 <= int(re.search(self.regex_in, self.value).groups()[0]) <= 76
        else:
            return False


class Hcl:
    def __init__(self, value):
        self.value = value
        self.regex = r'^#[0-9a-f]{6}$'

    def is_valid(self):
        return re.match(self.regex, self.value) is not None


class Ecl:
    def __init__(self, value):
        self.value = value
        self.regex = r'^amb|blu|brn|gry|grn|hzl|oth$'

    def is_valid(self):
        return re.match(self.regex, self.value) is not None


class Pid:
    def __init__(self, value):
        self.value = value
        self.regex = r'^[0-9]{9}$'

    def is_valid(self):
        return re.match(self.regex, self.value) is not None


class Cid:
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return True


class PasswordField:

    def __init__(self, field):
        self.name = field[0]
        self.value = field[1]
        self.factory = {
            PasswordFields.BIRTH_YEAR.value: Byr,
            PasswordFields.ISSUE_YEAR.value: Iyr,
            PasswordFields.EXPIRATION_YEAR.value: Eyr,
            PasswordFields.HEIGHT.value: Hgt,
            PasswordFields.HAIR_COLOR.value: Hcl,
            PasswordFields.EYE_COLOR.value: Ecl,
            PasswordFields.PASSPORT_ID.value: Pid,
            PasswordFields.COUNTRY_ID.value: Cid
        }

    def is_valid(self):
        return self.factory.get(self.name)(self.value).is_valid()
