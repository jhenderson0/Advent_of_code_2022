import numpy as np
from collections import Counter

with open('3/data.csv') as f:
    rucksacks = []
    for line in f:
        rucksack = line.strip()
        compartment_1 = rucksack[:len(rucksack)//2]
        compartment_2 = rucksack[len(rucksack)//2:]
        rucksacks.append((compartment_1, compartment_2))

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = np.arange(1,53)

priority_map = {letter : priority for letter, priority in zip(alphabet, priorities)}

score = 0
for rucksack in rucksacks:
    compartment_1 = Counter(rucksack[0])
    compartment_2 = Counter(rucksack[1])
    common_letter = np.unique(list((compartment_1 & compartment_2).elements()))[0]
    score += priority_map[common_letter]

print(score)
