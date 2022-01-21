# matrix 3 x 3
#critica matriz 9 x9
#ctrl / pra comentar tudo
#CORES
red = '\033[1:31m'
green = '\033[1:32m'
blue = '\033[1:34m'
gray = '\033[1:37m'
cls = '\033[m'

print(blue, "=" * 25)
print(red, f'{"JOGO DA VELHA":^25}')
print(blue, "=" * 25, cls)

msg ="PARÁBENS JOGADOR UM GANHOU"

#JOGADORES
options ="XO"
geral = []

#Função vitoria

def vitoria():
    while True:
        pontos = 0
        jogador = ['', '']
        jogador[0] = input('Deseja jogar com X ou O: ').strip().upper()[0]
        if jogador[0] in options:
            jogador[1] = 'X' if jogador[0] != 'X' else 'O'
            break
        else:
            print(f'{red}', end='')
            print('Opção inválida. Tente novamente.')
            print(f'{cls}')

            for i in range(3):
                for j in range(3):
                    if num_1 or num_2 == board[i][j]:
                        board[i][j] = "X"
                        #LINHAS
                        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
                            pontos += 1
                            print(msg)
                        elif board[i][1] == "X" and board[i][2] == "X" and board[i][2] == "X":
                            pontos += 1
                            print(msg)
                        elif board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
                            pontos += 1
                            print(msg)
                            # COLUNAS
                        elif board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X":
                            pontos += 1
                            print(msg)
                        elif board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X":
                            pontos += 1
                            print(msg)
                        elif board[0][j] == "X" and board[1][j] == "X" and board[2][j] == "X":
                            pontos += 1
                            print(msg)
                            # DIAGONAIS
                        elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                            pontos += 1
                            print(msg)
                        elif board[2][0] == "X" and board[1][1] == "X" and board[2][0] == "X":
                            pontos += 1
                            print(msg)
                    return pontos

#DESENHO JOGO DA VELHA

board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

desenho = [print(f"{blue}|        |      |        |"),
            print(f"{blue}|    {red}{board[0][0]}{blue}   | {red} {board[0][1]}{blue}   |  {red}{board[0][2]}{blue}     |"),
            print(f"{blue}|  ------|------|------  |"),
            print(f"{blue}|    {red}{board[1][0]}{blue}   | {red} {board[1][1]}{blue}   |  {red}{board[1][2]}{blue}     |"),
            print(f"{blue}|  ------|------|------  |"),
            print(f"{blue}|    {red}{board[2][0]}{blue}   | {red} {board[2][1]}{blue}   |  {red}{board[2][2]}{blue}     |"),
            print(f"{blue}|        |      |        |")]

while True:

    print(blue, end='')
    num_1 = int(input("jogador 1 selecione a casa selecionada: "))
    num_2 = int(input("jogador 2 selecione a casa selecionada: "))
    print(cls, end='')

    # CONDIÇÃO
    if num_1 > 8 or num_1 < 0 or num_2 > 8 or num_2 < 0:
        print(red, end='')
        print("Essa não é uma opção válida, digite novamente!")
        print(cls, end='')

    else:
        print(desenho)
        for i in range(3):
            for j in range(3):
                   if vitoria()

























    #if num_1 == len(board[0][0]):
        #(board) == "X"





#print(palavra)

#while True:
    #print(blue, end='')
    #print(forca[abs(tentativas - 6)])
    #print(''.join(palpite), end='\n\n')

    #try:  # Vai tentar rodar
        #letra = str(input('Digite uma letra: ')).upper().strip()


    #except IndexError:  # erro que deu
        #print(red, 'Entrada inválida! Tente novamente.', cls, end='')

    #if len(letra) > 1:
        #print(red, end='')
        #print("Essa letra não é válida, digite novamente!")
        #print(cls, end='')
    #else:

