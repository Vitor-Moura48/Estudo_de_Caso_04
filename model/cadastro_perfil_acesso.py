import pandas as pd
import inquirer

class CadastrarPerfilAcesso:
    def __init__(self):
        self.dados = {
            'perfis_acesso': pd.DataFrame(columns=['nome', 'areas_acesso']),
            'produtos': pd.DataFrame(columns=['nome', 'tipo', 'quantidade', 'preco']),
            'estoque': pd.DataFrame(columns=['nome', 'tipo', 'quantidade', 'preco']),
        }

    def criar_perfil_acesso(self):
        perguntas = [
            inquirer.Text('nome', message='Nome do perfil de acesso:'),
            inquirer.List('areas_acesso', message='Áreas de acesso:', choices=['Cadastro de Produtos', 'Controle de Estoque']),
        ]
        respostas = inquirer.prompt(perguntas)

        nome = respostas['nome']
        areas_acesso = respostas['areas_acesso']
        perfil = pd.DataFrame({'nome': [nome], 'areas_acesso': [areas_acesso]})

        self.dados['perfis_acesso'] = pd.concat([self.dados['perfis_acesso'], perfil], ignore_index=True)
        
        print('Perfil de acesso criado com sucesso.')

    def cadastrar_produto(self):
        questions = [
            inquirer.Text('nome', message='Nome do produto:'),
            inquirer.Text('tipo', message='Tipo do produto:'),
            inquirer.Text('quantidade', message='Quantidade do produto:'),
            inquirer.Text('preco', message='Preço do produto:'),
        ]

        answers = inquirer.prompt(questions)
        produto = pd.DataFrame([{
            'nome': answers['nome'],
            'tipo': answers['tipo'],
            'quantidade': answers['quantidade'],
            'preco': answers['preco'],
        }])
        self.dados['produtos'] = pd.concat([self.dados['produtos'], produto], ignore_index=True)

        print('Produto cadastrado com sucesso.')

    def adicionar_produto_estoque(self):
        questions = [
            inquirer.Text('nome_produto', message='Nome do produto:'),
            inquirer.Text('tipo_produto', message='Tipo do produto:'),
            inquirer.Text('quantidade_produto', message='Quantidade do produto:'),
            inquirer.Text('preco_produto', message='Preço do produto:'),
        ]

        answers = inquirer.prompt(questions)
        produto = pd.DataFrame([{
            'nome': answers['nome_produto'],
            'tipo': answers['tipo_produto'],
            'quantidade': answers['quantidade_produto'],
            'preco': answers['preco_produto'],
        }])
        self.dados['estoque'] = pd.concat([self.dados['estoque'], produto], ignore_index=True)

        print('Produto adicionado ao estoque com sucesso.')

    def salvar_dados_csv(self):
        for nome, df in self.dados.items():
            df.to_csv(f'database/{nome}.csv', index=False, mode='a', header=False)

        print('Dados salvos em CSV com sucesso.')

    def menu_principal(self):
        while True:
            opcoes = [
                inquirer.List('opcao', message='Escolha uma opção:', choices=['Criar Perfil de Acesso', 'Cadastrar Produto', 'Adicionar Produto ao Estoque', 'Salvar e Sair']),
            ]

            escolha = inquirer.prompt(opcoes)['opcao']

            if escolha == 'Criar Perfil de Acesso':
                self.criar_perfil_acesso()
            elif escolha == 'Cadastrar Produto':
                self.cadastrar_produto()
            elif escolha == 'Adicionar Produto ao Estoque':
                self.adicionar_produto_estoque()
            elif escolha == 'Salvar e Sair':
                self.salvar_dados_csv()
                break



