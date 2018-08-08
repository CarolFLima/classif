import pandas as pd

# Filtra e importa pra o csv
dataframe = pd.read_excel('data/difal.xlsx')
#
dataframe['item.desc'] = dataframe['item.desc'].str.replace('-', ' ')
dataframe['item.desc'] = dataframe['item.desc'].str.replace('[^ a-zA-Z]', '')
dataframe['item.desc'] = dataframe['item.desc'].str.replace(' +', ' ')
dataframe['item.desc'] = dataframe['item.desc'].str.lower()
df1 = dataframe['item.desc']
df1.to_csv('data/difal.csv')