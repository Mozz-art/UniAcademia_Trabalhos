#BRUNO CORONA E RAPHAELLA RANIERI
from Usuario import Usuario


class Avaliacao(Usuario):
    def __init__(self, nome, email, dtaNascimento, notas, comentarios):
        Usuario.__init__(self, nome, dtaNascimento, email)
        self._notas = notas
        self._comentarios = comentarios


    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, notas):
        self._notas = notas

    @property
    def comentarios(self):
        return self._comentarios

    @comentarios.setter
    def comentarios(self, comentarios):
        self._comentarios = comentarios



# Isso é para testa essa classe individualmente
# CTRL + SHIFT + F10 pra rodar esse arquivo no Pycharm
if __name__ == '__main__':
    usuario = Avaliacao('', '', '',
                        '', '', '')


    # MÉTODOS DA CLASSE USUARIO
    print(usuario.email)
    print(usuario.nome)
    print(usuario.dtaNascimento)

    # MÉTODOS DA CLASSE AVALIACAO
    print(usuario.notas)
    print(usuario.comentarios)


