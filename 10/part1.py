from functools import reduce
from copy import copy, deepcopy
from fractions import Fraction

en = enumerate

class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"☄️ {{ {self.x}, {self.y} }}"

    def __eq__(self, other):
        return self.x == other.x \
            and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        data = f.read()
        rows = data.split('\n')
        
        grid = list(map(lambda row: [k for k in map(lambda x: x is '#', row)], rows))
        grid.pop()

        assert(len(grid) == len(grid[0]))
        grid_size = len(grid)

        for row in grid:
            print(row)

        asteroids = {}
        for row_i, row in en(grid):
            for col_i, is_asteroid in en(row):
                if is_asteroid:
                    asteroids[(col_i, row_i)] = Asteroid(col_i, row_i)

        for asteroid in asteroids.values():
            print(asteroid)

        answers = []

        # For each asteroid
        for asteroid in asteroids.values():
            for row in grid:
                for elem in row:
                    print(" X " if elem else " . ", end='')
                print()

            print(f"Currently scanning {asteroid}")

            # List of asteroids that this asteroid can see
            line_of_sight_asteroids = set()

            # List of asteroids already processes, skip these
            completed_asteroids = set()

            # List of slopes along which we already have searched, skip these
            completed_slopes = set()
            
            # For every other asteroid
            for other_asteroid in asteroids.values():
                # Don't compare against itself
                if asteroid is other_asteroid:
                    continue

                print(f"    Comparing against {other_asteroid}")

                # Skip this if we already saw it
                if other_asteroid in completed_asteroids:
                    print(f"        Seen, skipping...")
                    continue

                # Check for zero x
                if other_asteroid.x == asteroid.x:
                    print(f"        Y Axis...")
                    # This is a vertical point, let's just iterate through the y axis and scan for planets

                    # First, do down from the current asteroid
                    blocked = False
                    for j in range(min(asteroid.y + 1, grid_size), grid_size):
                        if (asteroid.x, j) in asteroids:
                            current = asteroids[(asteroid.x, j)]
                            
                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")

                    # Then, search upwards from the current asteroid
                    blocked = False
                    for j in range(max(asteroid.y - 1, 0), 0, -1):
                        if (asteroid.x, j) in asteroids:
                            current = asteroids[(asteroid.x, j)]
                            
                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")


                # Check for zero y
                elif other_asteroid.y == asteroid.y:
                    print(f"        X Axis...")
                    # This is a horizonal point, let's just iterate through the y axis and scan for planets

                    # First, go right from the current asteroid
                    blocked = False
                    for j in range(min(asteroid.x + 1, grid_size), grid_size):
                        if (j, asteroid.y,) in asteroids:
                            current = asteroids[(j, asteroid.y,)]
                            
                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")

                    # Then, search left from the current asteroid
                    blocked = False
                    for j in range(max(asteroid.x - 1, 0), 0, -1):
                        if (j, asteroid.y,) in asteroids:
                            current = asteroids[(j, asteroid.y,)]
                            
                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")

                # This is a diagonal point
                else:
                    print(f"        Diagonal...")
                    slope = Fraction(
                        (other_asteroid.y - asteroid.y),
                        (other_asteroid.x - asteroid.x))

                    if slope in completed_slopes:
                        continue
                    else:
                        completed_slopes.add(slope)

                    x_increment = slope.denominator
                    y_increment = slope.numerator

                    curr_x = asteroid.x
                    curr_y = asteroid.y

                    blocked = False
                    while True:
                        curr_x += x_increment
                        curr_y += y_increment

                        if curr_x >= grid_size \
                        or curr_x < 0 \
                        or curr_y >= grid_size\
                        or curr_y < 0:
                            break

                        check_point = (curr_x, curr_y)

                        print(f"            Going to check {check_point}")

                        # If we found an asteroid at the point!
                        if check_point in asteroids and asteroids[check_point] != asteroid:
                            current = asteroids[check_point]

                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")

                    
                    blocked  = False
                    while True:
                        curr_x -= x_increment
                        curr_y -= y_increment

                        if curr_x >= grid_size \
                        or curr_x < 0 \
                        or curr_y >= grid_size\
                        or curr_y < 0:
                            break

                        check_point = (curr_x, curr_y)

                        # If we found an asteroid at the point!
                        if check_point in asteroids and asteroids[check_point] != asteroid:
                            current = asteroids[check_point]

                            # Skip the ones we've seen
                            if current in completed_asteroids:
                                print(f"        Seen, skipping...")
                                continue

                            # This is a new one
                            if not blocked:
                                # We can see this asteroid
                                completed_asteroids.add(current)
                                line_of_sight_asteroids.add(current)
                                blocked = True

                                print(f"        Can see {current} ✅")
                            else:
                                completed_asteroids.add(current)

                                print(f"        Blocked {current} ❌")


            if asteroid in line_of_sight_asteroids:
                line_of_sight_asteroids.remove(asteroid)

            count = len(line_of_sight_asteroids)
            print(f"Count for {asteroid}: {count}\n")
            answers.append((asteroid, count))

        print
        print(f"ANSWER : {max(answers, key=lambda x: x[1])}")
