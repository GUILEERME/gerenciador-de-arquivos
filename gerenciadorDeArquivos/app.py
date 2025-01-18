import os
import datetime
from tkinter.filedialog import askdirectory

print("Bem-vindo ao gerenciador de arquivos!")
print("1 - Visualizar arquivos")
print("2 - Criar pasta ou arquivos")
print(" 3 - Remover pasta ou arquivos")

opcao = int(input("Escolha uma opção:"))

match opcao:

    case 1:
        # Pergunta qual pasta o usuário quer abrir
        pastaSelecionada = askdirectory()
        print(f"Pasta selecionada: {pastaSelecionada}")

        # Lista todos os arquivos da pasta
        listaDeArquivos = os.listdir(pastaSelecionada)
        print("Arquivos na pasta:")
        print(listaDeArquivos)

        # Percorrer arquivos na pasta
        for arquivo in listaDeArquivos:
            print(arquivo)
            nomeCompletoArquivo = os.path.join(pastaSelecionada, arquivo)
            print(nomeCompletoArquivo)

    case 2:
        # Criar pasta de backup
        pastaBackup = input("Crie um nome para a pasta e INSIRA O CAMINHO: ")
        try:
            os.makedirs(pastaBackup)
            print(f"Pasta de backup '{pastaBackup}' criada com sucesso!")
        except FileExistsError:
            print("Erro: A pasta já existe.")
        except Exception as e:
            print(f"Erro ao criar pasta: {e}")

    case _:
        print("Opção inválida. Tente novamente.")