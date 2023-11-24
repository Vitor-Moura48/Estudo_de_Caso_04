import pandas as pd
import os

class ControleEstoque():
    def __init__(self):
        self.controle_estoque = 'controle_estoque.csv'

        if os.path.isfile(self.controle_estoque):
            # Se o arquivo existir, carregue o DataFrame do arquivo CSV
            self.df = pd.read_csv(self.controle_estoque)
        else:
            # Se o arquivo não existir, crie um DataFrame inicial com todas as filiais e quantidades zeradas
            filiais = [
                {'Filial': 'Filial 1', 'Alimentos': 26, 'Bebidas': 50, 'Enxoval': 65, 'Utensilios': 20, 'Equipamentos': 18, 'Energetico': 10},
                {'Filial': 'Filial 2', 'Alimentos': 27, 'Bebidas': 16, 'Enxoval': 23, 'Utensilios': 46, 'Equipamentos': 13, 'Energetico': 12},
                {'Filial': 'Filial 3', 'Alimentos': 17, 'Bebidas': 18, 'Enxoval': 20, 'Utensilios': 21, 'Equipamentos': 23, 'Energetico': 6}
            ]
            self.df = pd.DataFrame(filiais)
            
            self.df.to_csv(self.controle_estoque, index=False)

    def diminuir_estoque(self):
        print(f'{self.df}\n')

        filial = input('-Filial 1\n-Filial 2\n-Filial 3\nQual a Filial deseja atualizar? ')

        coluna = input('\n-Alimentos\n-Bebidas\n-Enxoval\n-Utensilios\n-Equipamentos\n-Energetico\nQual o tipo de produto? ')

        quantidade = int(input('Qual a quantidade que deseja retirar? '))
        
        # Atualizando o estoque:
        self.df.loc[self.df['Filial'] == filial, coluna] -= quantidade

        print(f'\n{self.df}')

        # Verificando se o estoque está abaixo do limite:
        estoque_atualizado = self.df.loc[self.df['Filial'] == filial, coluna].values[0]
        if estoque_atualizado < 5:
            print(f'AVISO: O estoque de {coluna} na {filial} está abaixo do limite de 5 unidades!')
            
        self.df.to_csv(self.controle_estoque, index=False)

# Criar uma instância da classe ControleEstoque
ger = ControleEstoque()

# Chamar o método diminuir_estoque
ger.diminuir_estoque()