import math

data = [10, 12, 15, 18, 20, 20, 22, 25]

mean = sum(data) / len(data)

variance = 0
for value in data:
   variance += (value - mean) ** 2

variance =variance / len(data)

sd = math.sqrt(variance)

print("Standard Deviation =", sd)

import numpy as np

print("Standard Deviation =", np.std(data))
