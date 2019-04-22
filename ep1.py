# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionario
import time # a fim de usar time.sleep(z), onde z eh demonimado como um numero
import colorama
from colorama import Fore, Back, Style, init # "colorir" 
import json # a fim de importar os arquivos

with open('cenarios.json', 'r', encoding="utf8") as arquivo_c:
    cenario = json.load(arquivo_c)

with open('lista_itens_totais.json', 'r', encoding="utf8") as arquivo_i:
    lista = json.load(arquivo_i)

with open("char_caract.json", "r", encoding = "utf8") as arqz:
    dados_char = json.load(arqz)

def carregar_cenarios(): 
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inventario(): #criando um inventario inicialmente de dois espacos
    todos_itens = lista
    inventario_slots = []*2
    return todos_itens, inventario_slots

def aparecer_monstros(dados): #ira rodar de forma aleatoria a partir dos dados Json lidos, os monstros
    monstros = [] #lista fazia da lista de monstros
    for mons in dados:
        for var in mons.keys():
            if var == "nome":
                monstros.append(mons[var])
    rand = random.randint(1,len(monstros)-1)
    return monstros[rand]

print (aparecer_monstros(dados))


def main():
    init(autoreset=True)
    print()
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    time.sleep(2) # tempo da pessoa ler todo o texto e aparecera o outro
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Voce está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    time.sleep(2)

    cenarios, nome_cenario_atual = carregar_cenarios()
    todos_itens,inventario_slots = inventario()

    game_over = False
    while not game_over: #enquanto a pessoa nao pereder
        inventario_atual= inventario_slots #o inventario sera igual a lista criada na funcao do inventario
        cenario_atual = cenarios[nome_cenario_atual]
        print("----------------")
        print(Back.RED + cenario_atual["titulo"])
        print("----------------")
        print(Fore.RED + cenario_atual["descricao"])
        print()
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Não há mais opções!")
            game_over = True
        else:
            print(Fore.CYAN + "Voce tem as seguintes opções:") 
            for opcao,val in opcoes.items():
                print(opcao,":",val)
            print(Fore.MAGENTA + "SEU INVENTARIO: {0}".format(inventario_atual))
            escolha = ""
            print(Fore.CYAN + "O que deseja fazer?")
            escolha_digitada = input("")
            print()

            while not escolha_digitada in opcoes and lista_t:
                    print(Back.CYAN + "Opcao inválida!!")
                    print("Digite como mostrado, por favor") # enquanto escrever errado ira mostrar essa mensagem
                    print()
                    print(Fore.CYAN + "Voce tem as seguintes opcoes:")# ira mostrar novalmente as opcoes
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

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


