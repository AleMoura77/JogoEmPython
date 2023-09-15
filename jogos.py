import forca
import adivinhacao

def escolhaJogo():
    print("******************")
    print("**Escolha o jogo**")
    print("******************")

    while(True):
        print("(1)FORCA (2)ADIVINHAÇÃO")

        jogo = int(input("Qual jogo: "))

        if(jogo == 1):
            print("FORCA")
            forca.jogar()
            break
        elif(jogo == 2):
            print("ADIVINHAÇÃO")
            adivinhacao.jogar()
            break
        else:
            print("JOGO NÃO ENCOTRADO")

if(__name__ == "__main__"):
    escolhaJogo()
