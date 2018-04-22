import pandas as pd

from bs4      import BeautifulSoup as BS

def main():
    df = pd.read_excel('body.xlsx')
    df['Post'] = df.body.apply(
        lambda x: '.'.join(content.text.lower() for content in BS(x).find_all(['p', 'li', 'h1'])))

    return

if __name__ == '__main__':
    main()