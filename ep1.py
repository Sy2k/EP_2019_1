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

with open("char_caract.json", "r", encoding = "utf8") as arquivo_char:
    dados_char = json.load(arquivo_char)

with open('Lista_itens_descricao.json', 'r', encoding="utf8") as arquivo_ld:
    dados_i = json.load(arquivo_ld)

def item_inicial():
    lista = dados_i
    return lista

def carregar_cenarios(): 
    cenarios = cenario
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def inventario_funcao(): #criando um inventario inicialmente de dois espacos
    inventario_slots = []*2
    return inventario_slots

def aparecer_monstros(dados): #ira rodar de forma aleatoria a partir dos dados Json lidos, os monstros
    monstros = [] #lista fazia da lista de monstros
    for mons in dados:
        for var in mons.keys():
            if var == "nome":
                monstros.append(mons[var])
    rand = random.randint(1,len(monstros)-1)
    return monstros[rand]

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
    inventario_slots = inventario_funcao()
    dados_itens = item_inicial()
    inventario = inventario_slots #o inventario sera igual a lista criada na funcao do inventariO
    print(Back.CYAN + "Você poderá começar o jogo com um item!")
    print("item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[0]['nome'], dados_itens[0]['plus HitPoint'], dados_itens[0]['Plus na defesa']))
    print("item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[1]['nome'],dados_itens[1]['plus HitPoint'],dados_itens[1]['Plus na defesa']))
    print("item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[2]['nome'],dados_itens[2]['plus HitPoint'],dados_itens[2]['Plus na defesa']))
    item_escolhido = input("Escolha entre os itens(digite o nome do item) {0}, {1} ou {2}:\n".format(dados_itens[0]["nome"],dados_itens[1]["nome"],dados_itens[2]["nome"]))
    if item_escolhido == dados_itens[0]['nome']:
        inventario.append(dados_itens[0]['nome'])
        print("Você escolheu o item: {0}".format(dados_itens[0]['nome'])) 
        print ("Item adicionado no inventario")
    elif item_escolhido == dados_itens[1]['nome']:
        inventario.append(dados_itens[1])
        print("Você escolheu o item: {0}".format(dados_itens[1]['nome'])) 
        print ("Item adicionado no inventario")
    elif item_escolhido == dados_itens[2]['nome']:
        inventario.append(dados_itens[2]['nome'])
        print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
        print ("Item adicionado no inventario")
        print()

    game_over = False
    while not game_over: #enquanto a pessoa nao pereder
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
            print(Fore.MAGENTA + "SEU INVENTARIO: {0}".format(inventario))
            escolha = ""
            print(Fore.CYAN + "O que deseja fazer?")
            escolha_digitada = input("")
            print()

            while not escolha_digitada in opcoes :
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
                        if not item_achado in inventario:
                            inventario.append(item_achado)

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


