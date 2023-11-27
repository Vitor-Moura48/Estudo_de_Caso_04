import inquirer
from model.controle_estoque import ControleEstoque

controle_estoque = ControleEstoque()

def run():
   while True:
    perguntas = [
        inquirer.List('opcao',
                      message="Escolha uma opção",
                      choices=[
                            ('1 - Diminuir no Estoque da Filial Desejada', '1'),
                            ('2 - Receber o Estoque', '2'),
                            ('3 - Sair do Módulo', '3')
                      ])]

    
    respostas = inquirer.prompt(perguntas)

    opcao = respostas['opcao']

    if opcao == '1':
        controle_estoque.diminuir_estoque()
    elif opcao == '2':
        controle_estoque.receber_no_estoque()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.") 


