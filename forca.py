import random

def jogar():
    imprime_abertura()
    palavra_secreta = carrega_palavra()
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0 
    
    while(not enforcou and not acertou):
        
        chute = letra_escolhida()
        
        if(chute in palavra_secreta):
                letra_correta(chute, letras_acertadas, palavra_secreta)
        else: 
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas            
        print(letras_acertadas)
        
    if(acertou):
        imprime_mensagem_ganhador()
    else: 
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_abertura():
    print("********************************")
    print("***BEM VINDO AO JOGO DA FORCA***")
    print("********************************")
    
def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta
    
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def letra_escolhida():
    return (input("Qual letra? ")).strip().upper()

def letra_correta(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[posicao] = letra
            (letra, posicao)   
        posicao += 1    

def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")    
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()