from utils.base import Day


class Day6(Day):

    def __init__(self, answers):
        self.answers = answers

    def part1(self):
        total = 0
        group_answers = set()

        for answer in self.answers:
            answer = set(answer.rstrip())
            group_answers = group_answers.union(answer)

            if not answer:
                total += len(group_answers)
                group_answers = set()

        total += len(group_answers)

        return total

    def part2(self):
        total = 0
        group_answers = []

        for answer in self.answers:
            answer = set(answer.rstrip())

            if answer:
                group_answers.append(answer)
            else:
                common_answers = set.intersection(*group_answers)
                total += len(common_answers)
                group_answers = []

        common_answers = set.intersection(*group_answers)
        total += len(common_answers)

        return total
