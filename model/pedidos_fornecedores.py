import csv
import os
import smtplib
import email.message

class Fornecedores:
    def __init__(self):
        self.nome = ''
        self.fornecedores = {}
        
        # Verificação se existe o arquivo
        if os.path.isfile('database/pedidos_fornecedores.csv'):
            with open('database/pedidos_fornecedores.csv', 'a', newline='') as arquivo:
                escritor = csv.writer(arquivo)
        else:
            with open('database/pedidos_fornecedores.csv', 'a', newline='') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(['Filial', 'Categoria', 'Quantidade para pedir'])

        if os.path.isfile('database/fornecedores.csv'):
            with open('database/pedidos_fornecedores.csv', 'a', newline='') as arquivo:
                escritor1 = csv.writer(arquivo)
        else:
            with open('database/fornecedores.csv', 'a', newline='') as arquivo:
                escritor1 = csv.writer(arquivo)
                escritor1.writerow(['Nome', 'Categoria'])
    
    def cadastro_fornecedores(self):
        while True:
            self.nome = input("Nome do fornecedor: ").strip()
            print('''
                  [ 1 ] Alimentos e bebidas
                  [ 2 ] Enxoval, utensílios e uniforme
                  [ 3 ] Equipamentos
                  [ 4 ] Energético
                  ''')
            tipos_fornecedores = int(input("Qual a categoria desse fornecedor? "))

            if tipos_fornecedores == 1:
                tipos_fornecedores = "Alimentos e bebidas"
                self.fornecedores[self.nome] = tipos_fornecedores 
            
            elif tipos_fornecedores == 2:
                tipos_fornecedores = "Enxoval, utensílios e uniforme"
                self.fornecedores[self.nome] = tipos_fornecedores 

            elif tipos_fornecedores == 3:
                tipos_fornecedores = "Equipamentos"
                self.fornecedores[self.nome] = tipos_fornecedores 

            elif tipos_fornecedores == 4:
                tipos_fornecedores = "Energético"
                self.fornecedores[self.nome] = tipos_fornecedores 
            
            else:
                print("Operação não concluída!")

            resp_gerente = input("Deseja continuar o cadastro de fornecedores? [S/N]").upper().strip()[0]

            if resp_gerente == "N":
                break
        
        print("Lista dos fornecedores cadastrados")
        print(self.fornecedores)
            
        self.salvar_fornecedores()
        
    
    def salvar_fornecedores(self):     
        with open("database/fornecedores.csv", 'a',newline='') as arquivo_fornecedores:
            escritor =  csv.writer(arquivo_fornecedores)
            for nome, categoria in self.fornecedores.items():
                escritor.writerow([nome, categoria])

    def ler_fornecedores_cadastrados(self):
        with open("database/fornecedores.csv", "r",newline='') as arquivo_fornecedores:
            leitor = csv.reader(arquivo_fornecedores)
            print(leitor)
    
    # PEDIDOS
    def ler_controle_estoque(self):
        pedidos = []
        quantidade_para_repor = 10
        with open("database/avisos.csv", "r", newline='') as arquivo_estoque:
            leitor = csv.reader(arquivo_estoque)
            next(leitor)
            for coluna in leitor:
                pedidos.append([coluna[0],coluna[1],quantidade_para_repor]) 
            return pedidos
                    
    def gerar_pedidos_automaticos(self):
        pedidos = self.ler_controle_estoque()
        # função para enviar os pedidos aos fornecedores
        self.enviar_pedidos(pedidos)

    def enviar_pedidos(self, pedidos):
        with open("database/pedidos_fornecedores.csv", 'a', newline='') as arquivo_pedidos:
            escritor = csv.writer(arquivo_pedidos)
            escritor.writerows(pedidos)

        # Email para avisar o gerente sobre a necessidade de reabastecimento
        self.enviar_email_gerente()
        print("Alerta enviado ao gerente.")
    
    def enviar_email_gerente(self):
        corpo_email = """
        <p>Olá Gerente</p>
        <p>Veja os pedidos de reabastecimento! </p>
        """

        msg = email.message.Message()
        msg['Subject'] = 'Necessidade de reabastecimento'
        msg['From'] = 'senhorremetente@gmail.com'
        msg['To'] = 'senhorremetente@gmail.com'
        password = 'dbwzmonbmmwabrcz'
        msg.add_header('Content-Type','text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        #login
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    

gereciamento = Fornecedores()
gereciamento.cadastro_fornecedores()
gereciamento.gerar_pedidos_automaticos()
