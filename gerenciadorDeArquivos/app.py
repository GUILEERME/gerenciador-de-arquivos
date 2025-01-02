import os
import datetime
from tkinter.filedialog import askdirectory

# Pergunta qual pasta o usuário quer abrir
pastaSelecionada = askdirectory()
print(pastaSelecionada)

# Lista todos os arquivos da pasta
listaDeArquivos = os.listdir(pastaSelecionada)
print(listaDeArquivos)

# Percorrer arquivos na pasta
for arquivo in listaDeArquivos:
    print(arquivo)
    nomeCompletoArquivo = f"{pastaSelecionada} / {arquivo}"
    print(nomeCompletoArquivo)
