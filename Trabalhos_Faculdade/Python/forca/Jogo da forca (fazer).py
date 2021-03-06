# jogo da forca, se erra 6 vezes perde o jogo, baixar lista de palavras
# função pra palavra aleatoria ( baixar o arquivo)

#Nome: Bruno Corona Braga

import random

# CORES
red = '\033[1:31m'
green = '\033[1:32m'
blue = '\033[1:34m'
gray = '\033[1:37m'
cls = '\033[m'


def sortear_palavra():

    arquivo = open("br-sem-acentos.txt")
    linhas = arquivo.readlines()
    palavra = ''
    while len(palavra) < 5 or len(palavra) > 10:
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]
    palavra = palavra.upper()
    arquivo.close()
    return palavra


print(blue, "=" * 20)
print(red, "JOGO DA FORCA")
print(blue, "=" * 20, cls)
forca = ["   |¯¯¯¯¯¯¯|\n"
         "           |\n"
         "           |\n"
         "           |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "           |\n"
         "           |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "   |       |\n"
         "           |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "  /|       |\n"
         "           |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "  /|\      |\n"
         "           |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "  /|\      |\n"
         "  /        |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ",
         "   |¯¯¯¯¯¯¯|\n"
         "   O       |\n"
         "  /|\      |\n"
         "  / \      |\n"
         "           |\n"
         " ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   "
         ]

palavra = sortear_palavra()
letras_disponiveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z']
letras_usadas = []  # Letras já digitadas pelo usuário
resposta = []  # A palavra sorteada como uma lista
palpite = []  # Palpite que será testado pelo usuário
tentativas = 6  # Total de tentativas permitidas

for c in range(0, len(palavra) - 1):
    resposta.append(palavra[c].upper())
    palpite.append('_')

#print(palavra)

while True:
    print(blue, end='')
    print(forca[abs(tentativas - 6)])
    print(''.join(palpite), end='\n\n')

    try:  # Vai tentar rodar
        letra = str(input('Digite uma letra: ')).upper().strip()


    except IndexError:  # erro que deu
        print(red, 'Entrada inválida! Tente novamente.', cls, end='')

    if len(letra) > 1:
        print(red, end='')
        print("Essa letra não é válida, digite novamente!")
        print(cls, end='')
    else:
        if letra.isalpha():
            if letra not in letras_usadas:
                letras_usadas.append(letra)
                letras_disponiveis.remove(letra)
                letras_usadas.sort()
                print(red, end='')
                print(f'letras usadas: {" ".join(letras_usadas)}')
                print(green, end='')
                print(f'letras disponíveis: {" ".join(letras_disponiveis)}')

                if letra in resposta:
                    for c in range(0, len(resposta)):
                        if resposta[c] == letra:
                            palpite[c] = letra
                    if ''.join(palpite) == ''.join(resposta):
                        print(green, end='')
                        print('Parabens voce ganhou!')
                        print(f'A palavra era: {palavra}')
                        break
                else:
                    tentativas -= 1
                    print(red, end='')
                    print(f'A letra \'{letra}\' não existe nessa palavra.')
                    print(f'Tentativas restantes: {tentativas}')
                    if tentativas <= 0:
                        print(red, end='')
                        print(forca[6])
                        print(f'GAME OVER!')
                        print(green, end='')
                        print(f'A palavra era: {palavra}')
                        break
            else:
                print(red, end='')
                print(f'A letra \'{letra}\' já foi usada. Tente novamente.')
                print(gray, end='')
                print(f'letras usadas: {" ".join(letras_usadas)}')
                print(green, end='')
                print(f'letras disponíveis: {" ".join(letras_disponiveis)}')
                print(cls, end='')
        else:
            print(red, "Essa não é uma letra válida. Digite novamevente")
