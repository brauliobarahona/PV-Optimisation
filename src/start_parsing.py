import os, sys
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
ddir = '../data'
fns = os.listdir(ddir)

# files in data file directory
for i in fns:
    print(i)

# let us load the dfs
for i in fns:
    print(pd.read_csv(os.path.join(ddir,i)).head())
df = pd.read_csv(os.path.join(ddir,i))
df
ax=df.plot()

# the available channels are
list(df)


df=df.set_index('Timestamp')
ax=df.plot()

# how are Grid_Supply_kW and Grid_Feed-In_kW different?
# what parts of the plants are consuming? e.g Grid_Supply-In_kW?
# is Overall_Consumption_Calc_kW simply the difference between Feed, Supply, and Generation? What are the signs?
## %hist -f start_parsing.py
