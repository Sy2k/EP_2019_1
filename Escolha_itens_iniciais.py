with open('lista_itens_totais.json', 'r', encoding="utf8") as arq:
    dados_itens = json.load(arq)

def escolher_item_inicial(dados_itens):
	while True: 
		print("Primeira Opcao:\n{0}\nHitPoint:\n{1}\nHp:{2}\nDefense:{3}".format(dados_itens[]['nome'][]['HitPoint'][]['HP']))
		print("Segunda Opcao:\n{0}\nHitPoint:\n{0}\nDefense:{3}".format(dados[]['nome']))