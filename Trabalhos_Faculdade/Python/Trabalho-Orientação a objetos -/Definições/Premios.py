#BRUNO CORONA E RAPHAELLA RANIERI
class Premios:
    def __init__(self, premio: str, categoria):
        self._premio = premio
        self._categoria = categoria

    @property
    def premio(self):
        return self._premio

    @premio.setter
    def premio(self, premio):
        self._premio = premio

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria




premios = Premios('', '')

print(premios.premio)
print(premios.categoria)