# 4- Quais os piores filmes desse ano que ganharam algum framboesa de ouro?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from Avaliacao import Avaliacao
from Usuario import Usuario
from Premios import Premios


if __name__ == '__main__':

        filmes = Filmes ('Senhor dos pasteis', 'Genero: Aventura', 'Duração: 400min ')
        filmes2 = Filmes  ('Exercito dos mortos', 'Genero: Terror', 'Duração: 140min ')
        filmes3 = Filmes ('Morrer ou morrer', 'Genero: Ação', 'Duração: 135min ')
        avaliacao1 = Avaliacao ('Usuario: Lorde','email: lorde@.com','Data de nascimento: 23/09/1999','Nota: 2',
        'Comentario: Dormi nos 2 primeiros minutos, muito ruim')
        avaliacao2 = Avaliacao('Usuario: Zeca','email: zeca@@.com','Data de nascimento: 22/01/1977',
        'Nota: 4', 'Comentario: Não assusta nem uma criança')
        avaliacao3 = Avaliacao ('Usuario: Fabin','email: fabin@@.com','Data de nascimento: 01/01/1923',
        'Nota: 5', 'Comentario: Quase morri vendo esse filme')
        premios = Premios ('Fambroesa:', 'Pior filme do século')
        premio2 = Premios ('Framboesa:', 'Terror mais fraco do ano')
        premio3 = Premios ('Framboesa:', 'Ação mais parada do mundo')


        print('4- Quais os piores filmes da netflix desse ano que ganharam algum framboesa de ouro?')
        print()
        print('=' * 40)

        print('-' * 15, 'Filme 1', '-' * 15)


        print(filmes.filme)
        print(filmes.genero)
        print(filmes.duracao)
        print(avaliacao1.nome)
        print(avaliacao1.notas)
        print(avaliacao1.comentarios)
        print(premios.premio)
        print(premios.categoria)


        print('-' * 15, 'Filme 2', '-' * 15)


        print(filmes2.filme)
        print(filmes2.genero)
        print(filmes2.duracao)
        print(avaliacao2.nome)
        print(avaliacao2.notas)
        print(avaliacao2.comentarios)
        print(premio2.premio)
        print(premio2.categoria)


        print('-' * 15, 'Filme 3', '-' * 15)


        print(filmes3.filme)
        print(filmes3.genero)
        print(filmes3.duracao)
        print(avaliacao3.nome)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)
        print(premio3.premio)
        print(premio3.categoria)
