#BRUNO CORONA E RAPHAELLA RANIERI
class Series:
    def __init__(self, serie: str, genero: str, ntemporadas: int):
        self._genero = genero
        self._ntemporadas = ntemporadas
        self._serie = serie

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ntemporadas(self):
        return self._ntemporadas

    @ntemporadas.setter
    def ntemporadas(self, ntemporadas):
        self._ntemporadas = ntemporadas

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, serie):
        self._serie = serie


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    series = Series('Serie Qualquer', 'Genero Qualquer', 10)
    print(series.serie)
    print(series.genero)
    print(series.ntemporadas)
