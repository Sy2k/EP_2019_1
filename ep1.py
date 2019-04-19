# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionario
import time
import colorama
from colorama import Fore, Back, Style, init
import json
with open('cenarios.json', 'r', encoding="utf8") as arquivo_c:
    cenario = json.load(arquivo_c)

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
        print("----------------")
        print(Back.RED + cenario_atual["titulo"])
        print("----------------")
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


