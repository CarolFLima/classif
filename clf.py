import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" % (topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))
        f.write("Topic %d:" % (topic_idx))
        f.write(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

#dataframe = pd.read_csv('data/teste.csv')
print("Começou")
dataframe = pd.read_csv('data/difal.csv')
print("Terminou")

dataframe.fillna(" ", inplace=True)

# Extração com TF-IDF pra decomposição no NMF
#tfidf_vectorizer = TfidfVectorizer()
#tfidf = tfidf_vectorizer.fit_transform(dataframe['item.desc'])
#tfidf_feature_names = tfidf_vectorizer.get_feature_names()
#print(tfidf_feature_names)

# Extração com o count vectorizer pra o LDA
tf_vectorizer = CountVectorizer()
tf = tf_vectorizer.fit_transform(dataframe['item.desc'])
tf_feature_names = tf_vectorizer.get_feature_names()
#print(tf_feature_names)

no_topics = 100

# Run NMF
#nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5,
                                learning_method='online', learning_offset=50.,random_state=0).fit(tf)

f = open("resultados.txt", "w")

no_top_words = 10
#display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)
