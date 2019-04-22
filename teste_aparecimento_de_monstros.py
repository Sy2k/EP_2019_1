 #----------------------------------------Teste esta dando ERROOOOOO-----------------------------------------
import json
import random

with open("HP_HitPoint_Defense(teste).json","r", encoding = "utf8") as arquivo:
	dados = json.load(arquivo)

with open("char_caract.json", "r", encoding = "utf8") as arqz:
	dados_char = json.load(arqz)

with open("premios.json","r",encoding ="utf8") as arquivoL:
    data = json.load(arquivoL)

with open("Lista_itens_descricao.json", "r", encoding = "utf8") as inf:
	info = json.load(inf)

def demons_app(dados): #ira rodar de forma aleatoria a partir dos dados Json lidos, os monstros
	monstros = [] #lista fazia da lista de monstros
	for mons in dados:
		for var in mons.keys():
			if var == "nome":
				monstros.append(mons[var])
	rand = random.randint(1,len(monstros)-1)
	print(monstros[rand])
	return monstros[rand]

#list_new_data = []# tentando criar um bagy para ir guardando as alteracoes dos HitPoint
def premios(data): #batalha mais premios 
	dados2 = demons_app(dados)
	villain= dados2
	char = dados_char[1]
	#list_new_data.append(data[1]["nome"], data[1]["HitPoint"], data[1]["HP"], data[1]["HP"])
	while char['HP'] > 0  or villain['HP'] > 0:
		premio = False
		if char['HitPoint'] > villain['defensa']:
			villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
			if villain['HP'] <=0:
				premio = True
				while premio == True: # dando o premio apos matar o monstro (item dropado)
					if villain == dados[2]: # cada tipo de monstro apos ser derrotado dropa um tipo de item
						print("O monstro dropou o seguinte item: {0}".format(data[6]["nome"]))
						z = input("Deseja pegar o item dropado?(sim/não) ")
						while z!="sim" or z!="nao": #verificacao da escolha que o player pode fazer
							print("Invalido, por favor escreva como mostrado")# caso não seja igual a sim ou nao deve se repetir entao repetira dentro desse while
							z = input("Deseja pegar o item dropado?(sim/nao)")
						if z == "sim": 
							#inv.append(data[6])
							print("Item adicionado no inventario")#será adicionado no inventario e devera mudar os dados do HitPoint, defesa e HP
						elif z == "nao":
							print("Okay, continue sua jornada arriscada")

					elif villain == dados[3]:
						print("O monstro dropou o seguinte item: {0}".format(data[1]["nome"]))
						z = input("Deseja pegar o item dropado?(sim/não) ")
						while z!="sim" or z!="nao":
							print("Invalido, por favor escreva como mostrado")
							z = input("Deseja pegar o item dropado?(sim/nao)")
						if z == "sim":
							inv.append(data[6])
						elif z == "nao":
							print("Okay, continue sua jornada arriscada")

					elif villain == dados[4]:
						print("O monstro dropou o seguinte item: {0}".format(data[4]["nome"]))
						z = input("Deseja pegar o item dropado?(sim/não) ")
						while z!="sim" or z!="nao":
							print("Invalido, por favor escreva como mostrado")
							z = input("Deseja pegar o item dropado?(sim/nao)")
						if z == "sim":
							inv.append(data[6])
						elif z == "nao":
							print("Okay, continue sua jornada arriscada")

					elif villain == dados[5]:
						print("O monstro dropou o seguinte item: {0}".format(data[2]["nome"]))
						z = input("Deseja pegar o item dropado?(sim/não) ")
						while z!="sim" or z!="nao":
							print("Invalido, por favor escreva como mostrado")
							z = input("Deseja pegar o item dropado?(sim/nao)")
						if z == "sim":
							inv.append(data[6])
						elif z == "nao":
							print("Okay, continue sua jornada arriscada")

					elif villain == dados[6]:
						print("O monstro dropou o seguinte item: {0}".format(data[5]["nome"]))
						z = input("Deseja pegar o item dropado?(sim/não) ")
						while z!="sim" or z!="nao":
							print("Invalido, por favor escreva como mostrado")
							z = input("Deseja pegar o item dropado?(sim/nao)")
						if z == "sim":
							inv.append(data[6])
						elif z == "nao":
							print("Okay, continue sua jornada arriscada")	

		elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
		    #villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
			resultado = "Você nem faz cocegas no monstro"
			return resultado

		elif villain['HitPoint'] > char['defesa']:
			char['HP'] = char['HP'] - (villain['HitPoint'] - char['defesa'])
			if char['HP'] <=0:
				#premio = False
				resultado = "O jogador perdeu a batalha"
				return resultado

		elif villain['HitPoint'] < char['defesa']:
		#	char['HP'] = char['HP']
			resultado = "O monstro não faz nem cocegas"
		return resultado
