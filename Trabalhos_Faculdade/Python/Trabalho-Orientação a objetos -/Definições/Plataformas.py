#BRUNO CORONA E RAPHAELLA RANIERI
class Plataformas():
    def __init__(self, plataforma: str):

        self._plataforma = plataforma

    @property
    def plataforma(self):
        return self._plataforma

    @plataforma.setter
    def plataforma(self, plataforma):
        self._plataforma = plataforma


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    plataformas = Plataformas('')


    # MÉTODOS DA CLASSE PLATAFORMAS
    print(plataformas.plataforma)
