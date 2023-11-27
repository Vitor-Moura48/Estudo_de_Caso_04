import pandas as pd
from colorama import init, Fore, Style

init()
cor_mensagem_ok = Fore.GREEN

class RelatorioGerencial:
    def __init__(self):
        desempenho_vendas = pd.read_csv("database/controle_estoque.csv")

        colunas = desempenho_vendas.columns

        print()
        for _,linha in desempenho_vendas.iterrows():
            for coluna in colunas:
                valor = linha[coluna]
                print(f"{cor_mensagem_ok}{coluna}: {valor}{Style.RESET_ALL}", end=' ')
            print(' \n')