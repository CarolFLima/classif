import pandas as pd

# Filtra e importa pra o csv
dataframe = pd.read_excel('data/difal.xlsx')
#
dataframe['item.desc'] = dataframe['item.desc'].str.replace('-', ' ')
dataframe['item.desc'] = dataframe['item.desc'].str.replace('[^ a-zA-Z]', '')
dataframe['item.desc'] = dataframe['item.desc'].str.replace(' +', ' ')
dataframe['item.desc'] = dataframe['item.desc'].str.lower()
print(dataframe['item.desc'])
dataframe.to_csv('data/difal.csv')
print(dataframe.head(10))
print(dataframe.tail(10))
