import inquirer
from model.monitoramento_de_producao import MonitoramentoProducao
from colorama import init, Fore, Style

init()
cor_mensagem_erro = Fore.RED
cor_mensagem_ok = Fore.GREEN

monitoramento_producao = MonitoramentoProducao()
def run():
    while True:
        perguntas = [
                    inquirer.List('opcao',
                                message='Selecione o que deseja fazer',
                                choices=[
                                        ('1 - Monitorar Produção', '1'),
                                        ('2 - Padronizar Receita', '2'),
                                        ('3 - Cadastrar Cardápio', '3'),
                                        ('4 - Sair do módulo', '4')
                                        ]
                                )
                    ]
        respostas = inquirer.prompt(perguntas)

        # Verifica se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':

            monitoramento_producao.monitorar_producao()

        elif opcao == '2':

            perguntas_registro = [
                                inquirer.Text('prato', message='Digite o nome do prato'),
                                inquirer.Text('instrucoes', message='Digite as instruções de preparo'),
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            prato = respostas_registro['prato']
            instrucoes = respostas_registro['instrucoes']
            
            monitoramento_producao.padronizar_receita_instrucao(prato, instrucoes)
            
        elif opcao == '3':
            perguntas_registro = [
                                inquirer.Text('filial', message='Digite o nome da filial'),
                                inquirer.Text('prato', message='Digite o nome do prato'),
                                inquirer.Text('ingredientes', message='Digite os ingredientes do prato'),
                                inquirer.Text('preco', message='Digite o preço'),
                                ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            filial = respostas_registro['filial']
            prato = respostas_registro['prato']
            insgredientes = respostas_registro['ingredientes']
            preco = respostas_registro['preco']

            monitoramento_producao.cadastrar_cardapio(filial, prato, insgredientes, preco)
        
        elif opcao == '4':
            print(f'{cor_mensagem_ok}Saindo do módulo de monitoramento de produção...{Style.RESET_ALL}')
            break