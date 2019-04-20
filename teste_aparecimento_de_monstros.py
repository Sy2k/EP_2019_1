 #----------------------------------------Teste-----------------------------------------
import json
import random
with open("HP_HitPoint_Defense(teste).json","r", encoding="utf8") as arquivo:
	dados = json.load(arquivo)
with open("char_caract.json", "r", encoding="utf8") as arqz:
	dados_char = json.load(arqz)
with open("premios.json","r",encoding="utf8") as arquivoL:
    data = json.load(arquivoL)

def aparecer_monstros(dados):
	lista_Mons = []
	for e in dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(1,len(lista_Mons)-1)
	#print(lista_Mons[key])
	return lista_Mons[key]

print (aparecer_monstros(dados))

def batalha(dados, dados_char):
	dados2 = aparecer_monstros(dados)
	villain= dados2
	char = dados_char[1]
	while char['HP'] > 0  or villain['HP'] > 0:
		if char['HitPoint'] > villain['defensa']:
			villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
			if villain['HP'] <=0:
				return "O jogador ganhou a batalha"

		elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
		    villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
			resultado = "Você nem faz cocegas no monstro"
			return resultado 

		elif villain['HitPoint'] > char['defesa']:
			char['HP'] = char['HP'] - (villain['HitPoint'] - char['defesa'])
			if char['HP'] <=0:
				#premio = False
				resultado = "O jogador perdeu a batalha"
				return resultado

		elif villain['HitPoint'] < char['defesa']:
			char['HP'] = char['HP']
			resultado = "O monstro não faz nem cocegas"
		return resultado

def premios(data):
	dados2 = aparecer_monstros(dados)
	villain= dados2
	char = dados_char[1]
	premio = False
	while char['HP'] > 0  or villain['HP'] > 0:
		if char['HitPoint'] > villain['defensa']:
			villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
			if villain['HP'] <=0:
				premio = True
				while premio == True:
					if villain == dados[2]:
						print("O monstro dropou o seguinte item: {0}".format(data[6]["nome"]))
					elif villain == dados[3]:
						print("O monstro dropou o seguinte item: {0}".format(data[1]["nome"]))
					elif villain == dados[4]:
						print("O monstro dropou o seguinte item: {0}".format(data[4]["nome"]))
					elif villain == dados[5]:
						print("O monstro dropou o seguinte item: {0}".format(data[2]["nome"]))
					elif villain == dados[6]:
						print("O monstro dropou o seguinte item: {0}".format(data[5]["nome"]))
						
		elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
		    villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
			resultado = "Você nem faz cocegas no monstro"
			return resultado 

		elif villain['HitPoint'] > char['defesa']:
			char['HP'] = char['HP'] - (villain['HitPoint'] - char['defesa'])
			if char['HP'] <=0:
				#premio = False
				resultado = "O jogador perdeu a batalha"
				return resultado

		elif villain['HitPoint'] < char['defesa']:
			char['HP'] = char['HP']
			resultado = "O monstro não faz nem cocegas"
		return resultado
 
