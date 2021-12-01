INPUT = """199
200
208
210
200
207
240
269
260
263"""

def count_increases(INPUT):
    """Count how many measurements are larger than the previous one."""
    INPUT = [int(number) for number in INPUT.split()]
    increases = 0
    for i in range(1, len(INPUT)):
        if INPUT[i] > INPUT[i - 1]:
            increases += 1
    return increases

assert(count_increases(INPUT) == 7)

with open("01.txt", "r") as o:
    measurements = o.read()

print("Number of increases", count_increases(measurements))


def count_increases_sliding_window(INPUT):
    """Count how many sliding windows (step size 3) are larger than the previous one."""
    INPUT = [int(number) for number in INPUT.split()]
    increases = 0
    for i in range(1, len(INPUT) - 2):
        if INPUT[i+2] > INPUT[i - 1]:
            increases += 1
    return increases

assert(count_increases_sliding_window(INPUT) == 5)

print("Number of increases sliding window", count_increases_sliding_window(measurements))
