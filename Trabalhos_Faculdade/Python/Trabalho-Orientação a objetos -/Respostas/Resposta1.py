#Quais filmes ganhadores do Oscar 2021?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from IdadeIndicativa import IdadeIndicativa
from Estreia import Estreia
from Premios import Premios


if __name__ == '__main__':

    filmes = Filmes('Dona chica e a morte do gato.', 'Genero: Suspense.', 'Duração: 120 min.')
    filmes2 = Filmes('João o ladrão de pão.', 'Aventura.', '110 min.')
    filmes3 = Filmes('A vingança do João.', 'Terror.', '140 min.')
    idadeIndicativa = IdadeIndicativa('Classificação indicativa é de: 16 Anos.')
    idadeIndicativa2 = IdadeIndicativa('Classificação indicativa é: Livre para todos os públicos.')
    idadeIndicativa3 = IdadeIndicativa('Classificação indicativa é de: 16 Anos.')
    estreia = Estreia ('Data de lançamento do filme: 2021.', 'Bilheteria: 10.000')
    estreia2 = Estreia ('Data de lançamento do filme: 2021.', 'Bilheteria: 12.030')
    estreia3 = Estreia ('Data de lançamento do filme: 2021.', 'Bilheteria: 23.000')
    premios = Premios('Ganhador do Oscar', 'Melhor filme')
    premios2 = Premios('Ganhador do Oscar', 'Melhor roteiro')
    premios3 = Premios('Ganhador do Oscar', 'Melhor ator')

    print('1- Quais filmes ganhadores do Oscar 2021?')
    print()
    print('=' * 40)

    print('-' * 15 ,'Filme 1' , '-' * 15)

    print(filmes.filme)
    print(filmes.genero)
    print(filmes.duracao)
    print(idadeIndicativa.idadeIndicativa)
    print(estreia.dtaLancamento)
    print(estreia.bilheteria)
    print(premios.premio)
    print(premios.categoria)

    print('=' * 40)
    print()

    print('-' * 15, 'Filme 2', '-' * 15)

    print(filmes2.filme)
    print(filmes2.genero)
    print(filmes2.duracao)
    print(idadeIndicativa2.idadeIndicativa)
    print(estreia.dtaLancamento)
    print(estreia.bilheteria)
    print(premios.premio)
    print(premios2.categoria)

    print('=' * 40)
    print()

    print('-' * 15, 'Filme 3', '-' * 15)

    print(filmes3.filme)
    print(filmes3.genero)
    print(filmes3.duracao)
    print(idadeIndicativa3.idadeIndicativa)
    print(estreia.dtaLancamento)
    print(estreia.bilheteria)
    print(premios.premio)
    print(premios3.categoria)
