 #----------------------------------------Teste-----------------------------------------
import json
import random
with open("HP_HitPoint_Defense(teste).json","r", encoding="utf8") as arquivo:
	dados = json.load(arquivo)
def aparecer_monstros(dados):
	lista_Mons = []
	for e in dados:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	print(lista_Mons[key])
	return lista_Mons[key]

print (aparecer_monstros(dados))

def batalha(dados):  
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
print("Você escolheu o item: {0}".format(dados[6]['nome'])) 

def batalha(dados):
	dados2 = aparecer_monstros(dados)
	villain= dados2
	char = dados[7]
	while char['HP'] > 0  or villain['HP'] > 0:
		if char['HitPoint'] > villain['defensa']:
			villain['HP'] = villain['HP'] - (char['HitPoint'] - villain['defesa'])
			if villain['HP'] <=0:
				return "O jogador ganhou a batalha"

		elif char['HitPoint'] <= villain['defesa']:  # Quando  o poder de ataque do jogador for
		    villain['HP'] = villain['HP']   # menor do que a defesa do oponente, a HPoponente nao se altera
			

		elif villain['HitPoint'] > char['defesa']:
			char['HP'] = char['HP'] - (villain['HitPoint'] - char['defesa'])
			if char['HP'] <=0:
				return "O jogador perdeu a batalha"

		elif villain['HitPoint'] < char['defesa']:
			char['HP'] = char['HP']

