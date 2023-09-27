def jogar():
    print("JOGO DA FORCA")
    
    palavra_secreta = "banana"
    
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        
        chute = (input("Qual letra? ")).strip()
        
        posicao = 0
        
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
                (letra, posicao)
                print(letras_acertadas)
            posicao = posicao + 1    

        print("JOGANDO")

if(__name__ == "__main__"):
    jogar()