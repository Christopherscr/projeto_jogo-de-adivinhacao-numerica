# Este é um jogo de adivinhação numérica

import math
import random

limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))

x = random.randint(limite_inferior, limite_superior)
tentativas = round(math.log(limite_superior - limite_inferior + 1, 2))

print("\nVocê tem ", tentativas, " chances para adivinhar o número inteiro!\n")

contador = 0

adivinhado = False

while contador < tentativas:
    palpite = int(input("Adivinhe um número: "))
    contador += 1

    if x == palpite:
        if contador == 1:
            print("Parabéns!! Você acertou na primeira tentativa.")
        else:
            print("Parabéns!! Você acertou em {} tentativas.".format(contador))
        adivinhado = True
        break
    elif x > palpite:
        print("Você adivinhou muito baixo!\n")
    elif x < palpite:
        print("Você adivinhou muito alto!\n")

if not adivinhado:
    print("O número é {}".format(x))
    print("Boa sorte na próxima vez!")
