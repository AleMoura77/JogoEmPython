import random

def jogar():
    print("*****************")
    print("ADIVINHE O NUMERO")
    print("*****************")

    numero_secreto = random.randrange(0,101)
    rodada = 1
    pontos = 1000

    while(True):
        
        print("DIFICULDADE")
        print("(1) FACIL (2) MEDIO (3) DIFICIL")
        dificuldade = int(input("DIGITE A DIFICULDADE: "))

        if(dificuldade == 1):
            tentativa = 20
            break
        elif(dificuldade == 2):
            tentativa = 10
            break
        elif(dificuldade == 3):
            tentativa = 5
            break
        else:
            print("DIFICULDADE INVALIDA")
            

    for rodada in range(1, tentativa + 1):

        print("TENTATIVA {} DE {}".format(rodada, tentativa)) 

        numero_jogador = input("DIGITE UM NUMERO ENTRE 1 E 100: ")

        acertou = int(numero_jogador) == numero_secreto
        maior = int(numero_jogador) > numero_secreto
        menor = int(numero_jogador) < numero_secreto

        if(int(numero_jogador) < 1 or int(numero_jogador) > 100):
            print("NUMERO INVALIDO ")
            continue 

        if(acertou):
            print("VOCE ACERTOU E FEZ {} PONTOS".format(pontos))
            break
        else:
            if(maior): 
                print("VOCE ERROU! MAIOR DO QUE O NUMERO SECRETO")
            elif(menor): 
                print("VOCE ERROU! MENOR DO QUE O NUMERO SECRETO")
        pontos = pontos - abs(numero_secreto - int(numero_jogador))

    print(numero_secreto)
    print("FIM DO JOGO")

if(__name__ == "__main__"):
    jogar()