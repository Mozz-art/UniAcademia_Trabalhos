#3- Quais filmes ganhadores de premios com notas 10 no site?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from Avaliacao import Avaliacao
from Usuario import Usuario
from Premios import Premios

if __name__ == '__main__':

        filmes = Filmes ('Harry potter e a ordem da fenix', 'Genero: Aventura', 'Duração: 138min ')
        filmes2 = Filmes  ('Alerta Vermelho', 'Genero: Ação', 'Duração: 115min ')
        filmes3 = Filmes ('Piratas do caribe 1', 'Genero: Aventura', 'Duração: 168min ')
        avaliacao1 = Avaliacao ('Usuario: Raphaella','email: rapha@@.com','Data de nascimento: 17/08/2000','Nota: 10',
        'Comentario: Obra prima')
        avaliacao2 = Avaliacao('Usuario: Zezin','email: ozé@@.com','Data de nascimento: 15/06/2002',
        'Nota: 10', 'Comentario: Engraçado')
        avaliacao3 = Avaliacao ('Usuario: Pedrao','email: pedrin@@.com','Data de nascimento: 14/07/1998',
        'Nota: 10', 'Comentario: Melhor aventura')
        premios = Premios ('Oscar',  'Melhor filme do ano' )
        premio2 = Premios ('Oscar', 'Melhor filme do mês')
        premio3 = Premios ('Oscar', ' Melhor ator principal')


        print('3- Quais filmes ganhadores de prêmios com notas 10 no site?')
        print()
        print('=' * 40)

        print('-' * 15, 'Filme 1', '-' * 15)

        print(avaliacao1.nome)
        print(filmes.filme)
        print(filmes.genero)
        print(filmes.duracao)
        print(avaliacao1.notas)
        print(avaliacao1.comentarios)
        print(premios.premio)
        print(premios.categoria)


        print('-' * 15, 'Filme 2', '-' * 15)

        print(avaliacao2.nome)
        print(filmes2.filme)
        print(filmes2.genero)
        print(filmes2.duracao)
        print(avaliacao2.notas)
        print(avaliacao2.comentarios)
        print(premio2.premio)
        print(premio2.categoria)

        print('-' * 15, 'Filme 3', '-' * 15)

        print(avaliacao3.nome)
        print(filmes3.filme)
        print(filmes3.genero)
        print(filmes3.duracao)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)
        print(premio3.premio)
        print(premio3.categoria)