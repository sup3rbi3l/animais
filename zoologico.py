from _super_animais import animal
from repteis import repteis
from mamiferos import mamiferos
from Anfibios import Anfibios




def main():
    print('==============reptil==============')
    reptil = repteis.cria_animal_filho1()
    print('==============mamifero==============')
    mamifero = mamiferos.cria_animal_filho2()
    print('==============anfibeo==============')
    anfibio = Anfibios.cria_animal_filho3()
    
    print('==============reptil==============')
    reptil.exibe_dados_filho()
    
    print('==============mamifero==============')
    mamifero.exibe_dados_filho()
    
    print('==============anfibio==============')
    anfibio.exibe_dados_filho()
if __name__ == '__main__':
    main()