# 5- Qual filme e indicação do ator indicado ao ultimo framboesa de ouro?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from Atores import Atores
from Premios import Premios


if __name__ == '__main__':
        atores = Atores ('O ator: Fabio galã', 'Idade: 42', 'Carreira: 20 anos')
        filme = Filmes ('Filme feito: Guerra em londres', 'Gênero: Ação', 'Duração: 75 min')
        premio = Premios ('Framboesa de ouro:', 'Pior Atuação')

        print('Qual filme e indicação do ator indicado ao ultimo framboesa de ouro?')
        print()
        print('=' * 40)

        print(atores.nomeAtor)
        print(atores.idadeAtor)
        print(atores.tempoCarreira)
        print(filme.filme)
        print(filme.genero)
        print(filme.duracao)
        print(premio.premio)
        print(premio.categoria)