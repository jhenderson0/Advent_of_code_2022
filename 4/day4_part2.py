import pandas as pd
import numpy as np

pairs = pd.read_csv('4/data.csv', sep='-|,|[|]', 
                  engine='python', header=None).to_numpy()

check = []
for pair in pairs:

    range1 = set(np.arange(pair[0], pair[1]+1))
    range2 = set(np.arange(pair[2], pair[3]+1))

    if len(range1 & range2) > 0:
        check.append(True)
    else:
        check.append(False)
        
print(np.sum(check))