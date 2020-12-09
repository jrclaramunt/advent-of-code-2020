import re
from enum import Enum

from utils.base import Day


class Instructions(Enum):
    ACC = 'acc'
    JMP = 'jmp'
    NOP = 'nop'


class Runner:
    def __init__(self):
        self.current_line = 0
        self.accumulator = 0
        self.steps = []

        self.instruction_set = {
            Instructions.ACC.value: self.acc,
            Instructions.JMP.value: self.jmp,
            Instructions.NOP.value: self.nop
        }

    @classmethod
    def regex(cls):
        return r'^([a-z]{3}) ([\+|-]\d+)$'

    def find_loop(self, code_base):
        while 1:
            parsed_line = re.match(Runner.regex(), code_base[self.current_line].rstrip()).groups()
            instruction = parsed_line[0]
            argument = int(parsed_line[1])

            if self.current_line in self.steps:
                return self.accumulator

            self.instruction_set[instruction](argument)

    def run(self, code_base):
        while 1:
            if self.current_line == len(code_base):
                return self.accumulator

            parsed_line = re.match(Runner.regex(), code_base[self.current_line].rstrip()).groups()
            instruction = parsed_line[0]
            argument = int(parsed_line[1])

            if self.current_line in self.steps:
                return None

            self.instruction_set[instruction](argument)

    def acc(self, argument):
        self.accumulator += argument
        self.steps.append(self.current_line)
        self.current_line += 1

    def jmp(self, argument):
        self.steps.append(self.current_line)
        self.current_line += argument

    def nop(self, *args):
        self.steps.append(self.current_line)
        self.current_line += 1


class Day8(Day):

    def __init__(self, args):
        self.code_base = args[0]

    def part1(self):
        return Runner().find_loop(self.code_base)

    def part2(self):
        nop_indexes = []
        jmp_indexes = []

        for index in range(len(self.code_base)):
            parsed_line = re.match(Runner.regex(), self.code_base[index].rstrip()).groups()
            instruction = parsed_line[0]
            if instruction == Instructions.NOP.value:
                nop_indexes.append(index)

            if instruction == Instructions.JMP.value:
                jmp_indexes.append(index)

        for nop_index in nop_indexes:
            code_base = self.code_base.copy()
            code_base[nop_index] = self.code_base[nop_index].replace(Instructions.NOP.value, Instructions.JMP.value)
            accumulator = Runner().run(code_base)
            if accumulator is not None:
                return accumulator

        for jmp_index in jmp_indexes:
            code_base = self.code_base.copy()
            code_base[jmp_index] = self.code_base[jmp_index].replace(Instructions.JMP.value, Instructions.NOP.value)
            accumulator = Runner().run(code_base)
            if accumulator is not None:
                return accumulator
