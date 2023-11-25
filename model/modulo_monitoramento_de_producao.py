import pandas as pd
import os

class MonitoramentoProducao():
    def __init__(self):
        self.caminho_estoque = "database/estoque.csv"
        self.caminha_receitas_padronizadas = "database/receitas_padronizadas.csv"
        self.caminho_filial_01 = "database/filial_01.csv"
        self.caminho_filial_02 = "database/filial_02.csv"
        self.caminho_filial_03 = "database/filial_03.csv"

        # cria os arquivos csv, caso eles não existam
        if not os.path.exists(self.caminha_receitas_padronizadas):
            receitas = pd.DataFrame({'nome': ['inicializacao'],
                                    'instrucoes': ['.']})
            receitas.to_csv(self.caminha_receitas_padronizadas, index = False)

        if not os.path.exists(self.caminho_filial_01):
            filial = pd.DataFrame({'prato': [''],
                                   'ingrediente': '',
                                   'preco': [0]})
            filial.to_csv(self.caminho_filial_01, index=False)
        if not os.path.exists(self.caminho_filial_02):
            filial = pd.DataFrame({'prato': [''],
                                   'ingrediente': '',
                                   'preco': [0]})
            filial.to_csv(self.caminho_filial_02, index=False)
        if not os.path.exists(self.caminho_filial_03):
            filial = pd.DataFrame({'prato': [''],
                                   'ingrediente': [''],
                                   'preco': [0]})
            filial.to_csv(self.caminho_filial_03, index=False)
    
    # busca o arquivo de estoque (não está completo)
    def monitorar_producao(self):
        try:
            estoque = pd.read_csv(self.caminho_estoque)
        except:
            estoque = pd.DataFrame()
        
        print(estoque.to_csv(index=False))

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
            if 'inicializacao' in receitas['nome'].values:
                receitas = receitas[receitas['nome'] != 'inicializacao']
                receitas.to_csv(self.caminha_receitas_padronizadas, index = False)
                nova_receita.to_csv(self.caminha_receitas_padronizadas, mode='a', index = False, header=False)

        else:
            print("O prato já foi cadstrado!")    
    
    # adiciona um novo prato ao cardapio (não está completo)
    def cadastrar_cardapio(self, filial, prato, ingredientes, preco):
        try:
            filial = pd.read_csv(f"database/{filial}")
        except:
            filial = pd.DataFrame()
        
        if filial.empty or prato not in filial:
            filial['prato'] = [prato]
            filial['ingradientes'] = ingredientes
            filial['preco'] - preco

            filial.to_csv(f"database/{filial}", index=False, header=False)
        
        else:
            print("Prato já foi cadastrado!")
        
teste = MonitoramentoProducao()
teste.padronizar_receita_instrucao('arroz_picante', 'Misture o 300g de arroz com 4 pimentas, adicione um pouco de sal')