# 8- Qual a serie de cada plataforma, com a maior nota do principal usuario do site de avaliação?
#BRUNO CORONA E RAPHAELLA RANIERI

from Series import Series
from Plataformas import Plataformas
from Avaliacao import Avaliacao

if __name__ == '__main__':
        serie = Series ('Mentes criminosas', 'Ação', '16 temporadas')
        serie2 = Series('NCIS', 'Policial', '10 temporadas')
        serie3 = Series('Vida fora de série', 'Romance', '4 temporadas')
        serie4 = Series('Olaf', 'Aventura', '6 temporadas')
        plataforma = Plataformas ('Plataforma: Netflix')
        plataforma2 = Plataformas ('Plataforma: Amazon prime')
        plataforma3 = Plataformas('Plataforma: Youtube series')
        plataforma4 = Plataformas ('Plataforma: Disney +')
        avaliacao = Avaliacao ('Valter', '18/08/2005', 'valterfilmes@email','nota: 9', 'Comentario: Serie que prende')
        avaliacao2 = Avaliacao('Valter', '18/08/2005', 'valterfilmes@email', 'nota: 10', 'Comentario: Mais emocionante de todas')
        avaliacao3 = Avaliacao('Valter', '18/08/2005', 'valterfilmes@email', 'nota: 8', 'Comentario: Me emocionei muito')
        avaliacao4 = Avaliacao('Valter', '18/08/2005', 'valterfilmes@email', 'nota: 9', 'Comentario: Final incrivel!')

        print('Qual a serie de cada plataforma, com a maior nota do principal usuario do site de avaliação?')
        print()
        print('=' * 40)

        print('-' * 15, 'O usuario:', '-' * 15)
        print(avaliacao.nome)
        print(avaliacao.dtaNascimento)
        print(avaliacao.email)

        print('-' * 15, 'Série 1', '-' * 15)
        print(serie.serie)
        print(serie.genero)
        print(serie.ntemporadas)
        print(plataforma.plataforma)
        print(avaliacao.notas)
        print(avaliacao.comentarios)


        print('-' * 15, 'Série 2', '-' * 15)
        print(serie2.serie)
        print(serie2.genero)
        print(serie2.ntemporadas)
        print(plataforma2.plataforma)
        print(avaliacao2.notas)
        print(avaliacao2.comentarios)

        print('-' * 15, 'Série 3', '-' * 15)
        print(serie3.serie)
        print(serie3.genero)
        print(serie3.ntemporadas)
        print(plataforma3.plataforma)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)

        print('-' * 15, 'Série 4', '-' * 15)
        print(serie3.serie)
        print(serie3.genero)
        print(serie3.ntemporadas)
        print(plataforma3.plataforma)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)