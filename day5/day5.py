from collections import defaultdict
from enum import Enum
from math import floor, ceil

from utils.base import Day


class Codes(Enum):
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'


class Day5(Day):

    def __init__(self, args):
        self.nearby_boarding_passes = args[0]
        self.plane_seats = defaultdict(list)
        self.id_list = []
        self.n_rows = 128
        self.n_seats_per_row = 8

    def search_in_plane(self, boarding_pass, element_range):
        if element_range[0] == element_range[1]:
            return element_range[0]

        if boarding_pass[0] == Codes.FRONT.value or boarding_pass[0] == Codes.LEFT.value:
            lower_limit = element_range[0]
            upper_limit = floor((element_range[1] + element_range[0]) / 2)
            return self.search_in_plane(boarding_pass[1:], (lower_limit, upper_limit))

        elif boarding_pass[0] == Codes.BACK.value or boarding_pass[0] == Codes.RIGHT.value:
            lower_limit = element_range[0] + ceil((element_range[1] - element_range[0]) / 2)
            upper_limit = element_range[1]
            return self.search_in_plane(boarding_pass[1:], (lower_limit, upper_limit))

        else:
            raise Exception()

    def part1(self):
        highest_id = 0

        for boarding_pass in self.nearby_boarding_passes:
            row = self.search_in_plane(boarding_pass[0:self.n_rows - 1], (0, self.n_rows - 1))
            seat = self.search_in_plane(boarding_pass[7:], (0, self.n_seats_per_row - 1))
            self.plane_seats[row].append(seat)

            seat_id = 8 * row + seat
            self.id_list.append(seat_id)
            if seat_id >= highest_id:
                highest_id = seat_id

        return highest_id

    def part2(self):
        all_seats = [i for i in range(8)]
        for row in range(self.n_rows):
            if 0 < len(self.plane_seats[row]) < self.n_seats_per_row:
                missing_seats = list(set(all_seats) - set(self.plane_seats[row]))
                for missing_seat in missing_seats:
                    own_seat_id = row * self.n_seats_per_row + missing_seat

                    if (own_seat_id + 1) in self.id_list and (own_seat_id - 1) in self.id_list:
                        return own_seat_id
