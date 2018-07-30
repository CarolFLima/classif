﻿"""
    Classificação a partir de técnicas de Machine Learning
    @author Natalia Lima
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from tpot import TPOTClassifier

import pandas as pd

LABELS = ['CEST PROD', 'DEST AUTOPECAS', 'COD_CST', 'COD CNAE EMIT', 'NCM PROD', 'TIP_FIN_NFE', 'COD CNAE DEST',
              'CFOP PROD']
TARGET = ['CODIFICAÇÃO']

def classificar():
    """
    Extrai dataframe da tabela, converte variáveis de texto para número
    e preenche vazios para -1
    """
    print("Comecei a extrair dataframe")
    dataframe = pd.read_excel('data/data.xlsx')
    print("Terminei")

    dest_autopecas = {'N': 0, 'S': 1}
    dataframe['DEST AUTOPECAS'] = [dest_autopecas[item] for item in dataframe['DEST AUTOPECAS']]
    dataframe.fillna(-1, inplace=True)
    target_dummies = pd.get_dummies(dataframe[TARGET])
    #X_train, X_test, y_train, y_test = multilabel_train_test_split(dataframe[LABELS],target_dummies,
    #                                                               min_count=1,
    #                                                               size=0.3,
    #                                                               seed=123)

    X_train, X_test, y_train, y_test = train_test_split(dataframe[LABELS].values, dataframe[TARGET].values, test_size=0.3)
    #pl = Pipeline(steps=[('clf', DecisionTreeClassifier())])
    #pl.fit(X_train, y_train)
    tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2)
    tpot.fit(X_train, y_train)
    print("%f" % tpot.score(X_test, y_test))
    tpot.export('tpot_classif_pipeline.py')


# def crop_sheet():
#     print("Comecei a extrair dataframe")
#     dataframe = pd.read_excel('data/dataset.xlsx', nrows=30000)
#     print("Terminei")
#     dataframe.to_excel("data/data.xlsx")


classificar()