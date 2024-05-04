from itertools import zip_longest
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def formatar_tokens(tokens, colunas=4):
    # Organiza os tokens em colunas para melhor legibilidade
    tokens_por_coluna = [tokens[i:i+colunas] for i in range(0, len(tokens), colunas)]
    tokens_formatados = zip_longest(*tokens_por_coluna, fillvalue='')
    tokens_formatados = [', '.join(column) for column in tokens_formatados]
    return '\n'.join(tokens_formatados)

def montar_relatorio(tokens, entidades, sentencas, topicos, resumo):
    # Aqui você pode montar o relatório com os resultados obtidos
    relatorio = "Relatório Final\n\n"

    # Adicione os resultados de cada etapa ao relatório
    relatorio += "Tokenização:\n"
    relatorio += formatar_tokens(tokens)
    relatorio += "\n\n"

    relatorio += "Identificação de Entidades Nomeadas (NER):\n"
    relatorio += "\n".join([f"{entidade[0]} - {entidade[1]}" for entidade in entidades])
    relatorio += "\n\n"

    relatorio += "Análise de Sentenças:\n"
    relatorio += "\n".join(sentencas)
    relatorio += "\n\n"

    relatorio += "Extração de Tópicos:\n"
    if topicos is not None:
        for i, topico in enumerate(topicos):
            relatorio += f"Tópico {i+1}: {topico}\n"
    else:
        relatorio += "Não foi possível extrair tópicos. Certifique-se de que há texto suficiente para análise.\n"
    relatorio += "\n"

    relatorio += "Resumo Automático:\n"
    relatorio += resumo if resumo is not None else "Não foi possível gerar um resumo automático. Certifique-se de que há texto suficiente para análise.\n"

    return relatorio

def gerar_pdf(relatorio):
    # Defina as margens esquerda, inferior, direita e superior
    margem_esquerda = 50
    margem_inferior = 50
    margem_direita = 50
    margem_superior = 750  # Ajuste conforme necessário

    c = canvas.Canvas("relatorio.pdf", pagesize=letter)
    text = c.beginText(margem_esquerda, margem_superior)
    text.setFont("Helvetica", 6)

    # Lógica para quebrar o texto e ajustá-lo às margens
    linhas = relatorio.split('\n')
    for linha in linhas:
        # Verifica se a próxima linha ultrapassa a margem inferior
        if text.getY() - 12 < margem_inferior:
            # Adiciona uma nova página
            c.drawText(text)
            c.showPage()
            c = canvas.Canvas("relatorio.pdf", pagesize=letter)
            text = c.beginText(margem_esquerda, margem_superior)
            text.setFont("Helvetica", 6)
        # Desenha a linha atual
        text.textLine(linha)

    # Desenha o último trecho do texto
    c.drawText(text)
    c.showPage()
    c.save()
