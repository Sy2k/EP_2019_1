# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionario
import time # a fim de usar time.sleep(z), onde z eh demonimado como um numero
import colorama
from colorama import Fore, Back, Style, init # "colorir" 
import json # a fim de importar os arquivos
import random

with open('cenarios.json', 'r', encoding="utf8") as arquivo_c:
    cenario = json.load(arquivo_c)

with open("char_caract.json", "r", encoding = "utf8") as arquivo_char:
    dados_char = json.load(arquivo_char)

with open('Lista_itens_descricao.json', 'r', encoding="utf8") as arquivo_ld:
    dados_i = json.load(arquivo_ld)

with open("HP_HitPoint_Defense(teste).json","r", encoding = "utf8") as arquivo:
    dados = json.load(arquivo)

with open("premios.json","r",encoding ="utf8") as arquivoL:
    data = json.load(arquivoL)


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

def aparecer_monstros(dados): #ira rodar de forma aleatoria a partir dos dados Json lidos, os monstros
    monstros = [] #lista fazia da lista de monstros
    for mons in dados:
        for var in mons.keys():
            if var == "nome":
                monstros.append(mons[var])
    rand = random.randint(1,len(monstros)-1)
    #print(monstros[key])
    return monstros[rand]

print (aparecer_monstros(dados))

def batalha(dados, dados_char):
    nome_monstro = aparecer_monstros(dados)
    villain = nome_monstro
    char = dados_char[0]
    while char['HP'] > 0  or villain['HP'] > 0:
        if char['HitPoint'] > villain['defensa']:
            villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
            if villain['HP'] <=0:
                resultado = "O jogador ganhou a batalha"

        elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
            villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
            resultado = "Você nem faz cocegas no monstro"

        elif villain['HitPoint'] > char['defesa']:
            char['HP'] = char['HP'] - (villain['HitPoint'] - char['defesa'])
            if char['HP'] <=0:
                #premio = False
                resultado = "O jogador perdeu a batalha"

        elif villain['HitPoint'] < char['defesa']:
            char['HP'] = char['HP']
            resultado = "O monstro não faz nem cocegas"
    return resultado

#list_new_data = []# tentando criar um bagy para ir guardando as alteracoes dos HitPoint
def premios_combate(data):#batalha mais premios
    game_over = False 
    while not game_over:
        n=0
        monstro = aparecer_monstros(dados)
        if monstro == "Professor DesSoft":
            villain = dados[0]

        elif monstro == "Raposa Selvagem":
            villain = dados[1]

        elif monstro == "Amigo Monstro":
            villain = dados[2]

        elif monstro == "Cozinheiro":
            villain= dados[3]

        elif monstro == "Veterano de ADM":
            villain = dados[4]

        elif monstro == "Monstro do corredor":
            villain = dados[5]

        char = dados_char[0]
        #list_new_data.append(data[1]["nome"], data[1]["HitPoint"], data[1]["HP"], data[1]["HP"])
        while char["HP"] > 0  or villain["HP"] > 0:
            premio = False
            if char["HitPoint"] > villain["defesa"]:
                villain["HP"] = villain["HP"] - (char["HitPoint"] - villain["defesa"])
                if villain["HP"] <=0:
                    resultado = "Você matou o monstro"
                    premio = True
                    if premio == True: # dando o premio apos matar o monstro (item dropado)
                        if villain == dados[1]["nome"]: # cada tipo de monstro apos ser derrotado dropa um tipo de item
                            print("O monstro dropou o seguinte item: {0}".format(data[6]["nome"]))
                            z = input("Deseja pegar o item dropado?(sim/nao) ")
                            while z!="sim" or z!="nao":#verificacao da escolha que o player pode fazer
                                print("Invalido") # caso não seja igual a sim ou nao deve se repetir entao repetira dentro desse while
                                z = input("Deseja pegar o item dropado? (sim/nao): ")
                            if z == "sim": 
                                #inv.append(data[6])
                                print("Item adicionado no inventario") #será adicionado no inventario e devera mudar os dados do HitPoint, defesa e HP
                            elif z == "nao":
                                print("Okay, continue sua jornada arriscada")
                            break

                        elif villain == dados[2]:
                            print("O monstro dropou o seguinte item: {0}".format(data[1]["nome"]))
                            z = input("Deseja pegar o item dropado?(sim/não): ")
                            while z!="sim" or z!="nao":
                                print("Invalido, por favor escreva como mostrado")
                                z = input("Deseja pegar o item dropado?(sim/nao): ")
                            if z == "sim":
                                inv.append(data[5])
                            elif z == "nao":
                                print("Okay, continue sua jornada arriscada")
                            break

                        elif villain == dados[3]:
                            print("O monstro dropou o seguinte item: {0}".format(data[4]["nome"]))
                            z = input("Deseja pegar o item dropado?(sim/nao): ")
                            while z!="sim" or z!="nao":
                                print("Invalido, por favor escreva como mostrado")
                                z = input("Deseja pegar o item dropado?(sim/nao): ")
                            if z == "sim":
                                inv.append(data[5])
                            elif z == "nao":
                                print("Okay, continue sua jornada arriscada")
                            break

                        elif villain == dados[4]:
                            print("O monstro dropou o seguinte item: {0}".format(data[2]["nome"]))
                            z = input("Deseja pegar o item dropado?(sim/não): ")
                            while z!="sim" or z!="nao":
                                print("Invalido, por favor escreva como mostrado")
                                z = input("Deseja pegar o item dropado?(sim/nao): ")
                            if z == "sim":
                                inv.append(data[5])
                            elif z == "nao":
                                print("Okay, continue sua jornada arriscada")
                            break

                        elif villain == dados[5]:
                            print("O monstro dropou o seguinte item: {0}".format(data[5]["nome"]))
                            z = input("Deseja pegar o item dropado?(sim/não): ")
                            while z!="sim" or z!="nao":
                                print("Invalido, por favor escreva como mostrado")
                                z = input("Deseja pegar o item dropado?(sim/nao): ")
                            if z == "sim":
                                inv.append(data[5])
                            elif z == "nao":
                                print("Okay, continue sua jornada arriscada")   
                            break

            elif char["HitPoint"] <= villain["defesa"]:  # Quando  o poder de ataque do jogador for
                #villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
                resultado = "Você nem faz cocegas no monstro"
                print("Você perdeu")
                game_over = True

            elif villain["HitPoint"] > char["defesa"]:
                char["HP"] = char["HP"] - (villain["HitPoint"] - char["defesa"])
                if char["HP"] <=0:
                    #premio = False
                    resultado = "O jogador perdeu a batalha"
                    game_over = True

            elif villain["HitPoint"] < char["defesa"]:
            #   char['HP'] = char['HP']
                resultado = "O monstro não faz nem cocegas"
        return resultado
print(premios_combate(data))


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


