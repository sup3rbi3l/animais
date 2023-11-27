




class Cliente:

    def __init__(self, nome,telefone,endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        
    def exibe_dados_pai(self):
        print('Nome:',self.nome)
        print('Telefone:',self.telefone)
        print('Endereço:',self.endereco)
    
    
class ClienteFisico(Cliente):
    
    
    def __init__(self, nome,telefone,endereco,cpf):
        super().__init__(nome,telefone,endereco)
        self.cpf = cpf
    def exibir_dados_filho(self):
        super().exibe_dados_pai()
        print('CPF',self.cpf)
        

class ClienteJuridico(Cliente):
    
    
    def __init__(self, nome,telefone,endereco,cnpj):
        super().__init__(nome,telefone,endereco)
        self.cnpj = cnpj
    def exibir_dados_filho(self):
        super().exibe_dados_pai( )
        print('CNPJ',self.cnpj)
        

    def __init__(self, nome,telefone,endereco,cnpj):
        super().__init__(nome,telefone,endereco)
        self.cnpj = cnpj
    def exibir_dados_filho(self):
        super().exibe_dados_pai()
        print('CNPJ',self.cnpj)
        
cliente1 = ClienteFisico('gab','12735175312','rua duque de caxas',91263826186127-1268)


cliente1.exibir_dados_filho()