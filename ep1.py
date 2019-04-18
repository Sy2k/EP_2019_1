# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionario
import time
import colorama
from colorama import Fore, Back, Style, init
import json
with open('cenarios.json', 'r', encoding="utf8") as arquivo:
    cenario = json.load(arquivo)

def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inventario(inv):
    z = input("Qual item deseja pegar? ")
    while z in opcao_item:
        inventario_slots = []
        for i in inv:
            x = i.split()  # Separa.
            h="".join(z)  # Junta tudo de novo com um espaco.
        if not h in inv:
            inv.append(h)  # Adiciona elementos que nao estao presentes na lista
            return inv
            #TEM o inventario tem dois espacoes no comeco
            # ai dps da mochila aumentar x numeros

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

    game_over = False
    while not game_over:
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
                else:
                    print("Sua indecisão foi sua ruína!")
                    game_over = True

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


