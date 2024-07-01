import pandas as pd
import os


def get_data():
    directory = os.path.dirname(__file__)
    df = pd.read_csv(f'{directory}/../data/dict.csv')
    tamil_words = df['Tamil']
    hindi_words = df['Hindi']

    dictionary = {t: h for t, h in zip(tamil_words, hindi_words)}
    return dictionary
