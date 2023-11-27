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


if __name__ == '__main__':
    main()