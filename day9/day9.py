import sys

from utils.base import Day


class Day9(Day):

    def __init__(self, args):
        port_output = args[0]
        self.port_output = list(map(lambda x: int(x), port_output))
        if args[1]['test']:
            self.number_preamble = 5
        else:
            self.number_preamble = 25

    def part1(self):
        for i in range(self.number_preamble, len(self.port_output)):
            result = self.port_output[i]

            preamble_range = self.port_output[i - self.number_preamble: i]
            is_present = False
            for preamble_number in preamble_range:
                candidate = result - preamble_number
                if candidate in preamble_range and candidate != preamble_number:
                    is_present = True

            if is_present is False:
                return result

    def part2(self):
        target = self.part1()

        for i in range(len(self.port_output)):
            total = 0
            min_value = sys.maxsize
            max_value = 0

            for j in self.port_output[i:]:
                total += j
                min_value = min(min_value, self.port_output[i])
                max_value = max(max_value, j)

                if total > target:
                    break
                elif total == target:
                    return min_value + max_value
