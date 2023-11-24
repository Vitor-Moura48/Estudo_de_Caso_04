class Fornecedores:
    def __init__(self):
        self.nome = ''
        self.fornecedores = {}
    
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
        for k, v in self.fornecedores.items():
            print(f"Nome: {k}")
            print(f"Categoria: {v}\n")

     

gereciamento = Fornecedores()
gereciamento.cadastro_fornecedores()
