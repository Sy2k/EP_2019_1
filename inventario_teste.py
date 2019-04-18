#lista_itens = [{'Caixas':},{"Chaves": },{"Balde de tinta": },{"Estilingue": },{"Frigideira": },{"Colher": } ,{"Faca": },{"Água fervente": },{"Pimenta": },{"Casca de Banana":"poder fugir"}]
def inventario(inv):
    z = input("Qual item deseja pegar")
    while z in opcao_item:
        inventario_slots = []
        for i in inv:
            x = i.split()  # Separa.
            h="".join(z)  # Junta tudo de novo com um espaco.
        if not h in inv:
            inv.append(h)  # Adiciona elementos que nao estao presentes na lista
            return inv
            #TEM o inventario tem dois espacoes no comeco
            # ai dps da mochila aumentar x numeros

"""
def fazer_inventario():
	if len(inventario) == 0:
    return 'Inventario: Não tem nada'
    conta_item = {}
    for item in inventario:
        if item in conta_item.keis():
            conta_item[item] += 1
        else:
            conta_item[item] = 1

    print('Inventario:')
    for item in set (inventario):
        if conta_item[item] > 1:
            print('{0}, {1}'.format(item, conta_item[item]))
        else:
            print('  ' + item)
faz_inv = fazer_inventario
return faz_inv
"""