from scipy.stats import entropy

# df, sequence > bool(regular), amount(regular)
def regularity_df(df, columns):
    # columns의 순서 중요하다
    df_temp = df[columns].copy()
    df_sum = df_temp.sum(axis=1)
    frac = df_temp.div(df_sum.iloc[0], axis='columns')
    return entropy(frac.T)

