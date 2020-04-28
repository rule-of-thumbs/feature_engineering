from scipy.stats import entropy

# df, sequence > bool(regular), amount(regular)
def regularity_df(df, boolean=False):
    # columns의 순서가 중요하다
    df_temp = df.copy()
    if boolean == True:
        df_temp = df_temp.astype(bool)
  
    return entropy(df_temp.T)
