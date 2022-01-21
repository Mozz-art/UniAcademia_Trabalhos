#10 - De todas as plataformas juntas, qual o filme de terror melhor avaliado por usuarios menores de idade?
#BRUNO CORONA E RAPHAELLA RANIERI
from Plataformas import Plataformas
from Filmes import Filmes
from Avaliacao import Avaliacao

if __name__ == '__main__':
        filme = Filmes ('O exorcismo', 'Gênero: Terror', 'Duração: 145min')
        plataformas = Plataformas  ('Neflix')
        avaliacao1 = Avaliacao ('Jorge', 'jorge@email.com', '21/02/2007', 'nota: 10', 'Comentario: Muito irado!')
        avaliacao2 = Avaliacao ('Pedro', 'pedro@email.com', '12/06/2006', 'nota: 9', 'Comentario: Deu medo!')
        avaliacao3 = Avaliacao ('Julia', 'Juju@email.com', '21/02/2005', 'nota: 10', 'Comentario: Melhor narrativa!')
        avaliacao4 = Avaliacao ('Mariana', 'mari@email.com', '10/08/2004', 'nota: 8', 'Comentario: Melhor do ano!')

        print('De todas as plataformas juntas, qual o filme de terror melhor avaliado por usuarios menores de idade?')
        print()
        print('=' * 40)

        print('-' * 15, 'Melhor Terror', '-' * 15)
        print(filme.filme)
        print(filme.duracao)
        print(plataformas.plataforma)

        print('=' * 40)

        print('-' * 15, 'Avaliações', '-' * 15)
        print(avaliacao1.nome)
        print(avaliacao1.dtaNascimento)
        print(avaliacao1.notas)
        print(avaliacao1.comentarios)

        print('-' * 40)

        print(avaliacao2.nome)
        print(avaliacao2.dtaNascimento)
        print(avaliacao2.notas)
        print(avaliacao2.comentarios)

        print('-' * 40)

        print(avaliacao3.nome)
        print(avaliacao3.dtaNascimento)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)

        print('-' * 40)

        print(avaliacao3.nome)
        print(avaliacao3.dtaNascimento)
        print(avaliacao3.notas)
        print(avaliacao3.comentarios)