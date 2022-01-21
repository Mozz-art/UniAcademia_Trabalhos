
# CORES
red = '\033[1:31m'
blue = '\033[1:34m'
gray = '\033[1:37m'
green = '\033[1:32m'
purple = '\033[1:35m'

bold = '\033[1m'
invert = '\033[7m'

cls = '\033[m'


def desenhar():
    """
    Método para desenha o jogo da velha.
    """
    print(f'{bold}', end='')
    c = 0
    for linha in range(0, 3):
        print(f' {linha + 1 + c} | {linha + 2 + c} | {linha + 3 + c}  | ', end='')
        print(f' {jogo[linha][0]} | {jogo[linha][1]} | {jogo[linha][2]} ')
        if linha != 2:
            print('---|---|--- | ---|---|---')
        c += 2
    print(f'{cls}', end='')


def checar():
    """
    Método responsável por checar se o jogador ou computador ganhou o jogo.
    """
    global resultado
    if len(disponiveis) == 0:
        resultado = 'EMPATOU!'
    else:
        if jogo[1][1] != ' ':
            if jogo[0][0] == jogo[1][1] == jogo[2][2] or jogo[2][0] == jogo[1][1] == jogo[0][2]:
                if jogo[1][1] == jogador[0]:
                    resultado = 'JOGADOR 1 - GANHOU!'
                else:
                    resultado = 'JOGADOR 2 - GANHOU!'
        for c in range(0, 3):
            if jogo[c][c] != ' ':
                if jogo[c][0] == jogo[c][1] == jogo[c][2]:  # HORIZONTAL
                    if jogo[c][0] == jogador[0]:
                        resultado = 'JOGADOR 1 - GANHOU!'
                    elif jogo[c][0] == jogador[1]:
                        resultado = 'JOGADOR 2 - GANHOU!'
                elif jogo[0][c] == jogo[1][c] == jogo[2][c]:  # VERTICAL
                    if jogo[0][c] == jogador[0]:
                        resultado = 'JOGADOR 1 - GANHOU!'
                    elif jogo[0][c] == jogador[1]:
                        resultado = 'JOGADOR 2 - GANHOU!'


def jogar(jogador):
    try:
        posicao = input('Posição: ').strip()[0] if len(disponiveis) > 1 else str(disponiveis[0])
        if posicao.isnumeric():
            posicao = abs(int(posicao))
            x = 0
            if posicao in disponiveis:
                if posicao <= 3:
                    i = 0  # indice: 0           1           2
                    x = 1  # 1 - x = 0 | 2 - x = 1 | 3 - x = 2
                elif posicao <= 6:
                    i = 1
                    x = 4  # 4 - x = 0 | 5 - x = 1 | 6 - x = 2
                else:
                    i = 2
                    x = 7  # 6 - x = 0 | 7 - x = 1 | 8 - x = 2
                jogo[i][posicao - x] = jogador
                disponiveis.remove(posicao)
                usados.append(posicao)
                return True
            elif posicao in usados:
                print(f'{red}', end='')
                print(f'A posição {posicao} já foi escolhida. Tente novamente.')
                print(f'{cls}')
                return False
            else:
                print(f'{red}', end='')
                print('Entrada inválida. Tente novamente.', end='')
                print(f'{cls}')
                return False
        else:
            print(f'{red}', end='')
            print('Entrada inválida. Tente novamente.', end='')
            print(f'{cls}')
            return False
    except IndexError:
        print(f'{red}', end='')
        print('Entrada inválida. Tente novamente.')
        print(f'{cls}')
        return False

# JOGO DA VELHA
while True:
    options = 'XO'
    jogador = ['', '']
    disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    usados = []
    jogo = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    resultado = None
    print(f'{invert}', end='')
    print(f'{"JOGO DA VELHA":^25}', end='')
    print(f'{cls}')
    # Os Jogadores escolhem entre X ou O
    while True:
        print(f'{invert}', end='')
        print(f'{"JOGADOR 1":^25}', end='')
        print(f'{cls}')
        try:
            jogador[0] = input('Deseja jogar com X ou O: ').strip().upper()[0]
            if jogador[0] in options:
                jogador[1] = 'X' if jogador[0] != 'X' else 'O'
                break
            else:
                print(f'{red}', end='')
                print('Opção inválida. Tente novamente.')
                print(f'{cls}')
        except IndexError:
            print(f'{red}', end='')
            print('Entrada inválida. Tente novamente.')
            print(f'{cls}')
            continue
    # Aqui começa realmente o jogo
    while resultado is None:
        for c in range(0, 2):
            while True:
                print(f'{invert}', end='')
                print(f'{"POSIÇÕES":^12}|{"JOGO":^12}', end='')
                print(f'{cls}')
                desenhar()
                print(f'Opções disponíveis: {disponiveis}.')
                print(f'{invert}', end='')
                if c == 0:
                    print(f'{"JOGADOR 1":^25}', end='')
                else:
                    print(f'{"JOGADOR 2":^25}', end='')
                print(f'{cls}')
                jogou = jogar(jogador[c])
                if jogou:
                    checar()
                    break
            if resultado is not None:
                desenhar()
                print(f'{invert}', end='')
                print(f'{"FIM DE JOGO!":^25}', end='')
                print(f'{cls}')
                print(f'{invert}', end='')
                print(f'{resultado:^25}', end='')
                print(f'{cls}')
                break
    while True:
        continua = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continua in 'SN':
            break
        else:
            print(f'{red}', end='')
            print('Opção inválida. Tente novamente.', end='')
            print(f'{cls}')
    if continua == 'N':
        break
