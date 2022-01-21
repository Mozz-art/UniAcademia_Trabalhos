#Bruno Corona Braga
#Aline Pires Rodrigues

import random

blue = '\033[1:34m'
gray = '\033[1:37m'
green = '\033[1:32m'
red = '\033[1:31m'
yellow = '\033[33m'
cls = '\033[m'


def imprime(A):  # Função para imprimir a matriz do jogador

    print(blue, "=" * 36)
    print(red, f'{"Campo Minado":^36}')
    print(blue, "=" * 36, cls)

    print(f"\t{red} 0   1   2   3   4   5   6   7   8   9{cls}")
    print()
    for i in range(matriz):
        print(f'{red}{i}{cls}', end='\t')
        for j in range(matriz):
            print(blue, A[i][j], cls, end="\t")
        print()
    print()


# Cria as matrizes A e B

matriz = 10

B = [None] * matriz

for i in range(matriz):
    B[i] = [0] * matriz

for i in range(matriz):
    for j in range(matriz):
        B[i][j] = 0

A = [None] * matriz

for i in range(matriz):
    A[i] = [0] * matriz

for i in range(matriz):
    for j in range(matriz):
        A[i][j] = f'{blue}-'


def bombas(B):  # Põe as bombas no tabuleiro

    bombas = 5

    for t in range(bombas):
        i = random.randint(0, 9)
        j = random.randint(0, 9)

        while B[i][j] == 'M':
            i = random.randint(0, 9)
            j = random.randint(0, 9)

        B[i][j] = 'M'


def valid(B, i, j):  # Valida se o digitado está dentro da matriz

    matriz = 10

    return 0 <= i < matriz and 0 <= j < matriz


def valid2(B, i, j):  # Valida se o comando é uma bomba ou não
    if B[i][j] == 'M':
        return False
    else:
        return True


def vizinhos(B):  # Acha o valor em volta de acordo com o posicionamento das bombas
    matriz = 10
    for i in range(matriz):
        for j in range(matriz):
            if B[i][j] == 'M':
                if valid(B, i - 1, j):
                    if valid2(B, i - 1, j):
                        B[i - 1][j] += 1
                if valid(B, i + 1, j):
                    if valid2(B, i + 1, j):
                        B[i + 1][j] += 1
                if valid(B, i, j + 1):
                    if valid2(B, i, j + 1):
                        B[i][j + 1] += 1
                if valid(B, i, j - 1):
                    if valid2(B, i, j - 1):
                        B[i][j - 1] += 1
                if valid(B, i - 1, j + 1):
                    if valid2(B, i - 1, j + 1):
                        B[i - 1][j + 1] += 1
                if valid(B, i - 1, j - 1):
                    if valid2(B, i - 1, j - 1):
                        B[i - 1][j - 1] += 1
                if valid(B, i + 1, j + 1):
                    if valid2(B, i + 1, j + 1):
                        B[i + 1][j + 1] += 1
                if valid(B, i + 1, j - 1):
                    if valid2(B, i + 1, j - 1):
                        B[i + 1][j - 1] += 1


# Abre espaços vazios
def abrirvazios(i, j, B, A):
    A[i][j] = 0
    for n in range(i - 1, i + 2, 1):
        for m in range(j - 1, j + 2, 1):
            if 0 <= n <= 9 and 0 <= m <= 9:
                if B[n][m] == 0 and A[n][m] != 0:
                    abrirvazios(n, m, B, A)
                elif 1 <= B[n][m] <= 9:
                    A[n][m] = B[n][m]


#


def entrada(B):  # Dá opção de ações, recebe as entradas e verifica o que são no tabuleiro
    game = True
    cont_bombas_falso = 5
    cont_bombas_real = 5
    while game:
        tipo_entrada = input(f"{blue}Selecione o tipo de entrada desejada, F para bandeira e S para selecionar ação: ")
        while tipo_entrada != 'S' and tipo_entrada != 's' and tipo_entrada != 'f' and tipo_entrada != 'F':
            tipo_entrada = input(f"{red}Input inválido. Selecione o tipo de entrada desejada, F para bandeira e S para selecionar ação: ")
        if tipo_entrada == 'S' or tipo_entrada == 's':
            print(f"{blue}Selecione a coordenada desejada para ação (linha, coluna): ")
            i = int(input(f"{blue}Coluna: "))
            while i < 0 or i > 9:
                i = int(input(f"{red}Input inválido. Digite um número entre 0 e 9 para seu linha: "))
            j = int(input(f"{blue}linha: "))
            while j < 0 or j > 9:
                j = int(input(f"{red}Input inválido. Digite um número entre 0 e 9 para seu coluna: "))
            print()
            if B[i][j] == 'M':
                print(f"{red}Acertou uma Bomba. Game Over.")
                imprime(B)
                game = False
            elif B[i][j] == 0:
                abrirvazios(i, j, B, A)
                imprime(A)
                game = True
                print(f"{blue}Bombas restantes: ", cont_bombas_falso)
            else:
                A[i][j] = f'{blue}{B[i][j]}{cls}'
                imprime(A)
                game = True
                print(f"{blue}Bombas restantes: ", cont_bombas_falso)
        elif tipo_entrada in 'fF':
            print(f"{blue}Seleciona a coordenada desejada para bandeira (linha, coluna): ")
            i = int(input("linha: "))
            while i < 0 or i > 9:
                i = int(input(f"{red}Input inválido. Digite um número entre 0 e 9 para seu linha: "))
            j = int(input("coluna: "))
            while j < 0 or j > 9:
                j = int(input(f"{red}Input inválido. Digite um número entre 0 e 9 para seu coluna: "))
            print("\n")
            if B[i][j] == 'M':
                cont_bombas_real -= 1
            if A[i][j] == 'F':
                print(f"{red}Já está marcado com uma bandeira.")
                print(f"{blue}Bombas restantes: ", cont_bombas_falso)
                print()

                imprime(A)

                game = True

            elif A[i][j] != 'F':

                A[i][j] = 'F'

                imprime(A)
                print()
                cont_bombas_falso -= 1
                print(f"{blue}Bombas restantes: ", cont_bombas_falso)

                game = True

            if cont_bombas_real == 0:
                print(f"{yellow}Todas as bombas foram eliminadas! Você ganhou!")
                game = False


def playgame():  # Função principal(main)
    print(f'''{blue}Regras: Coloque a bandeira em todas as 15 bombas para ganhar o jogo. 
        \nPara selecionar um comando digite S para ação e F para marcar uma bandeira. 
        \nlinha e coluna estão entre 0 e 9.''')
    print()
    matriz = 10
    bombas(B)
    vizinhos(B)
    imprime(A)
    entrada(B)


playgame()
