import numpy as np
import pandas as pd
from scipy.stats import entropy

# df, sequence > bool(regular), amount(regular)
def regularity_df(df, boolean=False, shift=False):
    # columns의 순서가 중요하다
    df_temp = df.copy()
    
    # replace nan values
    df_temp[(pd.isnull(df_temp))] = 0
    # parallel move when data is negative
    if (df_temp.min() < 0) and (shift):
        df_temp += abs(df_temp.min())
    
    if boolean == True:
        df_temp = df_temp.astype(bool)
  
    return entropy(df_temp.T)
