import random

# CORES
red = '\033[1:31m'
green = '\033[1:32m'
blue = '\033[1:34m'
gray = '\033[1:37m'
cls = '\033[m'
yellow = '\033[1m'
yellow = '\033[93m'


def vencer_jogo():
    global game
    global m_escondida

    w = 0
    e = 0
    while w < 10:
        while e < 10:
            if m_escondida[w][e] != 'M':
                game[w + 1][e + 1] = m_escondida[w][e]
            e += 1
        e = 0
        w += 1


def checar(x, z):
    global game
    global m_escondida

    if m_escondida[x][z] != 'M' and game[x + 1][z + 1] == '#':
        if m_escondida[x][z] != '.':
            game[x + 1][z + 1] = m_escondida[x][z]
        else:
            game[x + 1][z + 1] = m_escondida[x][z]
            abrir_mesa(x, z)


def abrir_mesa(t, y):
    global game
    global m_escondida

    if t - 1 > -1:
        if y - 1 > -1:
            checar((t - 1), (y - 1))
        if y + 1 < 10:
            checar((t - 1), (y + 1))
        checar((t - 1), y)

    if y - 1 > -1:
        checar(t, (y - 1))
    if y + 1 < 10:
        checar(t, (y + 1))

    if t + 1 < 10:
        if y - 1 > -1:
            checar((t + 1), (y - 1))
        if y + 1 < 10:
            checar((t + 1), (y + 1))
        checar((t + 1), y)




game = [0, '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
m_escondida = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

t = 0

while t < 11:
    if t == 0:
        game[t] = [red, '   ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    else:
        if t != 10:
            game[t] = [blue, str(t) + '  ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        else:
            game[t] = [blue, str(t) + ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    t += 1

t = 0
while t < 10:
    m_escondida[t] = ['!', '!', '!', '!', '!', '!', '!', '!', '!', '!']
    t += 1

t = 0
while t < 11:
    if t == 0:
        print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
              game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
        print()
    else:
        print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
              game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
    t += 1

print()
jogada_escolhida = input("Ponha as coordenadas separadas por Coluna:linha ")
print()

player_coordenadas = jogada_escolhida.split(':')
player_coordenadas[0] = int(player_coordenadas[0]) - 1
player_coordenadas[1] = int(player_coordenadas[1]) - 1

m_escondida[player_coordenadas[0]][player_coordenadas[1]] = '.'

# makes sure no minas around first pick

if player_coordenadas[0] - 1 > -1:
    if player_coordenadas[1] - 1 > -1:
        m_escondida[player_coordenadas[0] - 1][player_coordenadas[1] - 1] = 'c'
    m_escondida[player_coordenadas[0] - 1][player_coordenadas[1]] = 'c'
    if player_coordenadas[1] + 1 < 10:
        m_escondida[player_coordenadas[0] - 1][player_coordenadas[1] + 1] = 'c'

if player_coordenadas[1] - 1 > -1:
    m_escondida[player_coordenadas[0]][player_coordenadas[1] - 1] = 'c'
if player_coordenadas[1] + 1 < 10:
    m_escondida[player_coordenadas[0]][player_coordenadas[1] + 1] = 'c'

if player_coordenadas[0] + 1 < 10:
    if player_coordenadas[1] - 1 > -1:
        m_escondida[player_coordenadas[0] + 1][player_coordenadas[1] - 1] = 'c'
    m_escondida[player_coordenadas[0] + 1][player_coordenadas[1]] = 'c'
    if player_coordenadas[1] + 1 < 10:
        m_escondida[player_coordenadas[0] + 1][player_coordenadas[1] + 1] = 'c'

t = random.randint(0, 9)
y = random.randint(0, 9)

minas = 10  # when this changes change the other one too

while minas != 0:
    if (m_escondida[t][y] != '.') and (m_escondida[t][y] != 'M') and (m_escondida[t][y] != 'c'):
        m_escondida[t][y] = 'M'
        minas -= 1
    t = random.randint(0, 9)
    y = random.randint(0, 9)

minas = 10  # resets it for later use. change the one above too

# makes every none mine space except first point a point for number insrt algorithm to check
t = 0
y = 0
while t < 10:
    while y < 10:
        if (m_escondida[t][y] != '.') and (m_escondida[t][y] != 'M') and (m_escondida[t][y] != 'c'):
            m_escondida[t][y] = 'c'
        y += 1
    t += 1
    y = 0

# number insert algorithm for m_escondida board
t = 0
y = 0
mina_contador = 0
while t < 10:
    while y < 10:
        if (m_escondida[t][y] == 'c'):
            if t - 1 > -1:
                if y - 1 > -1:
                    if m_escondida[t - 1][y - 1] == 'M':
                        mina_contador += 1
                if y + 1 < 10:
                    if m_escondida[t - 1][y + 1] == 'M':
                        mina_contador += 1
                if m_escondida[t - 1][y] == 'M':
                    mina_contador += 1

            if y - 1 > -1:
                if m_escondida[t][y - 1] == 'M':
                    mina_contador += 1
            if y + 1 < 10:
                if m_escondida[t][y + 1] == 'M':
                    mina_contador += 1

            if t + 1 < 10:
                if y - 1 > -1:
                    if m_escondida[t + 1][y - 1] == 'M':
                        mina_contador += 1
                if y + 1 < 10:
                    if m_escondida[t + 1][y + 1] == 'M':
                        mina_contador += 1
                if m_escondida[t + 1][y] == 'M':
                    mina_contador += 1

            if mina_contador == 0:
                m_escondida[t][y] = '.'
            else:
                m_escondida[t][y] = mina_contador
                mina_contador = 0

        y += 1
    t += 1
    y = 0

# starting the game
abrir_mesa(player_coordenadas[0], player_coordenadas[1])

t = 0
while t < 11:
    if t == 0:
        print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
              game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
        print()
    else:
        print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
              game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
    t += 1

# playing the game
jogo = True
win = False

while jogo:
    print()
    jogada_escolhida = input("Ponha as coordenadas separadas C : L")
    print()

    if jogada_escolhida == 'kabum':
        t = 0
        while t < 10:
            print(m_escondida[t][0], ' ', m_escondida[t][1], ' ', m_escondida[t][2], ' ', m_escondida[t][3], ' ', m_escondida[t][4], ' ',
                  m_escondida[t][5], ' ', m_escondida[t][6], ' ', m_escondida[t][7], ' ', m_escondida[t][8], ' ', m_escondida[t][9])
            t += 1
        jogada_escolhida = input("Ponha as coordenadas separadas por :")
    elif jogada_escolhida == 'I am a total piece of shit, gg I win':
        jogada_escolhida = input("Você ganha no proximo acerto!")
        vencer_jogo()

    player_coordenadas = jogada_escolhida.split(':')
    player_coordenadas[0] = int(player_coordenadas[0]) - 1
    player_coordenadas[1] = int(player_coordenadas[1]) - 1

    if m_escondida[player_coordenadas[0]][player_coordenadas[1]] == 'M':
        jogo = False
        game[player_coordenadas[0] + 1][player_coordenadas[1] + 1] = m_escondida[player_coordenadas[0]][player_coordenadas[1]]
    elif m_escondida[player_coordenadas[0]][player_coordenadas[1]] == '.':
        game[player_coordenadas[0] + 1][player_coordenadas[1] + 1] = m_escondida[player_coordenadas[0]][player_coordenadas[1]]
        abrir_mesa(player_coordenadas[0], player_coordenadas[1])
    else:
        game[player_coordenadas[0] + 1][player_coordenadas[1] + 1] = m_escondida[player_coordenadas[0]][player_coordenadas[1]]

    t = 0
    while t < 11:
        if t == 0:
            print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
                  game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
            print()
        else:
            print(game[t][0], ' ', game[t][1], ' ', game[t][2], ' ', game[t][3], ' ', game[t][4], ' ', game[t][5], ' ',
                  game[t][6], ' ', game[t][7], ' ', game[t][8], ' ', game[t][9], ' ', game[t][10])
        t += 1

    print()

    NumberOSpaces = 0
    x = 1
    p = 1
    while x < 11:
        while p < 11:
            if game[x][p] == '#':
                NumberOSpaces += 1
            p += 1
        p = 1
        x += 1

    if NumberOSpaces == minas:
        win = True
        jogo = False

if win == True:
    print("\n\n\nVocê ganhou, parabéns, você é especial!")
else:
    print("\n\n\nVocê perdeu, era uma mina.")

print()
print()
input()