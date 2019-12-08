from copy import copy
from part1 import Point

def follow_wire(commands):
    points_data = {}

    pos = Point(0, 0)
    step_count = 0

    for command in commands:
        movement = Point(0, 0)

        direction = command["direction"]
        if direction == "L":
            movement.x = -1
        if direction == "R":
            movement.x = 1
        if direction == "D":
            movement.y = -1
        if direction == "U":
            movement.y = 1
        
        for _ in range(command["distance"]):
            step_count += 1
            pos.x += movement.x
            pos.y += movement.y

            points_data[copy(pos)] = step_count

    return points_data

def parse_commands(raw_commands):
    commands = []
    for command in raw_commands:
        commands.append({
            "direction": command[0],
            "distance": int(command[1:])
        })
    
    return commands

if __name__ == "__main__":
    with open ("input.txt", "r") as f:
        raw_commands1 = f.readline().split(",")
        raw_commands2 = f.readline().split(",")
        
        commands1 = parse_commands(raw_commands1)
        commands2 = parse_commands(raw_commands2)

        points_data1 = follow_wire(commands1)
        points_data2 = follow_wire(commands2)

        print()

        intersections = list(set(points_data1.keys()) & set(points_data2.keys()))

        distances =  [
            abs(points_data1[intersection]) + abs(points_data2[intersection])
        for intersection in intersections]
        
        min_distance = min(distances)

        print(min_distance)

"""
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?

"""
