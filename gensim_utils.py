from gensim.corpora import Dictionary
from gensim.models import LdaModel

def extrair_topicos(textos):
    if len(textos) == 0:
        return None
    dicionario = Dictionary(textos)
    corpus = [dicionario.doc2bow(doc) for doc in textos]
    modelo_lda = LdaModel(corpus, num_topics=3, id2word=dicionario, passes=10)
    topicos = []
    for topico in modelo_lda.print_topics():
        topicos.append(topico)
    return topicos
