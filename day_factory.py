from day1.day1 import Day1
from day2.day2 import Day2
from day3.day3 import Day3
from day4.day4 import Day4
from day5.day5 import Day5
from day6.day6 import Day6
from day7.day7 import Day7
from day8.day8 import Day8
from day9.day9 import Day9


class DayFactory:

    def __init__(self, day, *args):
        self.map = {
            1: Day1,
            2: Day2,
            3: Day3,
            4: Day4,
            5: Day5,
            6: Day6,
            7: Day7,
            8: Day8,
            9: Day9
        }
        print(f'Day {day}')
        self.map.get(day)(args).solution()
