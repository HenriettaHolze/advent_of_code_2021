INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

def calculate_gamma_epsilon(INPUT):
    n = len(INPUT)
    gamma_rate = []
    epsilon_rate = []
    for i in range(len(INPUT[0])):
        mysum = sum([int(j[i]) for j in INPUT])
        if mysum / n < 0.5:
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")

    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)

    return gamma_rate, epsilon_rate

def calculate_rates(INPUT):
    INPUT = INPUT.split()
    gamma_rate, epsilon_rate = calculate_gamma_epsilon(INPUT)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)

assert(calculate_rates(INPUT) == 198)

with open("03.txt", "r") as o:
    consumption = o.read()

print("rate", calculate_rates(consumption))

# ==================================================================

def calculate_rates_2(INPUT):

    INPUT = INPUT.split()
    ogr = INPUT
    csr = INPUT

    for j in range(len(INPUT[0])):
        gamma_rate, _ = calculate_gamma_epsilon(ogr)
        ogr_new = []
        for i in range(len(ogr)):
            if ogr[i][j] == gamma_rate[j]:
                ogr_new.append(ogr[i])
        ogr = ogr_new

        if len(ogr) == 1:
            break

    for j in range(len(INPUT[0])):
        _, epsilon_rate = calculate_gamma_epsilon(csr)
        csr_new = []
        for i in range(len(csr)):
            if csr[i][j] == epsilon_rate[j]:
                csr_new.append(csr[i])
        csr = csr_new

        if len(csr) == 1:
            break

    return int(ogr[0], 2) * int(csr[0], 2)

assert(calculate_rates_2(INPUT) == 230)

print("rate 2", calculate_rates_2(consumption))
