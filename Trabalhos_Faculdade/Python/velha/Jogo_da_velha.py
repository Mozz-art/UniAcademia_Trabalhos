from random import choice

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
    linha = 0
    print(f'{bold}', end='')
    while linha <= 6:
        print(f' {linha + 1} | {linha + 2} | {linha + 3}  | ', end='')
        print(f' {jogo[0 + linha]} | {jogo[1 + linha]} | {jogo[2 + linha]} ')
        linha += 3
        if linha != 9:
            print('---|---|--- | ---|---|---')
    print(f'{cls}', end='')


def ia():
    """
    Método IA - O computador, oponente do jogador no jogo da velha.
    """
    pos = choice(disponiveis)
    jogo[pos - 1] = computador
    disponiveis.remove(pos)
    usados.append(pos)


def checar():
    """
    Método responsável por checar se o jogador ou computador ganhou o jogo.
    """
    global resultado
    if len(disponiveis) == 0:
        resultado = 'EMPATOU!'
    else:
        if jogo[4] != ' ':
            if jogo[0] == jogo[4] == jogo[8] or jogo[2] == jogo[4] == jogo[6]:
                if jogo[4] == jogador:
                    resultado = 'VOCÊ GANHOU!'
                else:
                    resultado = 'VOCÊ PERDEU!'
        linha = 0
        coluna = 0
        while linha <= 6:
            if jogo[linha] != ' ':
                if jogo[linha] == jogo[linha + 1] == jogo[linha + 2]:  # HORIZONTAL
                    if jogo[linha] == jogador:
                        resultado = 'VOCÊ GANHOU!'
                    elif jogo[linha] == computador:
                        resultado = 'VOCÊ PERDEU!'
                elif jogo[coluna] == jogo[coluna + 3] == jogo[coluna + 6]:  # VERTICAL
                    if jogo[coluna] == jogador:
                        resultado = 'VOCÊ GANHOU!'
                    elif jogo[coluna] == computador:
                        resultado = 'VOCÊ PERDEU!'
            coluna += 1
            linha += 3


while True:
    options = 'XO'
    resultado = None
    jogo = [' '] * 9
    disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    usados = []
    print(f'{invert}', end='')
    print(f'{"JOGO DA VELHA":^25}', end='')
    print(f'{cls}')
    while True:
        jogador = input('Deseja jogar com X ou O: ').strip().upper()[0]
        if jogador in options:
            computador = 'X' if jogador != 'X' else 'O'
            break
        else:
            print(f'{red}', end='')
            print('Opção inválida. Tente novamente.')
            print(f'{cls}', end='')
    while len(disponiveis) > 0:
        print(f'{invert}', end='')
        print(f'{"POSIÇÕES":^12}|{"JOGO":^12}', end='')
        print(f'{cls}')
        desenhar()
        print(f'{green}')
        print(f'Opções disponíveis: {disponiveis}.')
        posicao = input('Posição: ').strip()[0]
        print(f'{cls}')
        if posicao.isnumeric():
            posicao = int(posicao)
            if posicao in disponiveis:
                jogo[posicao - 1] = jogador
                disponiveis.remove(posicao)
                usados.append(posicao)
                checar()
                if resultado is None:
                    ia()
                    checar()
                if resultado is not None:
                    desenhar()
                    print(f'{invert}', end='')
                    print(f'{"FIM DE JOGO!":^25}', end='')
                    print(f'{cls}')
                    print(f'{invert}', end='')
                    print(f'{resultado:^25}', end='')
                    print(f'{cls}')
                    break
            elif posicao in usados:
                print(f'{red}', end='')
                print(f'A posição {posicao} já foi escolhida. Tente novamente.')
                print(f'{cls}', end='')
            else:
                print(f'{red}', end='')
                print('Entrada inválida. Tente novamente.')
                print(f'{cls}', end='')
        else:
            print(f'{red}', end='')
            print('Entrada inválida. Tente novamente.')
            print(f'{cls}', end='')
    while True:
        continua = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if continua in 'SN':
            break
        else:
            print('\033[1:31m', end='')
            print('Opção inválida. Tente novamente.')
            print('\033[m', end='')
    if continua == 'N':
        break
