import pandas as pd

df = pd.read_csv('../1912_poniedziałekRW/dane/homes.csv')

df.to_json('dane/domki.json')