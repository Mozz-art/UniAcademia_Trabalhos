#BRUNO CORONA E RAPHAELLA RANIERI
class Usuario:
    def __init__(self, nome: str, dtaNascimento: str, email: str):
        self._nome = nome
        self._dtaNascimento = dtaNascimento
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dtaNascimento(self):
        return self._dtaNascimento

    @dtaNascimento.setter
    def dtaNascimento(self, dtaNascimento):
        self._dtaNascimento = dtaNascimento

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    usuario = Usuario('', '', '')
    print(usuario.nome)
    print(usuario.dtaNascimento)
    print(usuario.email)
