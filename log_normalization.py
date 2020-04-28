import numpy as np
import pandas as pd

# nobs, mx, mu, var, skew, kurt = stats.describe(log_transformed)
# get log normalization fit parameters: Log-Max
# https://towardsdatascience.com/transforming-skewed-data-73da4c2d0d16
def log_normal_df(df):
  # convert log normalization
  
  if not df.dtype.kind in 'biufc':
    # bool int uint float
    return df, None
  if pd.isnull(df).all():
    return df, None
  if df.max() == 0:
    return df, None
  # get base
  log_max = np.log(df.max())
  e = df.loc[(df != 0) | (df != np.nan)].min() * 1e-1
  
  # only change e when it zero, fill na
  df_temp = df.replace(0, e)
  df_temp.fillna(df_temp.mean(), inplace=True)
  
  # log transform
  log_transformed = np.log(df_temp) / np.log(log_max)
  return log_transformed, log_max
