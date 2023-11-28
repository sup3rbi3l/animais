


class animal():
    
    
    def __init__(self,nome,tamanhoComprimento, n_de_patas, cor, ambiente):
        
        self.nome = nome
        self.tamanhoComprimento = tamanhoComprimento
        self.n_de_patas = n_de_patas
        self.cor = cor
        self.ambiente = ambiente
        
        
    def cria_animal():
        nome = input('digite o nome:')
        tamanho = input('digite o tamanho:')
        patas = input('digite o numero de patas:')
        cor = input('digite a cor:')
        ambiente = input('digite o ambiente:')
        
        return nome,tamanho,patas,cor,ambiente
    def exibe_dados_pai(self):
        print('Nome:',self.nome)
        print('TamanhoComprimento:',self.tamanhoComprimento)
        print('nº_de_patas:',self.n_de_patas)
        print('Ambiente:',self.ambiente)