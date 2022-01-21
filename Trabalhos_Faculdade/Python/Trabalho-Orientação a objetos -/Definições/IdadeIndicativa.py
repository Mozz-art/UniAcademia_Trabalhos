#BRUNO CORONA E RAPHAELLA RANIERI

class IdadeIndicativa():
    def __init__(self, idadeIndicativa: int):

        self._idadeIndicativa = idadeIndicativa

    @property
    def idadeIndicativa(self):
        return self._idadeIndicativa

    @idadeIndicativa.setter
    def idadeIndicativa(self, idadeIndicativa):
        self._idadeIndicativa = idadeIndicativa


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    idadeIndicativa = IdadeIndicativa(18)


    # MÉTODOS DA CLASSE IDADEINDICATIVA
    print(idadeIndicativa.idadeIndicativa)
