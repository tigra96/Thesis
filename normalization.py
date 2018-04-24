import pymorphy2

from bs4 import BeautifulSoup as BS

def normalization(df):

    df['Post'] = df['body'].apply(
        lambda x: '.'.join(content.text.lower() for content in BS(x).find_all(['p', 'li', 'h1'])))

    df['Post_norm'] = df['Post'].apply(lemmatization)

    return df

def lemmatization(name):

    morph = pymorphy2.MorphAnalyzer()
    
    letters = [i for i in 'йцукенгшщзхъфывапролджэёячсмитьбю .,']
    name = name.replace('.', '. ').replace(',', ', ')
    
    name = ''.join(i for i in name if i in letters)
    name = name.replace('.', '').replace(',', '')
    
    name =  ' '.join([morph.parse(i)[0].normal_form for i in name.split(' ')])
    name += ' '

    return name