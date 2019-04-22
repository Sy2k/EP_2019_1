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
			#	char['HP'] = char['HP']
				resultado = "O monstro não faz nem cocegas"
		return resultado
print(premios_combate(data))
