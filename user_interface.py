from tkinter import messagebox, simpledialog, Tk

def perguntar_usuario():
    root = Tk()
    root.withdraw()  
    root.wm_geometry('800x600')  
    resposta = simpledialog.askstring("Inserir Texto", "Caso deseje inserir um texto manualmente, insira (M) ou deseja carregar de um arquivo de texto, insira (A)?")
    return resposta.upper()
