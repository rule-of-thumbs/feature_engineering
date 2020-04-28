import numpy as np
import pandas as pd

def log_normal_df(df):
  # convert log normalization
  
  if not df.dtype.kind in 'biufc':
    # bool int uint float
    return df, None
  if pd.isnull(df).any():
    return df, None
  if df.loc[(df != 0) & (~pd.isnull(df))].max() == 0:
    return df, None
  # get base
  log_max = np.log(df.loc[(df != 0) & (df != np.nan)].max())
  e = df.loc[(df != 0) & (~pd.isnull(df))].min() * 1e-1
  print(e)
  
  # only change e when it zero, fill na
  df_temp = df.copy()
  df_temp.replace(0, e, inplace=True)
  df_temp.fillna(df_temp.mean(), inplace=True)
  
  # log transform
  log_transformed = np.log(df_temp) / np.log(log_max)
  return log_transformed, log_max
