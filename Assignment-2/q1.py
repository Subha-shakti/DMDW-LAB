data=[10,12,15,18,20,20,22,25]
total=0
for value in data :
      total+=value
mean=total/ len(data)
print("Mean=",mean)
      
    
import numpy as np
data=[10,12,15,18,20,20,22,25]
print("Mean=",np.mean(data))
