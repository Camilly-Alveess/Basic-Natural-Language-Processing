from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def resumo_automatico(texto):
    if len(texto) == 0:
        return None
    parser = PlaintextParser.from_string(texto, Tokenizer('portuguese'))
    resumidor_lsa = LsaSummarizer()
    resumo = resumidor_lsa(parser.document, 3)
    resumo_texto = "\n".join(map(str, resumo))
    return resumo_texto
