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
with open('lista_itens_totais.json', 'r', encoding="utf8") as arquivo_i:
    lista = json.load(arquivo_i)
with open('teletransporte.json', 'r', encoding='utf8') as arquivo_t:
    lista_tele = json.load(arquivo_t)

def carregar_cenarios():
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inventario():
    todos_itens = lista
    inventario_slots = []*2
    return todos_itens, inventario_slots
#    z = input("Qual item deseja pegar")
#    while z in opcao_item:
#        for i in inv:
#            x = i.split()  # Separa.
#            h="".join(z)  # Junta tudo de novo com um espaco.
#       if not h in inv:
#            inv.append(h)  # Adiciona elementos que nao estao presentes na lista
#    return todos_itens, inventario_slots, inv
def teletransporte():
    lista_t = lista_tele
    nome_cenario_teletransporte = "teletransporte"
    return lista_t,nome_cenario_teletransporte

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
    lista_t, nome_cenario_teletransporte = teletransporte()

    game_over = False
    while not game_over:
        inventario_atual= inventario_slots
        cenario_atual = cenarios[nome_cenario_atual]
        cenario_teletransporte = lista_t[nome_cenario_teletransporte]

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
            escolha_inicial = ""
            print(Fore.CYAN + "O que deseja fazer?")
            escolha_digitada = input("")
            print()

            while not escolha_digitada in opcoes and lista_t:
                    print(Back.CYAN + "Opcao inválida!!")
                    print("Digite como mostrado, por favor")
                    print()
                    print(Fore.CYAN + "Voce tem as seguintes opcoes:") 
                    for opcao,val in opcoes.items():
                        print(opcao,":",val)
                    print(Fore.CYAN + "O que deseja fazer?")
                    escolha_digitada = input("")
                    print()

            if escolha_digitada in opcoes:
                escolha = escolha_digitada
                if escolha in opcoes:
                    nome_cenario_atual = escolha
                    if escolha == "item":
                        item_achado = opcoes[escolha]
                        if not item_achado in inventario_atual:
                            inventario_atual.append(item_achado)
            elif escolha_digitada in lista_t:
                if escolha == "teletransporte":
                    teletransporte_escolha = input("para onde deseja se teletransportar? ")
                    cenario_teletransporte = teletransporte_escolha
                    nome_cenario_atual = cenario_teletransporte
            

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


