from functools import reduce

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


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        planets = []
        for line in f:
            raw_data = list(map(int, map(lambda s: s.split("=")[1], map(lambda s: s.strip(), line.replace("<", "").replace(">", "").split(",")))))
            planets.append(Planet(raw_data[0], raw_data[1], raw_data[2]))

        print(planets)

        iterations = 1000

        for planet in planets:
            print(planet, end=' ')

        for iteration in range(iterations):

            print(f"{iteration}: ", end='')
            for planet in planets:
                print(planet, end=' ')
            print()

            for planet in planets:
                for other_planet in planets:
                    if planet is other_planet: # Don't apply gravity to self!
                        continue

                    planet.apply_gravity(other_planet)
                    
            for planet in planets:
                planet.update_positions()


        print(f"{iterations}: ", end='')
        for planet in planets:
            print(planet, end=' ')
        print()

        sum = reduce(lambda x, y: x + y.total_energy(), planets, 0)
        print(f"Ans : {sum}")
