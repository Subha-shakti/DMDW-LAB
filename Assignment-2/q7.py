import numpy as np
import statistics as stats

data=[10,15,20,25,30,35,40,45,50,55]

mean=np.mean(data)
print(f"Mean:{mean}")

median=np.median(data)
print(f"Median:{median}")

mode=stats.mode(data)
print(f"Mode:{mode}")

sd=np.std(data)
print(f"Standard Deviation:{sd}")

variance=np.var(data)
print(f"Variance:{variance}")
