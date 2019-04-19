# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionario
import time
import colorama
from colorama import Fore, Back, Style, init
<<<<<<< HEAD
def carregar_cenarios():
    cenarios = {
            "inicio": {
            "titulo": "SAGUAO DO PERIGO",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
            "andar professor": {
                    "titulo": "ANDAR DO DESESPERO",
                    "descricao": "Voce chegou ao andar da sala do seu professor",
                    "opcoes": {
                            "inicio": "Tomar o elevador para o saguao de entrada",
                            "professor": "Falar com o professor"
            }
        },
            "professor": {
                    "titulo": "O MONSTRO DO PYTHON",
                    "descricao": "Voce foi pedir para o professor adiar o EP. "
                    "O professor revelou que é um monstro disfarçado "
                    "e devorou sua alma.",
                    "opcoes": {}
        },
            "biblioteca": {
                    "titulo": "CAVERNA DA TRANQUILIDADE",
                    "descricao": "Voce esta na biblioteca",
                    "opcoes": {
                            "inicio": "Voltar para o saguao de entrada",
                            "aquario": "Entrar em um aquário"}
        },
            "aquario": {
                "titulo":"Lugar da privacidade",
                "descricao":"voce entrou na sala de estudo em grupo",
                "opcoes":{"biblioteca": "volte para biblioteca",
                    "conversar com os amigos": "passe tempo de qualidade com eles"
                                    }
        },
            "conversar com os amigos":{
                "titulo" : "CILADA",
                "descricao" : "um de seus amigos se mostrou um monstro",
                "opcoes" : {
                    "lutar":"batalhar contra o mosntro",
                    "fugir":"deixe seus amigos serem devorados"
                }
        },
            "fugir":{
                "titulo": "COVARDE",
                "descricao" : "merece morrer",
                "opcoes" : {}

        },  
            "Refeitorio":{
                "titulo": "TERRA DA COMELANCIA",
                "descricao":"Ao olhar ao redor vc viu o Professor De DesSoft da turma A, e que o clima daquele local estava estranho",
                "opcoes":{
                    "professor da turma A": "conversar com o mesmo",
                    "voltar": "Sair do Refeitorio"
            }

=======
import json
with open('cenarios.json', 'r', encoding="utf8") as arquivo_c:
    cenario = json.load(arquivo_c)
>>>>>>> 0f1f6e0122f760ed2a95903d368478a40060c03c

with open('lista itens totais.json', 'r', encoding="utf8") as arquivo_i:
    lista = json.load(arquivo_i)

def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inventario():
    todos_itens = lista
    inventario_slots = []*2
    return todos_itens, inventario_slots

def main():
    init(autoreset=True)
    print()
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    time.sleep(2)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Voce está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    time.sleep(2)

    cenarios, nome_cenario_atual = carregar_cenarios()
    todos_itens,inventario_slots = inventario()

    game_over = False
    while not game_over:
        inventario_atual= inventario_slots
        cenario_atual = cenarios[nome_cenario_atual]
        print(Back.RED + cenario_atual["titulo"])
        print ("----------------")
        print(Fore.RED + cenario_atual["descricao"])
        print()

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print(Fore.CYAN + "Voce tem as seguintes opcoes:") 
            for opcao,val in opcoes.items():
                print(opcao,":",val)
            print(Fore.MAGENTA + "SEU INVENTARIO: {0}".format(inventario_atual))
            escolhas = cenarios[nome_cenario_atual]['opcoes']
            escolha = ""
            print(Fore.CYAN + "O que deseja fazer?")
            choice = input("")
            print()
            while not choice in escolhas:
                    print("Opcao inválida!!")
                    print("Digite como mostrado, por favor")
                    print()
                    print(Fore.CYAN + "Voce tem as seguintes opcoes:") 
                    for opcao,val in opcoes.items():
                        print(opcao,":",val)
                    print(Fore.CYAN + "O que deseja fazer?")
                    choice = input("")
                    print()
            if choice in escolhas:
                escolha = choice
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                    if escolha == "item":
                        item_achado = opcoes[escolha]
                        if not item_achado in inventario_atual:
                            inventario_atual.append(item_achado)
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


