def calc_mean(data):
    return sum(data) / len(data)


def calc_median(data):
    sd = sorted(data)
    n = len(sd)
    mid = n // 2

    if n % 2 == 0:
        median = (sd[mid - 1] + sd[mid]) / 2
    else:
        median = sd[mid]

    return median


def calc_mode(data):
    fre = {}

    for num in data:
        fre[num] = fre.get(num, 0) + 1

    mode = max(fre, key=fre.get)
    return mode


def calc_variance(data):
    mean = calc_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return variance


def calc_sd(data):
    variance = calc_variance(data)
    sd = variance ** 0.5
    return sd


data = [int(x) for x in input("Enter a series of numbers: ").split()]

mean = calc_mean(data)
median = calc_median(data)
mode = calc_mode(data)
variance = calc_variance(data)
sd = calc_sd(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {sd}")
