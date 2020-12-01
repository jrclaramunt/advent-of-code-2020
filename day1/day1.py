class Day1:

    def __init__(self, expense_report):
        self.expense_report = set(map(lambda line: int(line), expense_report))
        self.total = 2020

    def solution(self):
        for expense_line in self.expense_report:
            partial = self.total - expense_line

            if partial in self.expense_report:
                print(f'Part 1: {partial * expense_line}')
                break

        expense_report_list = list(self.expense_report)

        for i in range(0, len(self.expense_report)):
            first_line = expense_report_list[i]
            first_partial = self.total - first_line

            for j in range(i + 1, len(self.expense_report)):
                second_line = expense_report_list[j]
                second_partial = first_partial - second_line

                if second_partial in self.expense_report:
                    print(f'Part 2: {first_line * second_partial * second_line}')
                    exit(0)


