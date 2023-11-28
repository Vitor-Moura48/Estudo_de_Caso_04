import pandas as pd
                                 #Gestão De Funcionários


######################################################################################

#    RF01  e RF04

# Filial  - 01
# Visualizar equipe:
# Escalas de trabalho:
# Registrar hora:
# Avaliar desempenho:

def gerenciar_equipe():
    print('Filial 1\n', 'Filial 2\n' , 'Filial 3')
    numero_da_filial = int(input('Selecione a filial:'))
    # primeiro selecionar a filial


    if (numero_da_filial == 1): # Filial 1

        # Dados da equipe
        f1_dados_equipe = {
            'id': [1, 2, 3, 4, 5],
            'cargo': ['Chefe', 'Cozinhero', 'Gerente', 'Garçon', 'Caixa'],
            'nome': ['João', 'Maria', 'Carlos', 'Ana', 'Pedro'],
            'carga_horaria': [40, 35, 40, 30, 35],
            'avaliacao_individual': [4.5, 3.8, 4.9, 4.2, 3.5]
        }

        # Criar DataFrame com os dados da equipe
        f1_equipe_df = pd.DataFrame(f1_dados_equipe)

        # Exibir a tabela
        print(f1_equipe_df)

    ####################################################################################################################

    elif (numero_da_filial == 2): # Filial 2

        # Dados da equipe
        f2_dados_equipe = {
            'id': [1, 2, 3, 4, 5],
            'cargo': ['Chefe', 'Cozinhero', 'Gerente', 'Garçon', 'Caixa'],
            'nome': ['João', 'Maria', 'Carlos', 'Ana', 'Pedro'],
            'carga_horaria': [40, 35, 40, 30, 35],
            'avaliacao_individual': [4.5, 3.8, 4.9, 4.2, 3.5]
        }

        # Criar DataFrame com os dados da equipe
        f2_equipe_df = pd.DataFrame(f2_dados_equipe)

        # Exibir a tabela
        print(f2_equipe_df)

    #################################################################################


    elif (numero_da_filial == 3): # Filial 3

        # Dados da equipe
        f3_dados_equipe = {
            'id': [1, 2, 3, 4, 5],
            'cargo': ['Chefe', 'Cozinhero', 'Gerente', 'Garçon', 'Caixa'],
            'nome': ['João', 'Maria', 'Carlos', 'Ana', 'Pedro'],
            'carga_horaria': [40, 35, 40, 30, 35],
            'avaliacao_individual': [4.5, 3.8, 4.9, 4.2, 3.5]
        }

        # Criar DataFrame com os dados da equipe
        f3_equipe_df = pd.DataFrame(dados_equipe)

        # Exibir a tabela
        print(f3_equipe_df)

                    


    #############################################################################################
#                                         ok +-              falta a função para fazer as alterações:

#                      - marcar ponto - alterar carga horária - alterar cargo - avaliar funcionário - avaliar equipe



        # Escala de trabalho: 

        #      Turno: manhã ?

        #  ID      Cargo      Nome        Carga Horária(D)    Ava individual
        # 8u89      Chef     Carlos            8H              0 ~ 10
        # Produção:
        # Avaliação da equipe: (Media dos membros da equipe)
        # Avaliação do Gerente:
        
        # Deseja fazer alguma modificação?

        # Se for na nota do funcionário
        # Se for no cargo
        # Se for na carga horária
'''            Informação importante                   '''
#             deve ter um contador para a quantidade total
# id_existente = 3
equipe_df = pd.DataFrame(dados_equipe)
# Dependendo da filial a variavel equipe_df vai mudar para:
# f1_equipe_df 
# f2_equipe_df 
# f3_equipe_df
#       e tambem dados_equipe:
# f1_dados_equipe 
# f2_dados_equipe 
# f3_dados_equipe
                              # Funções:
def alterar_cargo(id_funcionario, novo_cargo):
     equipe_df.loc[equipe_df['id'] == id_funcionario, 'cargo'] = novo_cargo
#                   ^^^^ fx_
def alterar_nota(id_funcionario, nova_nota):
      equipe_df.loc[equipe_df['id'] == id_funcionario, 'avaliacao_individual'] = nova_nota
#                   ^^^^ fx_
def alterar_carga_horaria(id_funcionario, nova_carga_horaria):
     equipe_df.loc[equipe_df['id'] == id_funcionario, 'carga_horaria'] = nova_carga_horaria
#                   ^^^^ fx_
def verificar_id_existente(id_funcionario):
     return any(equipe_df['id'] == id_funcionario)
#                   ^^^^ fx_

                                     # Alteração do cargo:

while True:
    print('\n'*5)
    # fx_equipe_df:
    # f == (filial)
    # x == 1,2 ou 3
    print(fx_equipe_df)
    id_do_funcionario = int(input('Selecione o ID do funcionário:'))
    
    if verificar_id_existente(id_existente):
        print(f"O ID {id_existente} existe na tabela.")
        print('\n'*2)
        print('1 - Chefe\n 2 - Cozinheiro\n 3 - Garçon\, 4 - Caixa')
        novo_cargo = int(input("Escola o novo cardo para que seja algerado:"))

        if (novo_cargo == 1) :
            novo_cargo = 'chefe'
            alterar_cargo(id_do_funcionario, novo_cargo)
            break

        elif (novo_cargo == 2) :
            novo_cargo = 'Cozinheiro'
            alterar_cargo(id_do_funcionario, novo_cargo) 
            break

        elif (novo_cargo == 3) :
            novo_cargo = 'Garçon'
            alterar_cargo(id_do_funcionario, novo_cargo)
            break

        elif (novo_cargo == 4) :
            novo_cargo = 'Caixa'
            alterar_cargo(id_do_funcionario, novo_cargo)

            break
        else:
            print('\n'*5)
            print('ops, ERRo', '\n'*5 , 'Tente novamente:')

    else:
        print(f"O ID {id_existente} não existe na tabela.\nTente de novo:")



                                         # Alteração da nota dos funcionários:
while True:
    # fx_equipe_df:
    # f == (filial)
    # x == 1,2 ou 3
    print('\n'*5)
    print(fx_equipe_df)
    id_do_funcionario = int(input('Selecione o ID do funcionário:'))
    if verificar_id_existente(id_existente):
        print(f"O ID {id_existente} existe na tabela.")
        print('\n'*5)
        nova_nota = int(input("Digite a nova nota do funcionário"))
        alterar_nota(id_do_funcionario, nova_nota)
        break
    else:
        print(f"O ID {id_existente} não existe na tabela.")


                                          # Alterar carga horária:

while True:
    # fx_equipe_df:
    # f == (filial)
    # x == 1,2 ou 3
    print(fx_equipe_df)
    print('\n'*5)
    id_do_funcionario = int(input('Selecione o ID do funcionário:'))
    if verificar_id_existente(id_existente):
        print(f"O ID {id_existente} existe na tabela.")
        nova_carga_horaria = int(input("A nova Carga horária semanal:"))
        if (nova_carga_horaria <= 68):
            alterar_carga_horaria(id_do_funcionario , nova_carga_horaria)
            break

        else:
            print('Tá ficando doido? a escravidão já passou!!!')
            print('\n'*5 , 'Seja humano e tente de novo:')
    else:
        print(f"O ID {id_existente} não existe na tabela.")

######################################################################################


#    RF02
# Chat de conversa entre filiais e base logistica:


import time
from threading import Thread

class Mensagem:
    def __init__(self, remetente, destinatario, conteudo):
        self.remetente = remetente
        self.destinatario = destinatario
        self.conteudo = conteudo
        self.timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

class Filial:
    def __init__(self, nome):
        self.nome = nome
        self.mensagens_recebidas = []

    def enviar_mensagem(self, destinatario, conteudo):
        mensagem = Mensagem(self.nome, destinatario, conteudo)
        print(f"{self.nome} enviou mensagem para {destinatario}: {conteudo}")
        return mensagem

    def receber_mensagem(self, mensagem):
        self.mensagens_recebidas.append(mensagem)
        print(f"{self.nome} recebeu mensagem de {mensagem.remetente}: {mensagem.conteudo}")

class BaseLogistica:
    def __init__(self, nome):
        self.nome = nome
        self.mensagens_recebidas = []

    def enviar_mensagem(self, destinatario, conteudo):
        mensagem = Mensagem(self.nome, destinatario, conteudo)
        print(f"{self.nome} enviou mensagem para {destinatario}: {conteudo}")
        return mensagem

    def receber_mensagem(self, mensagem):
        self.mensagens_recebidas.append(mensagem)
        print(f"{self.nome} recebeu mensagem de {mensagem.remetente}: {mensagem.conteudo}")

def simulacao_chat(filial, base_logistica):
    # Filial envia mensagem para a base logística
    mensagem_filial = filial.enviar_mensagem("Base Logística", "Precisamos de mais estoque.")
    base_logistica.receber_mensagem(mensagem_filial)

    # Base logística responde à filial
    mensagem_base_logistica = base_logistica.enviar_mensagem(filial.nome, "Enviaremos mais estoque em breve.")
    filial.receber_mensagem(mensagem_base_logistica)

# Criando instâncias de Filial e BaseLogistica
filial1 = Filial("Filial 1")
filial2 = Filial("Filial 2")
base_logistica = BaseLogistica("Base Logística")

# Simulando o chat entre Filial 1 e Base Logística
simulacao_chat(filial1, base_logistica)

# Simulando o chat entre Filial 2 e Base Logística
simulacao_chat(filial2, base_logistica)




######################################################################################
