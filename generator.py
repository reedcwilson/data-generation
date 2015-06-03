import random as rand
import numpy as np

variance = 3
mean = 0
current = 1000
mins = []
maxes = []
for i in range(150):
  val = int(max(0, current + np.random.normal(mean, variance)))
  print np.random.normal(mean, variance)
  mins.append(val)
  current = val

for m in mins:
  maxes.append(int(max(m + 2, np.random.normal(m + 20, variance))))


print mins
print maxes
