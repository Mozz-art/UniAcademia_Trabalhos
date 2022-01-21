#BRUNO CORONA E RAPHAELLA RANIERI
class Filmes:
    def __init__(self, filme: str, genero: str, duracao: str):
        self._filme = filme
        self._genero = genero
        self._duracao = duracao

    @property
    def filme(self):
        return self._filme

    @filme.setter
    def filme(self, filme):
        self._filme = filme

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    filmes = Filmes('', '')
    filmes2 = Filmes('', '', '')
    print(filmes.filme)
    print(filmes2.filme)
    print(filmes.genero)
    print(filmes.duracao)
