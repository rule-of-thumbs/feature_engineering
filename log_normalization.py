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
  if pd.isnull(df).any():
    return df, None
  if df.loc[(df != 0) & (~pd.isnull(df))].max() == 0:
    return df, None
  if df[df < 0].any():
    # log(negative) returns np.nan
    return df, None
  if (df == 0).all():
    return df, None
  # get base
  base = np.log(df.loc[(df != 0) & (~pd.isnull(df))].max())
  e = df.loc[(df != 0) & (~pd.isnull(df))].min() * 1e-1
  
  # only change e when it zero, fill na
  df_temp = df.copy()
  df_temp.replace(0, e, inplace=True)
  df_temp.fillna(df_temp.median(), inplace=True)
  
  # log transform
  log_transformed = np.log(df_temp) / np.log(base)
  return log_transformed, base
