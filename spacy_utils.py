import spacy

def carregar_modelo():
    return spacy.load('pt_core_news_sm')

def tokenizacao(texto, modelo):
    doc = modelo(texto)
    tokens = [token.text for token in doc if not token.is_punct] 
    return tokens

def identificar_entidades(texto, modelo):
    doc = modelo(texto)
    entidades = [(entidade.text, entidade.label_) for entidade in doc.ents]
    return entidades

def analise_sentencas(texto, modelo):
    doc = modelo(texto)
    sentencas = [sentenca.text for sentenca in doc.sents]
    return sentencas
