
import time

#import colorama
"""
lista_itens = [{'Caixas':},{"Chaves": },{"Balde de tinta": },{"Estilingue": },{"Frigideira": },{"Colher": } ,{"Faca": },{"Água fervente": },{"Pimenta": },{"Casca de Banana":"poder fugir"}]
def inventario_tentativa_2(inventario__2):
    inventario_2 = []
    for i in inventario__2:
        x = i.split()  # Separa.
        h="".join(z)  # Junta tudo de novo com um espaco.
    if not h in inventario_2:
        inventario__2.append(h)  # Adiciona elementos que nao estao presentes na lista
        return inventario_2
"""
"""
def fazer_inventario():
	if len(inventario) == 0:
        print('Inventario: Não tem nada')
        return
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
#faz_inv = fazer_inventario
return faz_inv
"""


def escolher_caminho():
 	caminho = " "
 	while caminho != "biblioteca" or caminho !="aquario" or caminho!= "refeitorio" or caminho!= "banheiro" or caminho!="andar do professor" or caminho!="Computadores": #Validação 
 		caminho = input("Qual caminho você irá escolher? ")
 	return caminho 

def acao (escolher_caminho):
	caminho = escolher_caminho
	if caminho == "biblioteca" or "Biblioteca":
		print("Ao entrar na biblioteca, você se depara com uma bibliotecaria")
		time.sleep(2)
		print("Você olha mais a sua volta e vê computadores, um bastão de beisebol")
		print("Um estilingue e um bolo, além de ser possível ir para o aquario")
		time.sleep(2)
		a = int(input("O que deseja fazer(escolher um caminho(digite 1); pegar algum item(digite 2); falar com a bibliotecaria (digite 3) "))
		while a!= 1 or a!=2 or a!=3: #validação
			a = int(input("O que deseja fazer(escolher um caminho(digite 1); pegar algum item(digite 2); falar com a bibliotecaria (digite 3) "))
		if a == 1:
			caminho = " "
 			while caminho != "biblioteca" or caminho !="aquario" or caminho!= "refeitorio" or caminho!= "banheiro" or caminho!="orar do professor" or caminho!="Computadores": #Validação 
 				caminho = input("Qual caminho você irá escolher(Sair da biblioteca(digite1); Ir para os aquarios(Digite2); Mexer nos computadores(Digite3)? ")
 				return caminho 
		elif a == 2:
			#verificar se conversou com a bibliotecaria

		elif a==3:
			print("Bibliotecaria:Olá, quanto tempo desde a última vez, precisa de ajuda com algo? ")
			time.sleep(2)
			print("Soube que para os alunos do primeiro semestre está meio corrido para entregar o projeto de programação")
			print("//Opções de ação: Sim, está muito corrido, você sabe onde esta o professor de Dessoft?(Digite1);não ta tranquilo e não conversar mais(Digite2)")
			time.sleep(2)
			print("//DICA: A bibliotecaria pode desbloquear seu inventario")
			time.sleep(2)
			fala_aluno_1 = int(input("O que deseja fazer? "))
			if fala_aluno_1 == 1:
				print("Bibliotecaria: Apenas falarei se você trouxer a caixa vermelha ")
			return fala_aluno_1
	elif caminho == 'aquario' or 'Aquario':







