from _super_animais import animal
    
    
    
class Anfibios(animal):
    
    
    def __init__(self, nome,tamanhoComprimento, nº_de_patas, cor, ambiente,alimento):
        super().__init__(nome,tamanhoComprimento, nº_de_patas, cor, ambiente)
        self.alimento = alimento
    def cria_animal_filho3():
        nome,tamanho,patas,cor,ambiente = animal.cria_animal()
        alimento = input ('digite o alimento:')
        
        return Anfibios(nome,tamanho,patas,cor,ambiente,alimento)
    
    def exibe_dados_filho(self):
        super().exibe_dados_pai()
        print('Alimento:',self.alimento)
        
        