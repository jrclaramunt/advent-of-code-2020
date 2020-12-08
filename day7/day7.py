import re
from collections import defaultdict

from utils.base import Day


class Bag:
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name


class Day7(Day):

    def __init__(self, rules):
        self.rules = rules
        self.bag_regex = r'^([a-z ]+) bags contain (.+).$'
        self.contents_regex = r'(\d+) ([a-z ]+) bags?'
        self.initial_color = 'shiny gold'

    def part1(self):
        bag_tree = defaultdict(list)

        for rule in self.rules:
            full_bag = re.match(self.bag_regex, rule).groups()
            bag_name = full_bag[0]
            bag_contents = re.findall(self.contents_regex, full_bag[1])
            for content in bag_contents:
                bag_tree[content[1]].append(bag_name)

        result = list()
        self.find_containers(bag_tree, self.initial_color, result)
        return len(set(result))

    def find_containers(self, tree_bag, name, result):
        if tree_bag.get(name) is None:
            return result

        containers = tree_bag.get(name)
        for container in containers:
            result.append(container)
            self.find_containers(tree_bag, container, result)

    def part2(self):
        tree_bag = defaultdict(list)

        for rule in self.rules:
            full_bag = re.match(self.bag_regex, rule).groups()
            bag_name = full_bag[0]
            bag_contents = re.findall(self.contents_regex, full_bag[1])

            for content in bag_contents:
                tree_bag[bag_name].append(Bag(quantity=content[0], name=content[1]))

        return self.count_bags(tree_bag, Bag(quantity=1, name=self.initial_color)) - 1

    def count_bags(self, tree_bag, root_bag):
        if tree_bag.get(root_bag.name) is None:
            return int(root_bag.quantity)

        containers = tree_bag.get(root_bag.name)
        root_quantity = int(root_bag.quantity)
        total = 0

        for container in containers:
            total += root_quantity * self.count_bags(tree_bag, container)

        return total + int(root_bag.quantity)
