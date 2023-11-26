import pandas as pd
import os
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_mensagem_ok = Fore.GREEN

class MonitoramentoProducao():
    def __init__(self):
        self.caminha_receitas_padronizadas = "database/receitas_padronizadas.csv"
        self.caminho_filial_01 = "database/filial_01.csv"
        self.caminho_filial_02 = "database/filial_02.csv"
        self.caminho_filial_03 = "database/filial_03.csv"

        # cria os arquivos csv, caso eles não existam
        if not os.path.exists(self.caminha_receitas_padronizadas):
            receitas = pd.DataFrame(columns=['nome', 'instrucoes'])
            receitas.to_csv(self.caminha_receitas_padronizadas, index = False)

        if not os.path.exists(self.caminho_filial_01):
            filial = pd.DataFrame(columns=['prato', 'ingredientes', 'preco'])
            filial.to_csv(self.caminho_filial_01, index=False)

        if not os.path.exists(self.caminho_filial_02):
            filial = pd.DataFrame(columns=['prato', 'ingredientes', 'preco'])
            filial.to_csv(self.caminho_filial_02, index=False)

        if not os.path.exists(self.caminho_filial_03):
            filial = pd.DataFrame(columns=['prato', 'ingredientes', 'preco'])
            filial.to_csv(self.caminho_filial_03, index=False)
    
    # busca o arquivo de estoque (não está completo)
    def monitorar_producao(self):
        try:
            estoque = pd.read_csv("databese/controle_estoque.csv")
        except:
            estoque = pd.DataFrame()
        
        if not estoque.empty:
            print(estoque.to_csv(index=False))
        else:
            print(f"{cor_mensagem_erro}O estoque está vazio!{Style.RESET_ALL}\n")

    # adiciona a receita de um produto se ela não estiver cadastrada
    def padronizar_receita_instrucao(self, nome_do_prato, instrucoes):
        try:
            receitas = pd.read_csv(self.caminha_receitas_padronizadas)
        except:
            receitas = pd.DataFrame()

        # adiciona se o prato não foi cadastrado ainda
        if receitas.empty or nome_do_prato not in receitas['nome'].values:
            nova_receita = pd.DataFrame({'nome': [nome_do_prato], 'instrucoes': [instrucoes]})

            # adiciona o novo prato no arquivo
            nova_receita.to_csv(self.caminha_receitas_padronizadas, mode='a', index = False, header=False)

            print(f"\n{cor_mensagem_ok}Padronizando Receita...{Style.RESET_ALL}\n")

        else:
            print(f"\n{cor_mensagem_erro}A receita já foi cadastrada!{Style.RESET_ALL}\n")    
    
    # adiciona um novo prato ao cardapio (não está completo)
    def cadastrar_cardapio(self, filial, prato, ingredientes, preco):
        try:
            cardapio_filial = pd.read_csv(f"database/{filial}.csv")
        except:
            print(f"\n{cor_mensagem_erro}Essa filial não existe!{Style.RESET_ALL}\n")
            return 0
        
        if cardapio_filial.empty or prato not in cardapio_filial['prato'].values:
            novo_prato = pd.DataFrame({'prato': [prato], 'ingredientes': [ingredientes], 'preco': [preco]})
            novo_prato.to_csv(f"database/{filial}.csv", mode='a', index=False, header=False)

            print(f"\n{cor_mensagem_ok}Cadastrando Prato...{Style.RESET_ALL}\n")
        
        else:
            print(f"{cor_mensagem_erro}Prato já foi cadastrado!{Style.RESET_ALL}\n")
        