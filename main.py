import inquirer
from colorama import init, Fore, Style

from model.cadastro_perfil_acesso import CadastrarPerfilAcesso

# questions = [
#     inquirer.Text('username', message='Enter your username:'),
#     inquirer.Password('password', message='Enter your password:')
# ]

# answers = inquirer.prompt(questions)

# username = answers['username']
# password = answers['password']

# print(f'Username: {username}')
# print(f'Password: {password}')



init()

# Função para colorir o texto
def color_text(hex_color):
    hex_color = hex_color.lstrip('#')

    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    return '\033[38;2;{};{};{}m'.format(*rgb_color)

cor_titulo = color_text('EE2E28')
cor_pergunta = Fore.WHITE
cor_resposta = Fore.MAGENTA
cor_mensagem = Fore.YELLOW
cor_mensagem_erro = Fore.RED

try:
    while True:
        print(f'{cor_titulo}╔══════════════════════════════════════════════════════════╗')
        print(f'║                                                          ║')
        print(f'║              🌍 Sabores do Mundo 🌍 🍽️                    ║')
        print(f'║                                            v1.0.0        ║')
        print(f'║                                                          ║')
        print(f'╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n')

        # Menu de opções



        pergunta = [
            inquirer.List('opcao',
                        message=f'Selecione o módulo que deseja acessar',
                        choices=[
                            (f'1 - Módulo de ', '1'),
                            (f'2 - Módulo de Cadastro de Perfil de Acesso', '2'),
                            (f'3 - Módulo de ', '3'),
                            (f'4 - Módulo de Monitoramento e Controle da Produção', '4'),
                            (f'5 - Módulo de ', '5'),
                            (f'6 - Encerrar a Sessão no Sistema', '6')
                        ])
        ]

        respostas = inquirer.prompt(pergunta)

        # Verifique se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        print(f'{cor_titulo}=>{Style.RESET_ALL} Você selecionou a opção: {cor_titulo}{opcao}{Style.RESET_ALL}\n')

        match opcao:
            case '1':
                pass
            case '2':
                sistema = CadastrarPerfilAcesso()
                sistema.menu_principal()
            case '3':
                pass
            case '4':
                from controller.monitoramento_producao_controller import run
                run()
            case '5':
                pass
            case '6':
                print(f'{cor_mensagem}👋 Até mais!{Style.RESET_ALL}\n')
                break
            case _:
                print(f'{cor_mensagem_erro}❌ Ocorreu um erro estranho{Style.RESET_ALL}\n')

except KeyboardInterrupt:
    print(f'{cor_mensagem_erro}❌ O Sistema foi interrompido forçadamente pelo usuário{Style.RESET_ALL}\n')