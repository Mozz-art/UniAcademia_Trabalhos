# 9- Quais são os filmes e series da plataforma com mais vencedores de premios em 2021?
#BRUNO CORONA E RAPHAELLA RANIERI

from Filmes import Filmes
from Series import Series
from Plataformas import Plataformas
from Premios import Premios
from Estreia import Estreia

if __name__ == '__main__':
        filme = Filmes('Filme: João e o Pé de feijão .', 'Genero: Animção', 'Duração: 120 min.')
        filme2 = Filmes('Filme: João o ladrão de pão.', 'Aventura.', '110 min.')
        serie = Series ('Amor em Paris', 'Genero: Romance', 'Número de temporadas: 4')
        serie2 = Series('CSI Miami', 'Genero: Policial', 'Número de temporadas: 6')
        plataforma = Plataformas ('Amazon prime')
        premio = Premios ('Prêmio: Oscar', 'Categoria: Melhor Animação do ano')
        premio2 = Premios('Prêmio: Emmy', 'Categoria: Melhor Trilha sonora')
        premio3 = Premios('Prêmio: Oscar', 'Categoria: Melhor atriz principal')
        premio4 = Premios('Prêmio: Oscar', 'Categoria: Melhor roteiro')
        estreia = Estreia('Data de estreia: 21/04/2021', 0)
        estreia2 = Estreia('Data de estreia: 01/08/2021', 0)
        estreia3= Estreia('Data de estreia: 23/12/2021' ,0)
        estreia4 = Estreia('Data de estreia: 18/07/2021',0)



        print ('Quais são os filmes e series da plataforma com mais vencedores de premios em 2021?')
        print()
        print('=' * 40)

        print('-' * 15, 'Lançamento 1', '-' * 15)

        print(filme.filme)
        print(filme.genero)
        print(filme.duracao)
        print(plataforma.plataforma)
        print(premio.premio)
        print(premio.categoria)
        print(estreia.dtaLancamento)

        print('-' * 15, 'Lançamento 2', '-' * 15)

        print(filme2.filme)
        print(filme2.genero)
        print(filme2.duracao)
        print(plataforma.plataforma)
        print(premio2.premio)
        print(premio2.categoria)
        print(estreia2.dtaLancamento)


        print('-' * 15, 'Lançamento 3', '-' * 15)

        print(serie.serie)
        print(serie.genero)
        print(serie.ntemporadas)
        print(plataforma.plataforma)
        print(premio3.premio)
        print(premio3.categoria)
        print(estreia3.dtaLancamento)

        print('-' * 15, 'Lançamento 4', '-' * 15)

        print(serie2.serie)
        print(serie2.genero)
        print(serie2.ntemporadas)
        print(plataforma.plataforma)
        print(premio4.premio)
        print(premio4.categoria)
        print(estreia4.dtaLancamento)




