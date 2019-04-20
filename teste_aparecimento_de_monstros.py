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
"""
def batalha(dados):  
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))
print("Você escolheu o item: {0}".format(dados[6]['nome'])) 
"""