import pandas as pd

s = pd.Series([0.0, 1.0, 0.000000, 2.0])
print(s)
s = s[s != 0.0]
print(s)