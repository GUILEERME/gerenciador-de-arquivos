import os
import datetime
from tkinter.filedialog import askdirectory

# Pergunta qual pasta o usuário quer abrir
pastaSelecionada = askdirectory()
print(pastaSelecionada)

# Lista todos os arquivos da pasta
os.listdir(pastaSelecionada)