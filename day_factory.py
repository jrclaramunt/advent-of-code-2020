from day1.day1 import Day1


class DayFactory:

    def __init__(self, day, input_data):
        self.map = {
            1: Day1(input_data)
        }
        print(f'Day {day}\n')
        print(self.map.get(day).solution())
