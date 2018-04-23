import pandas as pd

KAPPA = 5

def create_features(df):
    whole_text = df['Post_norm'].sum()

    features = list(set(whole_text.split(' ')))

    d = {}

    for feat in features:
        num_in_text = whole_text.count(feat)

        if num_in_text > KAPPA & len(feat) > 1:
            d[feat] = num_in_text

    return d