import re
import math
from collections import defaultdict

class Record:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} {self.value}"

    def __repr__(self):
        return self.__str__()

class Equation:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        lhs_string = ", ".join(map(lambda x: x.__str__(), self.lhs))
        return f'{lhs_string} -> {self.rhs}'

    @classmethod
    def from_string(cls, equation_string):
        (lhs_string, rhs_string) = tuple(equation_string.split(" => "))
        lhs_strings = lhs_string.split(", ")
        lhs = [Record(record_string.split(" ")[1].strip(), int(record_string.split(" ")[0].strip())) for record_string in lhs_strings]
        rhs = Record(rhs_string.split(" ")[1].strip(), int(rhs_string.split(" ")[0].strip()))

        return Equation(lhs, rhs)

equations = {}
reserve = defaultdict(int)

def get_required_ore(element, qty_requested, depth = 0):
    # We are able trivially produce ORE
    if element == "ORE":
        return qty_requested

    # If we've already got some of this element, return from the reserve
    qty = qty_requested
    excess_available = reserve[element] if element in reserve else 0
    if excess_available != 0:
        if excess_available >= qty:
            excess_available -= qty
            qty = 0
        elif excess_available < qty:
            qty -= excess_available
            excess_available = 0

        # Deduct from reserve
        reserve[element] = excess_available

    if qty == 0:
        return 0

    # We must find out how to make this current element
    production_rule = equations[element]
    
    dependencies = production_rule.lhs
    smallest_order_unit = production_rule.rhs.value

    order_multiplier = math.ceil(qty / smallest_order_unit)
    final_production = smallest_order_unit * order_multiplier
    excess_production = final_production - qty

    ore_required = 0
    for dependency in dependencies:
        ore_required += get_required_ore(dependency.name, dependency.value * order_multiplier, depth + 1)

    # Add the excess production to the reserve
    reserve[element] += excess_production

    return ore_required

with open("input.txt", "r") as f:
    for line in f:
        equation = Equation.from_string(line)
        equations[equation.rhs.name] = equation

    print(f"Ans : {get_required_ore('FUEL', 1)}")
