import random
from os import system, name


# Cabeçalho

def cabeçalho():
    
    print("\n Seja bem vindo(a) ao Jogo da Forca!")
    print("\n Você terá 6 chances de adivinhar o nome da fruta abaixo: \n")
    
    nome_fruta = fruta()
    n_de_letras = len(nome_fruta)
    blocos = " " + "_ " * n_de_letras
    
    print(blocos) 
    
    return nome_fruta, n_de_letras, blocos


# Escolhe uma fruta da lista

def fruta():
    
    frutas = ["melancia", "morango", "abacaxi", "cereja", "kiwi", "caju", "caqui", "manga"]
    
    fruta_escolhida = random.choice(frutas) 
    
    return fruta_escolhida


# Imagens possíveis:

def imagem_hangman(erros):
    
    imagens = [
        """
        -------
        |     |
        O     |
       \|/    |
        |     |
       / \    |
             --- """,

        """
        -------
        |     |
        O     |
       \|/    |
        |     |
       /      |
             --- """,
        """
        -------
        |     |
        O     |
       \|/    |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
       \|     |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
        |     |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
              |
              |
              |
             --- """,

        """
        -------
        |     |
              |
              |
              |
              |
             --- """
    ]
    
    
    print(imagens[-erros])
    
    return 
    

# Mudando os blocos para respostas corretas

def atualiza_blocos(resposta_certa, blocos_antigos, tentativa):
    
    indices = [i*2 + 1 for i in range(len(resposta_certa)) if resposta_certa[i] == tentativa]

    for index in indices:
        
        blocos_antigos_list = list(blocos_antigos)
        blocos_antigos_list[index] = tentativa
        blocos_antigos = ''.join(blocos_antigos_list)

    blocos_novos = blocos_antigos

    return blocos_novos

    
# Montando o Jogo    
    
def game():
    
    resposta_certa, n_de_blocos, blocos_originais = cabeçalho()
    n_erros = 0
    n_acertos = 0
    letras_escolhidas = []
    blocos_antigos = blocos_originais
    
    while n_erros <= 6:
    
        tentativa = input("\n Escolha uma letra: " )
        
        for i in tentativa:
            
            if i in resposta_certa:
                
                if i in letras_escolhidas:
                    
                    print("\n Você já escolheu essa letra. Tente outra.")
                    
                else:
                    
                    n_acertos += 1
                    letras_escolhidas.append(i)
                    novos_blocos = atualiza_blocos(resposta_certa, blocos_antigos, tentativa)
                    
                    print(novos_blocos)

                    blocos_antigos = novos_blocos
                    
                    if blocos_antigos.find("_") > 0:
                
                        print("\n Você esolheu bem!")
                        
                    else:
                        
                        return print("\n Parabéns, você conseguiu! :)")
                
            else:
                
                n_erros += 1
                tentativas_restantes = 6 - n_erros
                imagem_hangman(n_erros)
                
                if i in letras_escolhidas:
                    
                    print("\n Você já escolheu essa letra, e errou novamente! Tente novamente, você ainda tem", 6 - n_erros, "tentativas restantes.")
                
                else:
                    
                    letras_escolhidas.append(i)
                    
                    if tentativas_restantes > 0:
                    
                        print("\n Você esolheu mal! Tente novamente, você ainda tem", 6 - n_erros, "tentativas restantes.")
                        
                    else:
                        
                        print("\n Você esolheu mal! Pense bem, essa é a sua última tentativa!")
                        print("\n Game Over! A fruta correta é:", resposta_certa)
    
    return 
    
    
game()
    
    
    
    
    
    
    
    