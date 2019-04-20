with open('lista_itens_totais.json', 'r', encoding="utf8") as arq:
    dados_itens = json.load(arq)

def escolher_item_inicial(dados_itens): 
	while True: 
		print("Primeira Opcao:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[1]['nome']dados_itens[1]['HitPoint']dados_itens[1]['HP']))
		print("Segunda Opcao:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[2]['nome']dados_itens[2]['HitPoint']dados_itens[2]['HP']))
		print("Terceira Opcao:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[3]['nome']dados_itens[3]['HitPoint']dados_itens[3]['HP']))
		escolha_inicial = input("Escolha entre os itens {0}, {1} ou {2}:".format(dados_itens[1]["nome"],dados[2]["nome"],dados[3]["nome"]))
		if escolha_inicial == dados_itens[1]['nome']:
			colection = dados_itens[1] 
			inventario_slots.append(dados[1])
			print("Você escolheu o item: {0}".format(dados[1]['nome'])) 
			return "Item adicionado no inventario"
			break
		elif escolha_inicial == dados[2]['nome']:
			colection = dados_itens[2]
			print("Você escolheu o item: {0}".format(dados[2]['nome'])) 
			inventario_slots.append(dados[2])
			return "Item adicionado no inventario"
			break
		elif escolha == dados[2]['nome']:
			colection = dados[2]
			print("Você escolheu o item: {0}".format(dados[2]['nome'])) 
			list_player.append(dados[2])
			return "Item adicionado no inventario"
		else:
			print(Style.DIM + "Erro! Escolha novamente (Por favor copie exatamente como mostrado!)")
			continue			

