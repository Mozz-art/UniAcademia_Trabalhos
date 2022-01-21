# 7- Quais series que irão chegar na netflix em 2022 ganharam prêmio nos EUA?
#BRUNO CORONA E RAPHAELLA RANIERI
from Series import Series
from Plataformas import Plataformas
from Estreia import Estreia
from Premios import Premios

if __name__ == '__main__':
        serie = Series ('Gênero: Aventura', '5 temporadas', 'Nome: Rain' )
        serie2 = Series('Gênero: Ação', '16 temporadas', 'Nome: Corra')
        serie3 = Series('Gênero: Comédia', '3 temporadas', 'Nome: Dark')
        estreia = Estreia ('Data de estreia: 20/01/2022', 0)
        estreia2 = Estreia ('Data de estreia: 01/04/2022', 0)
        estreia3 = Estreia ('Data de estreia: 28/09/2022', 0)
        plataforma = Plataformas ('Netflix')
        premio = Premios ('Vencedor Oscar', 'Melhor ator principal')
        premio2 = Premios ('Vencedor Oscar', 'Melhor trilha sonora')
        premio3 = Premios ('Vencedor Emmy', 'Melhor série do ano')


        print('Quais series irão chegar na netflix em 2022?')
        print()
        print('=' * 40)

        print('-' * 15, 'Série 1', '-' * 15)
        print (serie.serie)
        print (serie.genero)
        print (serie.ntemporadas)
        print (estreia.dtaLancamento)
        print (plataforma.plataforma)
        print (premio.premio)
        print (premio.categoria)

        print('-' * 15, 'Série 2', '-' * 15)
        print (serie2.serie)
        print (serie2.genero)
        print (serie2.ntemporadas)
        print (estreia2.dtaLancamento)
        print (plataforma.plataforma)
        print (premio2.premio)
        print (premio2.categoria)

        print('-' * 15, 'Série 3', '-' * 15)
        print (serie3.serie)
        print (serie3.genero)
        print (serie3.ntemporadas)
        print (estreia3.dtaLancamento)
        print (plataforma.plataforma)
        print (premio3.premio)
        print (premio3.categoria)
