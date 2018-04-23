import pandas as pd

from fpg_tree      import FPTree
from normalization import normalization
from associative   import create_features

def main():
    df = pd.read_excel('body.xlsx')

    df = normalization(df)

    features = create_features(df)

    for key in list(features.keys()):
        df[key] = df.Post_norm.apply(lambda x: 1 if key in x else 0)

    tree = FPTree()

    for row_num in range(df.shape[0]):
        row = list(df.loc[row_num][df.loc[row_num] == 1].index)
        row_sorted = [j[1] for j in sorted([(features[i], i)
                                            for i in row], reverse=True)]
        if row_sorted:
            tree.add(row_sorted)

    print(tree.root.search('матч'))

    return

if __name__ == '__main__':
    main()