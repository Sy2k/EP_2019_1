import json
with open('Lista_itens_descricao.json', 'r', encoding="utf8") as arq:
	dados_itens = json.load(arq)

def item_inicial(dados_itens):
	inventario_slots = [] 
	while True: 
		print("Opcao de item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[1]['nome'], dados_itens[1]['plus HitPoint'], dados_itens[1]['Plus na defesa']))
		print("Segunda opcao de item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[2]['nome'],dados_itens[2]['plus HitPoint'],dados_itens[2]['Plus na defesa']))
		print("Terceira opcao de item: {0}\nHitPoint: {1}\nDefense: {2}".format(dados_itens[3]['nome'],dados_itens[3]['plus HitPoint'],dados_itens[3]['Plus na defesa']))
		item_escolhido = input("Escolha entre os itens(digite o nome do item) {0}, {1} ou {2}: \n ".format(dados_itens[1]["nome"],dados_itens[2]["nome"],dados_itens[3]["nome"]))
		if item_escolhido == dados_itens[1]['nome']:
			col = dados_itens[1] 
			inventario_slots.append(dados[1])
			print("Você escolheu o item: {0}".format(dados_itens[1]['nome'])) 
			return "Item adicionado no inventario"
			break
		elif item_escolhido == dados_itens[2]['nome']:
			col = dados_itens[2]
			print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
			inventario_slots.append(dados_itens[2])
			return "Item adicionado no inventario"
			break
		elif item_escolhido == dados_itens[2]['nome']:
			col = dados_itens[2]
			print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
			inventario_slots.append(dados_itens[2])
			return "Item adicionado no inventario"
		else:
			print("INVALIDO ESCREVA COMO MOSTRADO")
			continue	
	return inventario_slots	
itens = dados_itens
print (item_inicial(itens))	

