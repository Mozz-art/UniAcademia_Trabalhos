# 6- Qual filme para crianças com a maior bilheteria desse ano?
#BRUNO CORONA E RAPHAELLA RANIERI
from Filmes import Filmes
from IdadeIndicativa import IdadeIndicativa
from Estreia import Estreia

if __name__ == '__main__':
        filme = Filmes ('Filme: Procurando o pai do nemo', 'Gênero: Animção', 'Duração: 130min')
        idadeindicativa = IdadeIndicativa ('Indicado para crianças de 10 anos')
        estreia = Estreia ('Estreia: 2021', 'Bilheteria 1.000')

        print('Qual filme para crianças com a maior bilheteria desse ano?')
        print()
        print('=' * 40)

        print(filme.filme)
        print(filme.genero)
        print(filme.duracao)
        print(idadeindicativa.idadeIndicativa)
        print(estreia.dtaLancamento)
        print(estreia.bilheteria)

