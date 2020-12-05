from day1.day1 import Day1
from day2.day2 import Day2
from day3.day3 import Day3
from day4.day4 import Day4


class DayFactory:

    def __init__(self, day, input_data):
        self.map = {
            1: Day1,
            2: Day2,
            3: Day3,
            4: Day4
        }
        print(f'Day {day}')
        self.map.get(day)(input_data).solution()
