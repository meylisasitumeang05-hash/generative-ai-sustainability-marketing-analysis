import pandas as pd

constructs = ['M1_GWS_mean', 'M2_TR_mean', 'Y_PI_mean']

desc = df[constructs].describe().T
print(desc)
