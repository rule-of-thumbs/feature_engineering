from scipy.stats import entropy

# df, sequence > bool(regular), amount(regular)
def regularity_df(df, columns, boolean=False):
    # columns의 순서가 중요하다
    df_temp = df[columns].copy()
    if boolean == True:
    df_temp = df_temp.astype(bool)
  
    df_sum = df_temp.sum(axis=1)
    frac = df_temp.div(df_sum.iloc[0], axis='columns')
  
    return entropy(frac.T)
