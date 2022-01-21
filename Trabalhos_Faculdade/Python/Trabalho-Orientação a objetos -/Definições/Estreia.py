#BRUNO CORONA E RAPHAELLA RANIERI
class Estreia():
    def __init__(self, dtaLancamento: str, bilheteria: int):

        self._dtaLancamento = dtaLancamento
        self._bilheteria = bilheteria


    @property
    def dtaLancamento(self):
        return self._dtaLancamento

    @dtaLancamento.setter
    def dtaLancamento(self, dtaLancamento):
        self._dtaLancamento = dtaLancamento

    @property
    def bilheteria(self):
        return self._bilheteria

    @bilheteria.setter
    def bilheteria(self, bilheteria):
        self._bilheteria = bilheteria


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    estreia = Estreia('10', '10 milhoes')



    # METODOS DA CLASSE DATA
    print(estreia.dtaLancamento)
    print(estreia.bilheteria)
    print('=' * 20)
