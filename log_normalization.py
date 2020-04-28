import numpy as np

def log_normal_df(df):
    # nobs, mx, mu, var, skew, kurt = stats.describe(log_transformed)
    # get log normalization fit parameters: Log-Max
    # https://towardsdatascience.com/transforming-skewed-data-73da4c2d0d16
    # convert df into log normalization df
    log_max = np.log(df.max())
    e = df.loc[df != 0].min() * 1e-1
    # only change e when data is zero
    df_temp = df.replace(0, e)
    log_transformed = np.log(df_temp) / np.log(log_max)
    return log_transformed, log_max
