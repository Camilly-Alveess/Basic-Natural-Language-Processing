import spacy_utils
import gensim_utils
import sumy_utils
import file_utils
import user_interface
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import relatorio_utils

def main():
    try:
        # Carregar o modelo spaCy
        modelo = spacy_utils.carregar_modelo()

        # Carregar texto do usuário ou do arquivo
        while True:
            opcao = user_interface.perguntar_usuario()
            if opcao == "M":
                texto = simpledialog.askstring("Inserir Texto", "Digite o texto:                                                                                                                                      ")
                if texto and texto.strip():  # Verifica se o texto não está vazio
                    break
                else:
                    messagebox.showwarning("Aviso", "O texto não pode estar vazio. Por favor, insira um texto válido.")
            elif opcao == "A":
                texto = file_utils.carregar_arquivo()
                if texto is not None:  # Verifica se um arquivo foi selecionado
                    break
                else:
                    messagebox.showwarning("Aviso", "Nenhum arquivo selecionado. Por favor, selecione um arquivo válido.")
            else:
                messagebox.showwarning("Aviso", "Opção inválida. Por favor, escolha 'M' ou 'A'.")

        # Tokenização
        tokens = spacy_utils.tokenizacao(texto, modelo)

        # Identificação de Entidades Nomeadas (NER)
        entidades = spacy_utils.identificar_entidades(texto, modelo)

        # Análise de Sentenças
        sentencas = spacy_utils.analise_sentencas(texto, modelo)

        # Extração de Tópicos
        textos_para_topicos = [sentenca.split() for sentenca in sentencas] 
        topicos = gensim_utils.extrair_topicos(textos_para_topicos)

        # Resumo Automático
        resumo = sumy_utils.resumo_automatico(texto)

        # Montar relatório final
        relatorio = relatorio_utils.montar_relatorio(tokens, entidades, sentencas, topicos, resumo)
        print(relatorio)

        # Gerar PDF com o relatório
        relatorio_utils.gerar_pdf(relatorio)
    
    except Exception as e:
        print(f"Ocorreu um erro durante a execução: {e}")

if __name__ == "__main__":
    main()
