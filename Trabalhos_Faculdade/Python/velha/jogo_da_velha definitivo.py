# critica  espaço vazio
# critica 2 ou maais numeros
# critica letra

# erros resolvidos usando um try..except

#Desenho do vasco
 # ⢀⢀⢀⢀⢀⢀⢀⢀⡤⠤⠒⠒⠒⠛⠉⣉⣉⡉⠛⠒⠒⠒⠦⢤⢀⢀⢀⢀⢀⢀⢀⢀\n'
 #  ⢀⢀⢀⢀⢀⢀⢀⣧⠀⣶⣿⣿⣿⡿⠛⣿⣿⣿⣿⣿⣶⠀⣸⢀⢀⢀⢀⢀⢀⢀⢀ \n'
 #  ⢀⢀⢀⢀⢀⢀⢀⢸⠀⣿⣿⣿⣯⣴⡇⣿⣿⣿⣿⣿⣿⠀⣿⢀⢀⢀⢀⢀⢀⢀⢀ \n'
 #  ⡖⠦⠤⠤⠤⠖⢋⣠⣿⣿⣿⣿⣇⠤⠤⠤⠤⠀⠿⠿⠋⡈⠀⡉⠲⠤⠤⠤⠴⢶ \n'
 #  ⡖⠦⠤⠤⠤⠖⢋⣠⣿⣿⣿⣿⣇⠤⠤⠤⠤⠀⠿⠿⠋⡈⠀⡉⠲⠤⠤⠤⠴⢶ \n'
 #  ⡇⢰⣶⣶⣶⣾⣿⣿⣿⣿⣏⠉⠉⠁⠁⠁⠁⠁⠁⠈⠈⠈⠈⠁⠈⠈⢀⡄⡆⢸.\n'
 #  ⡇⢸⣿⠿⢰⣒⠛⢿⣟⠛⠛⢒⢒⡆⠠⠄⠄⠄⠠⢀⢀⠂⠈⠈⠈⣀⣴⣿⡇⢸.\n'
 #  ⡇⢸⣏⢸⢘⣉⢼⣿⣿⡀⢂⠆⠆⠆⠄⠄⠆⠄⠄⠄⠄⠄⠘⣠⣾⣿⣿⣿⡇⢸.\n'
 #  ⡇⢸⣿⣦⢍⣉⡆⢶⣿⠇⢀⡀⢀⢀⢠⡈⢿⠏⣠⢀⢀⢀⢠⣿⣿⣿⣿⣿⡇⢸.\n'
 #  ⢷⠘⣿⣷⣶⣿⣿⣿⠿⢀⢀⠇⢀⢀⠸⠛⣿⡛⠻⢀⢀⢀⣸⣿⣿⣿⣿⣿⠃⡞.\n'
 #  ⢸⡀⣿⣿⣿⡿⠋⠁⢂⠀⠤⢀⢀⢀⢀⣈⣉⠍⡀⢀⢀⣠⣿⣿⣿⣿⣿⣿⢀⡇.\n'
 #  ⢀⣇⠸⠿⠋⢀⢀⠁⢀⢐⠁⣤⢔⡪⠍⣒⡞⡔⢍⣤⣾⣿⣿⣿⣿⣿⣿⠇⣸⢀.\n'
 #  ⢀⠘⡄⢂⢀⢀⢀⢀⢀⠀⠪⢦⣕⡢⠥⢰⢳⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⠃⢀.\n'
 #  ⢀⢀⠹⡄⠂⢀⢀⠤⠤⣩⡶⠭⣭⠿⠯⣭⡿⠭⢽⣿⠷⣿⣿⣿⣿⠟⢠⠏⢀⢀.\n'
 #  ⢀⢀⢀⠘⣆⠁⡀⣠⣾⣿⣿⣿⣛⢻⠿⠿⠿⠛⣻⣿⣿⣿⣿⣿⠋⡰⠃⢀⢀⢀.\n'
 #    ⢀⢀⢀⠈⠳⡈⠻⣿⣿⣿⣿⣿⢀⢾⣿⠏⣼⣿⣿⣿⣿⠟⢁⠞....... \n'
 #     ⢀⢀⢀⠈⠳⢤⡀....⠄⠄⠄⠄⠄⠄⠄⠄⠄⡤⠞⠁......\n'
 #  ⠄⠄⠄⠄⠄⠄⠄⠄⠈⠳⢤⡀....⢀ ..⢀⠞⠁⠄⠄⠄⠄⠄⠄⠄..\n '
 #  ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠲⢤⡤⠖⠉⠄⠄⠄⠄........ ']

#Bruno Corona Braga


# CORES
red = '\033[1:31m'
green = '\033[1:32m'
blue = '\033[1:34m'
gray = '\033[1:37m'
cls = '\033[m'
yellow = '\033[1m'
yellow = '\033[93m'

taça = ["   ___________\n"
        "  .-\:      /-.\n"
        " | (|:.     |) |\n"
        "   -|:.     |-"'\n'
        "     \::.  /\n"
        "      ::..\n"
        "       ) (\n"
        "     |_. ._|"]


# Função JOGADORES
def bandeiras():
    bandeiras = [
    f'{blue}Parabéns, o {red}PRIMEIRO{blue} jogador é {red}flamenguista! {blue}             Que tristeza, o {red}SEGUNDO {blue}Jogador{red} é vascaíno! {blue}=( \n'
    f'                                                                                                \n'
    f'{red} ⡏⠉⠉⠩⢭⣉⣩⣭⣉⠉⠉⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿               {blue}   ⢀⢀⢀⢀⢀⢀⢀⢀⡤⠤⠒⠒⠒⠛⠉⣉⣉⡉⠛⠒⠒⠒⠦⢤⢀⢀⢀⢀⢀⢀⢀⢀\n'
    f'{red} ⡇{cls}⠄⠄⣠⠆⣿⣿⢤⣽⢷⣠⣤⡇{red}⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿               {blue}    ⢀⢀⢀⢀⢀⢀⢀⢀⣧⠀⣶⣿⣿⣿⡿⠛⣿⣿⣿⣿⣿⣶⠀⣸⢀⢀⢀⢀⢀⢀⢀⢀ \n' 
    f'{red} ⡇{cls}⠄⣼⠃⠄⣿⠉⢸⡇⣽⢃⡀⠣{red}⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⢸               {blue}    ⢀⢀⢀⢀⢀⢀⢀⢀⢸⠀⣿⣿⣿⣯⣴⡇⣿⣿⣿⣿⣿⣿⠀⣿⢀⢀⢀⢀⢀⢀⢀⢀ \n'
    f'{red} ⡇{cls}⠈⢿⡄⠄⣿⠦⣼⡻⠶⣾⠄⠄{red}⢸⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⢸               {blue}     ⡖⠦⠤⠤⠤⠖⢋⣠⣿⣿⣿⣿⣇⠤⠤⠤⠤⠀⠿⠿⠋⡈⠀⡉⠲⠤⠤⠤⠴⢶ \n'
    f'{red} ⡇{cls}⠄⠈⠳⢦⣟⣠⢸⡱⡄⠋⠄⠄{red}⢸⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣾               {blue}     ⡖⠦⠤⠤⠤⠖⢋⣠⣿⣿⣿⣿⣇⠤⠤⠤⠤⠀⠿⠿⠋⡈⠀⡉⠲⠤⠤⠤⠴⢶ \n'
    f'{red} ⡇{cls}⠄⠄⠄⠼⠻⠄⠘⠓⠙⠛⠄⠄{red}⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿               {blue}     ⡇⢰⣶⣶⣶⣾⣿⣿⣿⣿⣏⠉⠉⠁⠁⠁⠁⠁⠁⠈⠈⠈⠈⠁⠈⠈⢀⡄⡆⢸.\n'
    f'{red} ⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹               {blue}     ⡇⢸⣿⠿⢰⣒⠛⢿⣟⠛⠛⢒⢒⡆⠠⠄⠄⠄⠠⢀⢀⠂⠈⠈⠈⣀⣴⣿⡇⢸.\n' 
    f'{red} ⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡼               {blue}     ⡇⢸⣏⢸⢘⣉⢼⣿⣿⡀⢂⠆⠆⠆⠄⠄⠆⠄⠄⠄⠄⠄⠘⣠⣾⣿⣿⣿⡇⢸.\n'              
    f'{red} ⢸⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡇               {blue}     ⡇⢸⣿⣦⢍⣉⡆⢶⣿⠇⢀⡀⢀⢀{red}⢠⡈⢿⠏⣠{cls}{blue}⢀⢀⢀⢠⣿⣿⣿⣿⣿⡇⢸.\n' 
    f'{red} ⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁               {blue}     ⢷⠘⣿⣷⣶⣿⣿⣿⠿⢀⢀⠇⢀⢀{red}⠸⠛⣿⡛⠻{cls}{blue}⢀⢀⢀⣸⣿⣿⣿⣿⣿⠃⡞.\n' 
    f'{red} ⠄⠸⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⠇⠄               {blue}     ⢸⡀⣿⣿⣿⡿⠋⠁⢂⠀⠤⢀⢀⢀⢀{red}⣈⣉⠍⡀{cls}{blue}⢀⢀⣠⣿⣿⣿⣿⣿⣿⢀⡇.\n' 
    f'{red} ⠄⠄⠹⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠏⠄⠄               {blue}     ⢀⣇⠸⠿⠋⢀⢀⠁⢀⢐⠁⣤⢔⡪⠍⣒⡞⡔⢍⣤⣾⣿⣿⣿⣿⣿⣿⠇⣸⢀.\n' 
    f'{red} ⠄⠄⠄⠙⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⠋⠄⠄⠄               {blue}     ⢀⠘⡄⢂⢀⢀⢀⢀⢀⠀⠪⢦⣕⡢⠥⢰⢳⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⠃⢀.\n' 
    f'{red} ⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠄⠄⠄⠄               {blue}     ⢀⢀⠹⡄⠂⢀⢀⠤⠤⣩⡶⠭⣭⠿⠯⣭⡿⠭⢽⣿⠷⣿⣿⣿⣿⠟⢠⠏⢀⢀.\n' 
    f'{red} ⠄⠄⠄⠄⠄⠄⠙⠿⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢛⠟⠋⠄⠄⠄⠄⠄⠄               {blue}     ⢀⢀⢀⠘⣆⠁⡀⣠⣾⣿⣿⣿⣛⢻⠿⠿⠿⠛⣻⣿⣿⣿⣿⣿⠋⡰⠃⢀⢀⢀.\n' 
    f'{red} ⠄⠄⠄⠄⠄⠄⠄⠄⠈⠳⢤⡀....⢀⡤⠞⠁⠄⠄⠄⠄⠄⠄⠄..              {blue}       ⢀⢀⢀⢀⠈⠳⡈⠻⣿⣿⣿⣿⣿⢀⢾⣿⠏⣼⣿⣿⣿⣿⠟⢁⠞....... \n'
    f'{red} ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠲⢤⡤⠖⠉⠄⠄⠄⠄........              {blue}        ⢀⢀⢀⢀ ⠈⠳⢤⡀....⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡤⠞⠁......\n'
    f'                                                            ⠄⠄⠄⠄⠄⠄⠄⠄⠈⠳⢤⡀....⢀ ..⢀⠞⠁⠄⠄⠄⠄⠄⠄⠄..\n '
    f'                                                            ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠲⢤⡤⠖⠉⠄⠄⠄⠄........ ']
    print("\n".join(bandeiras))
    print(cls)
    return

#Função vitoria/desenho

def vitoria():
    global resultado
    print(yellow, end='')
    if str(board[1][1]) in 'XO':
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == jogador[0]:
                resultado = (f'{yellow}JOGADOR 1 - GANHOU!')
                return
            elif board[0][0] == jogador[1]:
                resultado = (f'{yellow}JOGADOR DOIS - GANHOU!')
                return
        elif board[2][0] == board[1][1] == board[0][2]:
            if board[2][0] == jogador[0]:
                resultado = (f'{yellow}JOGADOR UM - GANHOU!')
                return
            elif board[2][0] == jogador[1]:
                resultado = (f'{yellow}JOGADOR DOIS - GANHOU!')
                return
    for c in range(3):
        if str(board[c][c]) in 'XO':
            if board[c][0] == board[c][1] == board[c][2]:  # HORIZONTAL
                if board[c][0] == jogador[0]:
                    resultado = (f'{yellow}JOGADOR UM - GANHOU!')
                    return
                elif board[c][0] == jogador[1]:
                    resultado = (f'{yellow}JOGADOR DOIS - GANHOU!')
                    return
            elif board[0][c] == board[1][c] == board[2][c]:  # VERTICAL
                if board[0][c] == jogador[0]:
                    resultado = (f'{yellow}JOGADOR UM - GANHOU!')
                    return
                elif board[0][c] == jogador[1]:
                    resultado = (f'{yellow}JOGADOR DOIS - GANHOU!')
                    return
    print(cls, end='')

def desenha():
    print(blue, end='')
    print('|       |     |        |')
    for linha in range(3):
        # SE for X ou O ele já coloca em AMARELO SENÃO coloca em VERMELHO
        item_1 = f'{yellow}{board[linha][0]}{cls}' if str(board[linha][0]) in 'XO' else f'{red}{board[linha][0]}{cls}'
        item_2 = f'{yellow}{board[linha][1]}{cls}' if str(board[linha][1]) in 'XO' else f'{red}{board[linha][1]}{cls}'
        item_3 = f'{yellow}{board[linha][2]}{cls}' if str(board[linha][2]) in 'XO' else f'{red}{board[linha][2]}{cls}'
        print(f'{blue}|    {item_1}  {blue}|  {item_2}  {blue}|  {item_3}     {blue}|')
        if linha != 2:
            print('|  -----|-----|------  |')
        linha += 3
    print('|       |     |        |')
    print(cls, end='')

print(blue, "=" * 36)
print(red, f'{"JOGO DA VELHA":^36}')
print(blue, "=" * 36, cls)

while True:
    numeros_validos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    jogadas = 0
    jogador = ['', '']
    resultado = None
    print(blue, end='')
    try:
        jogador[0] = input(f'{blue}Jogador {red}UM{blue} - Deseja jogar com {yellow}X{blue} ou {yellow}O{blue}? \n').upper().strip()[0]
        if jogador[0] in 'XO':
            jogador[1] = 'X' if jogador[0] != 'X' else 'O'
            bandeiras()
            print(cls, end='')
        else:
            print(red, 'Entrada inválida! Tente novamente.', cls, end='')
            continue

    except ValueError:
        print(red, 'Entrada inválida! Tente novamente.', cls, end='')
        continue
    else:
        while resultado is None and jogadas < 9:
            for c in range(2):
                if resultado is not None:
                    break  # Se acabou a partida, ele SAI do loop (for)
                while True:  # loop aqui
                    desenha()
                    print(blue, end='')
                    try:
                        posicao = int(input(f"jogador {yellow}{c + 1}{blue} selecione a casa: "))
                    except ValueError:  # Qualquer coisa que NÃO for um número, vai da error
                        print(red, end='')
                        print("Essa não é uma opção válida, digite novamente!")
                        print(cls, end='')
                        continue  # Para voltar para o INÍCIO do loop
                    else:  # Se não tiver erros, executa o código abaixo
                        if posicao not in numeros_validos:
                            print(red, end='')
                            print("Essa não é uma opção válida, digite novamente!")
                            print(cls, end='')
                            continue  # Para voltar para o INÍCIO do loop
                        else:
                            numeros_validos.remove(posicao)
                            for i in range(3):
                                for j in range(3):
                                    if posicao == board[i][j]:
                                        board[i][j] = jogador[c]

                            vitoria()

                            jogadas += 1
                            if resultado is not None:
                                desenha()
                                print(resultado)
                                print("\n".join(taça))
                                break
                            elif jogadas == 9:
                                desenha()
                                print(f"{yellow} EMPATOU!")
                                break
                            else:
                                break
