from _super_animais import animal
    
    
    
class repteis(animal):
    
    
    def __init__(self, nome,tamanhoComprimento, n_de_patas, cor, ambiente,alimento):
        super().__init__(nome,tamanhoComprimento, n_de_patas, cor, ambiente)
        self.alimento = alimento
    def cria_animal_filho1():
        super().cria_animal()
        
        alimento = input ('digite o alimento:')
        
    
    def exibe_dados_filho(self):
        super().exibe_dados_pai()
        print('Alimento:',self.alimento)
        
        