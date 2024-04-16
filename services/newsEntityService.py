import spacy
import pandas as pd

def extractEntity():
    pln = spacy.load('pt')

    # document processing.
    df = pd.read_csv('financeMainNews.csv')

    text = df['machete'].to_list()
    print('aqui é o texto csv')

    document = pln(text)
    for entity in document.ents:
        print(entity.text, entity.label_)
