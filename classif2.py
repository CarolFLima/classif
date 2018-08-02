"""
    Classificação a partir de técnicas de Machine Learning
    @author Natalia Lima
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tpot import TPOTClassifier
import pandas as pd
import numpy as np

LABELS = ['CEST PROD', 'DEST AUTOPECAS', 'COD_CST', 'COD CNAE EMIT', 'NCM PROD', 'TIP_FIN_NFE', 'COD CNAE DEST',
              'CFOP PROD']
TARGET = ['CODIFICAÇÃO']

def classificar():
    """
    Extrai dataframe da tabela, converte variáveis de texto para número
    e preenche vazios para -1
    """

    dataframe = pd.read_excel('data/data.xlsx')

    #dataframe.rename({'CODIFICAÇÃO': 'class'}, axis='columns', inplace=True)

    # Binarizando variável com multiplos niveis
    encoder = LabelEncoder()
    classe_label = encoder.fit_transform(dataframe.iloc[:, 0])

    print(classe_label)

    # Binarizando variável com dois niveis
    dest_autopecas = {'N': 0, 'S': 1}
    dataframe['DEST AUTOPECAS'] = [dest_autopecas[item] for item in dataframe['DEST AUTOPECAS']]
    # Preenchendo vazios com valor padrão
    dataframe.fillna(-1, inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(dataframe[LABELS].values, np.array(classe_label), test_size=0.3)

    tpot = TPOTClassifier(generations=5, population_size=50, verbosity=3)
    tpot.fit(X_train, y_train)
    print(tpot.score(X_test, y_test))
    tpot.export('tpot_classif_pipeline.py')


classificar()
