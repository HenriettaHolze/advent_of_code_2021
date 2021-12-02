INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def determine_position(INPUT):
    INPUT = [line.split(" ") for line in INPUT.split("\n")]

    # horizontal, depth
    position = [0, 0]

    for command in INPUT:
        direction = command[0]
        steps = int(command[1])

        if direction == "forward":
            position[0] += steps
        elif direction == "down":
            position[1] += steps
        elif direction == "up":
            position[1] -= steps

    return position[0] * position[1]

assert(determine_position(INPUT) == 150)

with open("02.txt", "r") as o:
    commands = o.read()

print("position", determine_position(commands))

def determine_position_aim(INPUT):
    INPUT = [line.split(" ") for line in INPUT.split("\n")]

    # horizontal, depth
    position = [0, 0]
    aim = 0

    for command in INPUT:
        direction = command[0]
        steps = int(command[1])

        if direction == "down":
            aim += steps
        elif direction == "up":
            aim -= steps
        elif direction == "forward":
            position[0] += steps
            position[1] += steps * aim

    return position[0] * position[1]


assert(determine_position_aim(INPUT) == 900)

print("position aim", determine_position_aim(commands))
