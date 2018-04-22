import pandas as pd

from normalization import normalization


def main():
    df = pd.read_excel('body.xlsx')

    df = normalization(df)
    print(df.head())

    return

if __name__ == '__main__':
    main()