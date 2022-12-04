import pandas as pd
import numpy as np

pairs = pd.read_csv('4/data.csv', sep='-|,|[|]', 
                  engine='python', header=None).to_numpy()

check = []
for pair in pairs:

    #elf 2 is contained within elf 1
    if (pair[2] >= pair[0]) and (pair[3] <= pair[1]) :
        check.append(True)

    #elf 1 is contained within elf 2
    elif (pair[0] >= pair[2]) and (pair[1] <= pair[3]) :
        check.append(True)

    else:
        check.append(False)

print(np.sum(check))