# NOME: Bruno Corona Braga
#       Aline Pires Rodrigues



# CORES
red = '\033[1:31m'
green = '\033[1:32m'
blue = '\033[1:34m'
gray = '\033[1:37m'
cls = '\033[m'
yellow = '\033[1m'
yellow = '\033[93m'

# Imports
import time

# globals
vazio = " "
# bem vindo
print(f"""{blue}
                                           |_
                                       ---/ |
                                       ___\_|__
                                      /| o  o |
                       ___           / |______|\          ___
                  ====/___\  ,------,--|------|--.       /___\====
    _________________,|- -|,/---------------------\.____,|- -|,______________
    \                       \. . . . . . . . . . . ./                       /     , 
 ,   \   o           o           o           o           o           o     /    ,   )',    ,     ,(
=)'===\___________________________________________________________________/==="('=='""=='"(=='-'  ',
____________________________________________________________________________________________________
____________________________________________________________________________________________________
                            {red}Bem vindo ao Batalha Naval
               <------------------------------------------------->
""")

medalha = (f"""         {yellow} |@@@@|     |####|
          |@@@@|     |####|
          |@@@@|     |####|
          \@@@@|     |####/
           \@@@|     |###/
            `@@|_____|##'
                 (O)
              .-'''''-.
            .'  * * *  `.
           :  *       *  :
          :~ P L A Y E R ~:
          : ~ A W A R D ~ :
           :  *       *  :
            `.  * * *  .'
              `-.....-'   """)
# Regras
print(f"""{red}Regras:{blue}
-> Player 1 posiciona o navio.
-> Player 2 atira no navio.
-> Coloque as coordenadas. Ex. A1, C4, B3
-> Jogador 1 terá 5 navios para colocar, e jogador 2 terá 13 tentativas.
""")

# tempo
time.sleep(1)

# listas global
movimentos_possiveis = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1",
                        "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]
board = [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio,
         vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio]
board2 = [vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio,
          vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio, vazio]
jogada_feita = []
acertos = []
tentativas_feitas = []
poss = "ABCDE"


# board jogador 1 posição
def board_one():
    print(f" | {red}1{blue} | {red}2{blue} | {red}3{blue} | {red}4{blue} | {red}5{blue} |")
    print(f" |___|___|___|___|___|")
    print(f"{red}A{blue}|", board[0], "|", board[1], "|", board[2], "|", board[3], "|", board[4], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}B{blue}|", board[5], "|", board[6], "|", board[7], "|", board[8], "|", board[9], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}C{blue}|", board[10], "|", board[11], "|", board[12], "|", board[13], "|", board[14], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}D{blue}|", board[15], "|", board[16], "|", board[17], "|", board[18], "|", board[19], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}E{blue}|", board[20], "|", board[21], "|", board[22], "|", board[23], "|", board[24], "|")
    print(f" |___|___|___|___|___|")


# board jogador 2 atirar
def board_two():
    print(f" | {red}1{blue} | {red}2{blue} | {red}3{blue} | {red}4{blue} | {red}5{blue} |")
    print(f" |___|___|___|___|___|")
    print(f"{red}A{blue}|", board2[0], "|", board2[1], "|", board2[2], "|", board2[3], "|", board2[4], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}B{blue}|", board2[5], "|", board2[6], "|", board2[7], "|", board2[8], "|", board2[9], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}C{blue}|", board2[10], "|", board2[11], "|", board2[12], "|", board2[13], "|", board2[14], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}D{blue}|", board2[15], "|", board2[16], "|", board2[17], "|", board2[18], "|", board2[19], "|")
    print(f" |___|___|___|___|___|")
    print(f"{red}E{blue}|", board2[20], "|", board2[21], "|", board2[22], "|", board2[23], "|", board2[24], "|")
    print(f" |___|___|___|___|___|")


# player 1 posição
def player1_move():
    for counter in range(0, 5):
        while True:
            jogada = input("Aonde você quer jogar? ").strip().upper()
            if jogada.isalnum():
                if jogada[0].isalpha() and jogada[1:].isnumeric() and 0 < int(jogada[1:]) < 6 and jogada[0] in poss:
                    jogada_feita.append(jogada)
                    # Navios = posição em  movimentos_possiveis
                    navios = movimentos_possiveis.index(jogada)
                    # coloca x na posição do navio
                    board[navios] = "X"
                    board_one()
                    break
                else:
                    print(f"{red}Essa não é uma jogada valida, tente novamente!{blue}")
            else:
                print(f"{red}Essa não é uma jogada valida, tente novamente!{blue}")
    troca_player = input("Aperte enter para esconder o jogador um. jogador 2 agora vai atacar: ")
    board_two()


# player 2 ataque
def user2_move():
    print("DICA:\nX = acertou")
    print("O = não acertou")
    time.sleep(1)
    # tentativas de ataque do 2 player
    tiros_restantes = 13
    for i in range(0, 13):
        # pergunta ao jogador 2 aonde ele quer atirar
        while True:
            tiros = input(f"{red}Canhões prontos!{blue} Adivinhe aonde os navios do jogador um estão: ").strip().upper()
            if tiros.isalnum():
                if tiros[0].isalpha() and tiros[1:].isnumeric() and 0 < int(tiros[1:]) < 6 and tiros[0] in poss:
                    tentativas_feitas.append(tiros)
                    tiros_board = movimentos_possiveis.index(tiros)
                    # player 2 board vai mostrar X por acerto e O por erro.
                    if tiros in (jogada_feita):
                        board2[tiros_board] = "X"
                        board_two()
                    else:
                        board2[tiros_board] = "O"
                        board_two()
                    # se os tiros do jogador 2 estiverem na lista do jogador 1 appends como acerto.
                    if tiros in jogada_feita:
                        print("Ataques feitos: ", tentativas_feitas)
                        tiros_restantes -= 1
                        acertos.append(tiros)
                        print("Acertou! você tem:", tiros_restantes, "tiros restantes!")
                    else:
                        tiros_restantes -= 1
                        print(f"{red}ERROOU{blue}, tente de novo. Você tem:", tiros_restantes, "tiros restantes.")
                        print(tentativas_feitas)
                    # Compara acerto com as jogadas se forem iguais o jogador 2 ganha.
                    if len(acertos) == len(jogada_feita):
                        player_2_win()
                        return None
                        break
                else:
                    print(f"{red}Essa não é uma jogada valida, tente novamente!{blue}")
            else:
                print(f"{red}Essa não é uma jogada valida, tente novamente!{blue}")
    # se acabar as tentativas do jogador 2, jogador 1 ganha.
    if tiros_restantes == 0:
        player_1_win()


# player 2 ganhou
def player_2_win():
    print(f"{yellow}Player 2 ganhou!{blue} Player 2 afundou todos os navios do player 1.")
    print(medalha)
    return None


# player 1 ganhou
def player_1_win():
    print(f"{yellow}Player 1 ganhou!{blue} Player 2 não conseguiu afundar todos os navios inimigos.")
    print(medalha)
    return None


# jogo
def jogo():
    board_one()
    player1_move()
    user2_move()


jogo()
