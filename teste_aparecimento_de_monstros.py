def aparecer_monstros(info):
	lista_Mons = []
	for e in info:
		for x in e.keys():
			if x == "nome":
				lista_Mons.append(e[x])
	key = random.randint(0,len(lista_Mons)-1)
	print(lista_Mons[key])
	return lista_Mons[key]
print (Aparecimento_de_Mons(info))
def batalha_2(dados):  
 #----------------------------------------Teste-----------------------------------------
	n=0
	list_0 = []
	list_0.append(Aparecimento_de_Mons(dados))