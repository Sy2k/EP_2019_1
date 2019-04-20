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
	key = random.randint(0,len(lista_Mons)-1)
	#print(lista_Mons[key])
	return lista_Mons[key]

print (aparecer_monstros(dados))

def batalha():
	dados2 = aparecer_monstros(dados)
	villain= dados2
	char = dados_char[1]
	while char['HP'] > 0  or villain['HP'] > 0:
		if char['HitPoint'] > villain['defensa']:
			villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
			if villain['HP'] <=0:
				resultado = "O jogador ganhou a batalha"
				#premio = True 
				return resultado
		elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
		    villain['HP'] = villain['HP']   # menor igual do que a defesa do oponente, a HP do Oponente nao se altera
			resultado = "Você nem faz cocegas no monstro"
			print(resultado) 

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
	