import numpy as np
from collections import Counter


with open('3/data.csv') as f:
    groups = []
    i = 1
    group = []
    for line in f:
        if i%4 == 0:
            groups.append(group)
            i = 1
            group = []
        group.append(line.strip())
        i += 1
groups.append(group)
        
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = np.arange(1,53)
priority_map = {letter : priority for letter, priority in zip(alphabet, priorities)}

score = 0
for group in groups:
    elf_1 = Counter(group[0])
    elf_2 = Counter(group[1])
    elf_3 = Counter(group[2])
    
    common_letter = np.unique(list((elf_1 & elf_2 & elf_3).elements()))[0]
    score += priority_map[common_letter]

print(score)
