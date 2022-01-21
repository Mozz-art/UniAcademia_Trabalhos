#Qual genero mais procurado na amazon filmes em 2017?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from Series import Series
from Estreia import Estreia
from Plataformas import Plataformas


if __name__ == '__main__':
    categoria = ['suspense', 'terror', 'aventura']
    estreia = Estreia('2017', '')
    filmes = Filmes('', f'O Genero de filmes mais assistido em {estreia.dtaLancamento} foi de: {categoria[0]}.', '')
    series = Series('', f'O Genero das series mais assistidas em {estreia.dtaLancamento} foi de: {categoria[1]}', '')
    plataformas = Plataformas('Plataforma: Amazon Filmes')

    print()
    print('Qual genero mais procurado na amazon filmes em 2017?')
    print()
    print('=' * 60)
    print()
    print('-' * 26 ,'Filmes' , '-' * 26)
    print()
    print(filmes.genero)
    print()
    print()
    print(plataformas.plataforma)
    print()
    print('=' * 60)
    print()

    print('-' * 26 ,'Series' , '-' * 26)
    print()
    print(series.genero)
    print()
    print(plataformas.plataforma)
