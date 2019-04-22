import json
with open('Lista_itens_descricao.json', 'r', encoding="utf8") as arq:
	dados_itens = json.load(arq)

def item_inicial(dados_itens): 
	while True: 
		print("Opcao de item:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[1]['nome'],dados_itens[1]['HitPoint'],dados_itens[1]['HP']))
		print("Segunda opcao de item:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[2]['nome'],dados_itens[2],['HitPoint'],dados_itens[2]['HP']))
		print("Terceira opcao de item:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens,[3]['nome'],dados_itens[3]['HitPoint'],dados_itens[3]['HP']))
		wahl = input("Escolha entre os itens(digite o nome do item) {0}, {1} ou {2}: ".format(dados_itens,[1]["nome"],dados[2]["nome"],dados[3]["nome"]))
		if wahl == dados_itens[1]['nome']:
			col = dados_itens[1] 
			inventario_slots.append(dados[1])
			print("Você escolheu o item: {0}".format(dados_itens[1]['nome'])) 
			return "Item adicionado no inventario"
			break
		elif wahl == dados_itens[2]['nome']:
			col = dados_itens[2]
			print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
			inventario_slots.append(dados_itens[2])
			return "Item adicionado no inventario"
			break
		elif wahl == dados_itens[2]['nome']:
			col = dados_itens[2]
			print("Você escolheu o item: {0}".format(dados_itens[2]['nome'])) 
			inventario_slots.append(dados_itens[2])
			return "Item adicionado no inventario"
		else:
			print("INVALIDO ESCREVA COMO MOSTRADO")
			continue			

