import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000)+1,
                   'b':np.random.randn(1000),
                   'c':np.random.randn(1000) - 1,
                   'd':np.random.randn(1000)}, 
                    columns=['a', 'b', 'c','d'])

df.diff().hist(bins=10)
'''
x = pd.DataFrame(np.random.randn(1000))
x.diff().hist(bins=20)
'''