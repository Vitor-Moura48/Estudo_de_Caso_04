import pandas as pd
import os

class ControleEstoque():
    def __init__(self):
        self.controle_estoque = 'controle_estoque.csv'
        self.avisos = 'avisos.csv'

        if os.path.isfile(self.controle_estoque):
            # Se o arquivo existir, carregue o DataFrame do arquivo CSV
            self.df = pd.read_csv(self.controle_estoque)
        else:
            # Se o arquivo não existir, crie um DataFrame inicial com todas as filiais e quantidades zeradas
            filiais = [
                {'Filial': 'Filial 1', 'Alimentos': 26, 'Bebidas': 50,'Utensilios': 12, 'Uniforme':12,'Equipamentos': 18, 'Energetico': 10},
                {'Filial': 'Filial 2', 'Alimentos': 27, 'Bebidas': 16,'Utensilios': 12, 'Uniforme':12,'Equipamentos': 13, 'Energetico': 12},
                {'Filial': 'Filial 3', 'Alimentos': 17, 'Bebidas': 18,'Utensilios': 12, 'Uniforme':12,'Equipamentos': 23, 'Energetico': 6}
            ]
            self.df = pd.DataFrame(filiais)
            
            self.df.to_csv(self.controle_estoque, index=False)

        if os.path.isfile(self.avisos):
            self.df2 = pd.read_csv(self.avisos)
            
        else:
            self.df2 = pd.DataFrame(columns=['Filial', 'Categoria'])
            
            self.df2.to_csv(self.avisos, index=False)

    def diminuir_estoque(self):
        print(f'{self.df}\n')

        filial = input('-Filial 1\n-Filial 2\n-Filial 3\nQual a Filial deseja atualizar? ')
        
        coluna = input('\n-Alimentos\n-Bebidas\n-Utensilios\n-Uniforme\n-Equipamentos\n-Energetico\nQual o tipo de produto? ')

        quantidade = int(input('Qual a quantidade que deseja retirar? '))
        
        # Atualizando o estoque:
        self.df.loc[self.df['Filial'] == filial, coluna] -= quantidade

        print(f'\n{self.df}')

        # Verificando se o estoque está abaixo do limite:
        estoque_atualizado = self.df.loc[self.df['Filial'] == filial, coluna].values[0]

        if estoque_atualizado < 5:
            print(f'AVISO: O estoque de {coluna} na {filial} está abaixo do limite de 5 unidades!')
            aviso = {'Filial': filial, 'Categoria': coluna, 'Quantidade': estoque_atualizado}
            self.df2 = pd.concat([self.df2, pd.DataFrame([aviso])], ignore_index=True)
            self.df2.to_csv(self.avisos, index=False)

        self.df.to_csv(self.controle_estoque, index=False)

# Criar uma instância da classe ControleEstoque
ger = ControleEstoque()

# Chamar o método diminuir_estoque
ger.diminuir_estoque()
