import inquirer
from model.pedidos_fornecedores import Fornecedores

fornecedores = Fornecedores()

perguntas = [
        inquirer.List('opcao',
                      message="Escolha uma opção",
                      choices=[
                            ('1 - Cadastrar Fornecedor', '1'),
                            ('2 - Listar Fornecedores', '2'),
                            ('3 - Gerar Pedidos', '3'),
                            ('4 - Sair', '4')
                      ]
                      )
]

while True:
    respostas = inquirer.prompt(perguntas)

    opcao = respostas['opcao']

    if opcao == '1':
        fornecedores.cadastro_fornecedores()
    elif opcao == '2':
        fornecedores.ler_fornecedores_cadastrados()
    elif opcao == '3':
        fornecedores.gerar_pedidos_automaticos()
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")
