import pandas as pd
import numpy as np

df = pd.DataFrame([25,25,25,25], 
                  index=['a', 'b', 'c', 'd'], 
                  columns=['y'])
df.plot.pie(subplots=False)