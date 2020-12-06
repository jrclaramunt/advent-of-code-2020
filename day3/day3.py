from enum import Enum

from utils.base import Day
from utils.utils import Coordinate


class MapElements(Enum):
    OPEN_SQUARE = '.'
    TREE = '#'


class Day3(Day):

    def __init__(self, area_map):
        self.area_map = area_map
        self.current_position = Coordinate(0, 0)
        self.destination_row = len(self.area_map)
        self.slopes = [
            {'right': 3, 'down': 1},
            {'right': 1, 'down': 1},
            {'right': 5, 'down': 1},
            {'right': 7, 'down': 1},
            {'right': 1, 'down': 2},
        ]

    def restart_position(self):
        self.current_position.update(0, 0)

    def check_for_tree(self, current_position):
        if self.area_map[current_position.y][current_position.x] == MapElements.TREE.value:
            return True
        return False

    def update_position(self, slope):
        x = (self.current_position.x + slope['right']) % (len(self.area_map[0]) - 1)
        y = self.current_position.y + slope['down']
        self.current_position.update(x, y)

    def part1(self):
        trees = 0

        while self.current_position.y < self.destination_row:
            if self.check_for_tree(self.current_position):
                trees += 1
            self.update_position(self.slopes[0])

        return trees

    def part2(self):
        total_trees = 1

        for slope in self.slopes:
            self.restart_position()
            trees = 0
            while self.current_position.y < self.destination_row:
                if self.check_for_tree(self.current_position):
                    trees += 1
                self.update_position(slope)

            total_trees *= trees

        return total_trees
