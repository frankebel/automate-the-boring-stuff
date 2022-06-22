#!/usr/bin/env python
import random
from itertools import groupby

random.seed(0)

threshold = 6
experiments = 10_000
count = 0

# Do experiment.
for _ in range(experiments):
    # Create list of heads, tails values.
    n = 100
    flips = [random.randint(0, 1) for _ in range(n)]

    # Consecutive maximum occurrence in list.
    aux = [sum(1 for _ in b) for a, b in groupby(flips)]
    consecutive = max(aux)
    
    # Add to count.
    if consecutive >= threshold:
        count += 1

print(f'Percentage of streak >= {threshold}: {count/experiments*100} %')

