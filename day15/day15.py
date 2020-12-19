import time

from utils.base import Day


class Day15(Day):

    def __init__(self, args):
        self.starting_numbers = args[0][0].rstrip().split(',')

    def get_n_position(self, n):
        history = {}
        sequence = []

        for turn in range(1, n + 1):
            if turn - 1 < len(self.starting_numbers):
                sequence.append(self.starting_numbers[turn - 1])
                history[self.starting_numbers[turn - 1]] = {
                    'occurrences': 1,
                    'turns': [turn]
                }
            else:
                last_spoken_number = str(sequence[turn - 2])
                entry = history.get(last_spoken_number)

                if entry is None or entry['occurrences'] == 1:
                    sequence.append('0')
                    try:
                        history['0']['occurrences'] += 1
                        history['0']['turns'].append(turn)
                        if len(history['0']['turns']) > 2:
                            del history['0']['turns'][0]

                    except KeyError:
                        history['0'] = {
                            'occurrences': 1,
                            'turns': [turn]
                        }
                else:
                    next_number = str(history[last_spoken_number]['turns'][1] - history[last_spoken_number]['turns'][0])
                    sequence.append(next_number)
                    try:
                        history[next_number]['occurrences'] += 1
                        history[next_number]['turns'].append(turn)
                        if len(history[next_number]['turns']) > 2:
                            del history[next_number]['turns'][0]

                    except KeyError:
                        history[next_number] = {
                            'occurrences': 1,
                            'turns': [turn]
                        }

        return sequence[n - 1]

    def part1(self):
        start = time.time()
        result = self.get_n_position(2020)
        end = time.time()
        print(f'Total time: {end - start}')
        return result

    def part2(self):
        start = time.time()
        result = self.get_n_position(30000000)
        end = time.time()
        print(f'Total time: {end - start}')
        return result
