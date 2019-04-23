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

with open("caracteristica_jogador.json", "r", encoding = "utf8") as arquivo_char:
    dados_char = json.load(arquivo_char)

with open('descricao_de_todos_itens.json', 'r', encoding="utf8") as arquivo_ld:
    dados_i = json.load(arquivo_ld)

with open("monstros_descricao.json","r", encoding = "utf8") as arquivo:
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

def premios_combate(dados, data):#batalha mais premios
    lista_pergunta = ["sim","nao"]
    monstro = aparecer_monstros(dados) #randomizar o monstro

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
    while char["HP"] > 0  or villain["HP"] > 0:
        global resultado
        global item_dado
        global HitPoint_item
        global Defesa_item 
        print("*Voce possui HP suficiente para batalhar!*")
        premio = False
        if char["HitPoint"] > villain["defesa"]:
            villain["HP"] = villain["HP"] - (char["HitPoint"] - villain["defesa"])
            if villain["HP"] <=0:
                resultado = "Contiue sua jornada! (não volte para esta sala)"
                premio = True
                if premio == True: # dando o premio apos matar o monstro (item dropado)
                    if villain == dados[1]["nome"]: # cada tipo de monstro apos ser derrotado dropa um tipo de item
                        print (Back.MAGENTA + "Você se deparou com : {0}!!!".format(dados[1]["nome"]))
                        print("HP do monstro:{0}  HitPoint:{1}  Defesa:{2}".format(dados[1]["HP"],dados[1]["HitPoint"],dados[1]["defesa"]))
                        time.sleep(2)
                        print("")
                        print(Fore.RED + "Você matou o monstro!")
                        print("O monstro dropou o seguinte item: {0}".format(data[1]["nome"]))
                        z = input("Deseja pegar o item dropado?(sim/nao):")
                        while not z in lista_pergunta: #verificacao da escolha que o player pode fazer
                            print("Invalido") # caso não seja igual a sim ou nao deve se repetir entao repetira dentro desse while
                            z = input("Deseja pegar o item dropado?(sim/nao):")
                        if z == "sim":
                            item_dado = data[1]['nome']
                            HitPoint_item = data[1]['plus HitPoint']
                            Defesa_item = data[1]['Plus na defesa']
                            print("Item adicionado no inventario") #será adicionado no inventario e devera mudar os dados do HitPoint, defesa e HP
                        elif z == "nao":
                            print("Okay, continue sua jornada arriscada")
                        break

                    elif villain == dados[2]:
                        print (Back.MAGENTA + "Você se deparou com : {0}!!!".format(dados[2]["nome"]))
                        print("HP do monstro:{0}  HitPoint:{1}  Defesa:{2}".format(dados[2]["HP"],dados[2]["HitPoint"],dados[2]["defesa"]))
                        time.sleep(2)
                        print("")
                        print(Fore.RED + "Você matou o monstro!")
                        print("O monstro dropou o seguinte item: {0}".format(data[2]["nome"]))
                        z = input("Deseja pegar o item dropado?(sim/nao):")
                        while not z in lista_pergunta:
                            print("Invalido, por favor escreva como mostrado")
                            z = input("Deseja pegar o item dropado?(sim/nao):")
                        if z == "sim":
                            item_dado = data[2]['nome']
                            HitPoint_item = data[2]['plus HitPoint']
                            Defesa_item = data[2]['Plus na defesa']
                        elif z == "nao":
                            print("Okay, continue sua jornada arriscada")
                        break

                    elif villain == dados[3]:
                        print (Back.MAGENTA + "Você se deparou com : {0}!!!".format(dados[3]["nome"]))
                        print("HP do monstro:{0}  HitPoint:{1}  Defesa:{2}".format(dados[3]["HP"],dados[3]["HitPoint"],dados[3]["defesa"]))
                        time.sleep(2)
                        print("")
                        print(Fore.RED + "Você matou o monstro!")
                        print("O monstro dropou o seguinte item: {0}".format(data[3]["nome"]))
                        z = input("Deseja pegar o item dropado?(sim/nao):")
                        while not z in lista_pergunta:
                            print("Invalido, por favor escreva como mostrado")
                            z = input("Deseja pegar o item dropado?(para sim/nao):")
                        if z == "sim":
                            item_dado = data[3]['nome']
                            HitPoint_item = data[3]['plus HitPoint']
                            Defesa_item = data[3]['Plus na defesa']
                        elif z == "nao":
                            print("Okay, continue sua jornada arriscada")
                        break

                    elif villain == dados[4]:
                        print (Back.MAGENTA + "Você se deparou com : {0}!!!".format(dados[4]["nome"]))
                        print("HP do monstro:{0}  HitPoint:{1}  Defesa:{2}".format(dados[4]["HP"],dados[4]["HitPoint"],dados[4]["defesa"]))
                        time.sleep(2)
                        print("")
                        print(Fore.RED + "Você matou o monstro!")
                        print("O monstro dropou o seguinte item: {0}".format(data[4]["nome"]))
                        z = input("Deseja pegar o item dropado?(sim/nao):")
                        while not z in lista_pergunta:
                            print("Invalido, por favor escreva como mostrado")
                            z = int(input("Deseja pegar o item dropado?(para sim digite 1/para nao digite 2):"))
                        if z == "sim":
                            item_dado = data[4]['nome']
                            HitPoint_item = data[4]['plus HitPoint']
                            Defesa_item = data[4]['Plus na defesa']
                        elif z == "nao":
                            print("Okay, continue sua jornada arriscada")
                        break

                    elif villain == dados[5]:
                        print (Back.MAGENTA + "Você se deparou com : {0}!!!".format(dados[5]["nome"]))
                        print("HP do monstro:{0}  HitPoint:{1}  Defesa:{2}".format(dados[5]["HP"],dados[5]["HitPoint"],dados[5]["defesa"]))
                        time.sleep(2)
                        print("")
                        print(Fore.RED + "Você matou o monstro!")
                        print("O monstro dropou o seguinte item: {0}".format(data[5]["nome"]))
                        z = input("Deseja pegar o item dropado?(sim/não): ")
                        while not z in lista_pergunta:
                            print("Invalido, por favor escreva como mostrado")
                            z = input("Deseja pegar o item dropado?(sim/não): ")
                        if z == "sim":
                            item_dado = data[5]['nome']
                            HitPoint_item = data[5]['plus HitPoint']
                            Defesa_item = data[5]['Plus na defesa']
                        elif z == "nao":
                            print("Okay, continue sua jornada arriscada")   
                        break

        elif char["HitPoint"] <= villain["defesa"]:  # Quando  o poder de ataque do jogador for
            #villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
            resultado = "Você nem faz cocegas no monstro"
            print("Você perdeu! sem HitPoint suficiente!!")
            game_over = True

        elif villain["HitPoint"] > char["defesa"]:
            char["HP"] = char["HP"] - (villain["HitPoint"] - char["defesa"])
            if char["HP"] <=0:
                resultado = "O jogador perdeu a batalha"
                game_over = True

        elif villain["HitPoint"] < char["defesa"]:
            resultado = "O monstro não faz nem cocegas"

        break 
    return resultado, item_dado, HitPoint_item, Defesa_item

def batalha_professor():
    professor_monstro = dados[0]
    caracteristica = dados_char[0]
    while caracteristica["HP"] > 0  or professor_monstro["HP"] > 0:

        if caracteristica["HitPoint"] > professor_monstro["defesa"]:
            professor_monstro["HP"] = professor_monstro["HP"] - (caracteristica["HitPoint"] - professor_monstro["defesa"])

            if professor_monstro["HP"] < 150:
                print("A vida do professor é menor que 150")
            elif professor_monstro["HP"] < 100:
                print("Você tirou metade de sua vida")
            elif professor_monstro["HP"] < 75:
                print("O HP do professor é menor que 75")
            elif professor_monstro["HP"] < 50:
                print("O HP do professor é menor que a 50")
            elif [professor]["HP"]<25:
                print("O HP do professor é menor a 25")
            elif professor_monstro["HP"] <=0:
                resultado = "Ganhou!! a EP foi adiada!"
            break
        elif caracteristica['HitPoint'] <= professor_monstro['defesa']:  # Quando  o poder de ataque do jogador for menor igual do que a defesa do oponente, a HP do Oponente nao se altera
            resultado = "Você nem faz cocegas no professor"
            
        elif professor_monstro['HitPoint'] > caracteristica['defesa']:
            caracteristica['HP'] = caracteristica['HP'] - (professor_monstro['HitPoint'] - caracteristica['defesa'])
            if caracteristica["HP"] < 75:
                print("Seu HP é menos que 75")
            elif caracteristica["HP"] < 50:
                print("Seu HP é esta menos que a metade")
            elif caracteristica["HP"] < 25:
                print("Seu HP caiu para menor que 25")
            elif caracteristica['HP'] <=0:
                resultado = "O jogador perdeu a batalha"
            break
    return resultado




def main():
    init(autoreset=True)
    print()
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    time.sleep(1) # tempo da pessoa ler todo o texto e aparecera o outro
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Voce está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    time.sleep(2)
    print(Back.RED + "aviso: O mesmo monstro pode aparecer varias vezes, caso drope um item que você já obtenha no inventario, não será adicionado novamente")
    time.sleep(2)
    print(Back.RED + "aviso: Para ficar mais divertido, procure não entrar novamente em locais que já houveram batalhas!")
    time.sleep(2)
    print(Back.RED + "As batalhas irão depender da sua vida e seus atributos (aprimorados ao longo do jogo)")
    print()
    time.sleep(2)

    cenarios, nome_cenario_atual = carregar_cenarios()
    inventario_slots = inventario_funcao()
    dados_itens = item_inicial()
    inventario = inventario_slots #o inventario sera igual a lista criada na funcao do inventario
    caracteristicas = dados_char[0]

    print("Você poderá começar o jogo com um item!")
    print(Fore.BLUE + "item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[0]['nome'], dados_itens[0]['plus HitPoint'], dados_itens[0]['Plus na defesa']))
    print(Fore.GREEN + "item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[1]['nome'],dados_itens[1]['plus HitPoint'],dados_itens[1]['Plus na defesa']))
    print(Fore.YELLOW + "item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[2]['nome'],dados_itens[2]['plus HitPoint'],dados_itens[2]['Plus na defesa']))
    item_escolhido = input("Escolha entre os itens(digite o nome do item) {0}, {1} ou {2}:\n".format(dados_itens[0]["nome"],dados_itens[1]["nome"],dados_itens[2]["nome"]))
    if item_escolhido == dados_itens[0]['nome']:
        inventario.append(dados_itens[0]['nome']) #adiciona o item no inventario
        caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[0]['plus HitPoint'] #muda o hitpoint de acordo com o objeto
        caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[0]['Plus na defesa'] #muda a defesa de acordo com o objeto
        print("Você escolheu o item: {0}".format(dados_itens[0]['nome'])) 
        print ("Item adicionado no inventario")
    elif item_escolhido == dados_itens[1]['nome']:
        inventario.append(dados_itens[1]['nome'])
        caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[1]['plus HitPoint']
        caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[1]['Plus na defesa']
        print("Você escolheu o item: {0}".format(dados_itens[1]['nome'])) 
        print ("Item adicionado no inventario")
    elif item_escolhido == dados_itens[2]['nome']:
        inventario.append(dados_itens[2]['nome'])
        caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[2]['plus HitPoint']
        caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[2]['Plus na defesa']
        print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
        print ("Item adicionado no inventario")
        print()

    game_over = False
    while not game_over: #enquanto a pessoa nao pereder
        cenario_atual = cenarios[nome_cenario_atual]
        opcoes = cenario_atual['opcoes']
        print()
        print("----------------")
        print(Back.RED + cenario_atual["titulo"])
        print("----------------")
        print(Fore.RED + cenario_atual["descricao"])
        print()
        if len(opcoes) == 0:
            batalha_professor()
        elif len(opcoes) == 1:
            resultado_obtido, item_obtido, HitPoint_add, Defesa_add = premios_combate(dados,data)
            print(resultado_obtido)
            if not item_obtido in inventario:
                inventario.append(item_obtido)
                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + HitPoint_add
                caracteristicas["defesa"] = caracteristicas["defesa"] + Defesa_add
            time.sleep(2)
            print(Fore.MAGENTA + "HP:{0} HitPoint:{1} Defesa total:{2}".format(caracteristicas["HP"],caracteristicas["HitPoint"],caracteristicas["defesa"]))
            print(Fore.MAGENTA + "SEU INVENTARIO: {0}".format(inventario))
            print()
            print(Fore.CYAN + "Voce tem as seguintes opções:") 
            for opcao,val in opcoes.items():
                print(opcao,":",val)
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
                                 
        else:
            print(Fore.MAGENTA + "HP:{0} HitPoint:{1} Defesa total:{2}".format(caracteristicas["HP"],caracteristicas["HitPoint"],caracteristicas["defesa"]))
            print(Fore.MAGENTA + "SEU INVENTARIO: {0}".format(inventario))
            print()
            print(Fore.CYAN + "Voce tem as seguintes opções:") 
            for opcao,val in opcoes.items():
                print(opcao,":",val)
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
                            if item_achado == "livro de literatura":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[3]['plus HitPoint'] #muda o hitpoint de acordo com o objeto
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[3]['Plus na defesa'] #muda a defesa de acordo com o objeto
                            elif item_achado == "colher":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[8]['plus HitPoint']
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[8]['Plus na defesa'] 
                            elif item_achado == "bolo ana maria":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[11]['plus HitPoint']
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[11]['Plus na defesa'] 
                            elif item_achado == "frigideira":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[7]['plus HitPoint']
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[7]['Plus na defesa'] 
                            elif item_achado == "chaves":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[5]['plus HitPoint']
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[5]['Plus na defesa'] 
                            elif item_achado == "balde de tinta":
                                inventario.append(item_achado)
                                caracteristicas["HitPoint"] = caracteristicas["HitPoint"] + dados_itens[6]['plus HitPoint']
                                caracteristicas["defesa"] = caracteristicas["defesa"] + dados_itens[6]['Plus na defesa'] 

    print("Voce morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


