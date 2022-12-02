from functools import reduce
from copy import copy, deepcopy
import math

class Planet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.xvel = 0
        self.yvel = 0
        self.zvel = 0

    def pot_energy(self):
        return sum(map(abs, (self.x, self.y, self.z)))

    def kin_energy(self):
        return sum(map(abs, (self.xvel, self.yvel, self.zvel)))

    def total_energy(self):
        return self.pot_energy() * self.kin_energy()

    def __repr__(self):
        return f"🪐{{ {self.x}, {self.y}, {self.z} }}"

    def apply_gravity(self, other):
        xvel_increment = 0 if self.x == other.x else (1 if self.x < other.x else -1)
        yvel_increment = 0 if self.y == other.y else (1 if self.y < other.y else -1)
        zvel_increment = 0 if self.z == other.z else (1 if self.z < other.z else -1)

        self.xvel += xvel_increment
        self.yvel += yvel_increment
        self.zvel += zvel_increment

    def update_positions(self):
        self.x += self.xvel
        self.y += self.yvel
        self.z += self.zvel

    def __eq__(self, other):
        return self.x == other.x \
            and self.y == other.y \
            and self.z == other.z \
            and self.xvel == other.xvel \
            and self.yvel == other.yvel \
            and self.zvel == other.zvel

def lcm(a, b, c):
    return abs(a*b*c) // (math.gcd(math.gcd(a, b), c))

if __name__ == "__main__":
    with open("input2.txt", 'r') as f:
        planets = []
        for line in f:
            raw_data = list(map(int, map(lambda s: s.split("=")[1], map(lambda s: s.strip(), line.replace("<", "").replace(">", "").split(",")))))
            planets.append(Planet(raw_data[0], raw_data[1], raw_data[2]))

        initial_planets = deepcopy(planets)
        print(f"INITIAL : {planets}")

        iteration = 0
        x_repeat = 0
        y_repeat = 0
        z_repeat = 0

        while(True):
            for planet in planets:
                for other_planet in planets:
                    if planet is other_planet: # Don't apply gravity to self!
                        continue

                    planet.apply_gravity(other_planet)
                    
            for planet in planets:
                planet.update_positions()

            check = True
            for planet, initial_planet in zip(planets, initial_planets):
                cond = planet.x == initial_planet.x
                if not cond:
                    check = False
                    break
            
            if check:
                # print(x_repeat)
                x_repeat = iteration if x_repeat == 0 else x_repeat

            check = True
            for planet, initial_planet in zip(planets, initial_planets):
                cond = planet.y == initial_planet.y
                if not cond:
                    check = False
                    break

            if check:
                # print(y_repeat)
                y_repeat = iteration if y_repeat == 0 else y_repeat

            check = True
            for planet, initial_planet in zip(planets, initial_planets):
                cond = planet.z == initial_planet.z
                if not cond:
                    check = False
                    break
            
            if check:
                # print(z_repeat)
                z_repeat = iteration if z_repeat == 0 else z_repeat

            if x_repeat and y_repeat and z_repeat:
                break

            iteration += 1

        print(x_repeat)
        print(y_repeat)
        print(z_repeat)
        print(lcm(x_repeat, y_repeat, z_repeat))
        print(x_repeat * y_repeat * z_repeat)
