#BRUNO CORONA E RAPHAELLA RANIERI
class Atores:
    def __init__(self,  nomeAtor: str, idadeAtor: int, tempoCarreira: int):
        self._nomeAtor = nomeAtor
        self._idadeAtor = idadeAtor
        self._tempoCarreira = tempoCarreira
    @property
    def nomeAtor(self):
        return self._nomeAtor

    @nomeAtor.setter
    def nomeAtor(self, nomeAtor):
        self._nomeAtor = nomeAtor

    @property
    def idadeAtor(self):
        return self._idadeAtor

    @idadeAtor.setter
    def idadeAtor(self, idadeAtor):
        self._idadeAtor = idadeAtor

    @property
    def tempoCarreira(self):
        return self._tempoCarreira

    @tempoCarreira.setter
    def tempoCarreira(self, tempoCarreira):
        self._tempoCarreira = tempoCarreira


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    atores = Atores('Ator Qualquer', 69, 5)


    # MÉTODOS DA CLASSE ATORES
    print(atores.nomeAtor)
    print(atores.idadeAtor)
    print(atores.tempoCarreira)

