from tkinter import Tk
from tkinter.filedialog import askopenfilename

def carregar_arquivo():
    root = Tk()
    root.withdraw()  
    root.wm_geometry('500x500')  
    arquivo = askopenfilename()  
    if not arquivo:
        return None
    with open(arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto
