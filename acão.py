import ep1
import time
import colorama
from colorama import Fore, Back, Style, init
def escolher_caminho():
 	caminho = " "
 	while caminho != "biblioteca" or caminho !="aquario" or caminho!= "refeitorio" or caminho!= "banheiro" or caminho!="andar do professor" or caminho!="Computadores": #Validação 
 		caminho = input(Fore.BLUE + "Qual caminho você irá escolher? ")
 	return caminho 

def acao (escolher_caminho):
	cenario = escolher_caminho
	game_over = False
	while not game_over:
		cenario_atual = cenarios[nome_cenario_atual]
		print(cenario_atual["titulo"])
		print ("----------------")
		print(cenario_atual["descricao"])
		print()
		print("para se teletransportar, voce deve saber o nome correto de cada sala" )
		print()
		if cenario == "biblioteca" or "Biblioteca":
			print("Ao entrar na biblioteca, você se depara com uma bibliotecaria")
			time.sleep(2)
			print("Voce olha mais a sua volta e vê computadores, um bastao de beisebol")
			print("Um estilingue e um bolo, além de ser possível ir para o aquario")
			time.sleep(2)
			a = int(input("O que deseja fazer(escolher um caminho(digite 1); pegar algum item(digite 2); falar com a bibliotecaria (digite 3) "))
			while a!= 1 or a!=2 or a!=3: #validação
				a = int(input("O que deseja fazer(escolher um caminho(digite 1); pegar algum item(digite 2); falar com a bibliotecaria (digite 3) "))
			if a == 1:
				cenario = " "
	 			while cenario != "biblioteca" or cenario!="aquario" or cenario!= "refeitorio" or cenario!= "banheiro" or cenario!="orar do professor" or cenario!="Computadores": #Validação 
	 				cenario = input(Fore.BLUE + "Qual caminho você irá escolher(Sair da biblioteca(digite1); Ir para os aquarios(Digite2); Mexer nos computadores(Digite3)? ")
	 				return cenario 
			elif a == 2:
				#como validar????
				print("Qual item deseja pegar? ")
				pick = int(input("Sendo possivel pegar o bastao de beisebol(Digite 10),Estilingue(Digite 11) ou o Bolo(Digite 12) "))
				print("O bastao de beisebol aumentara seu poder em 5, o Estilingue em 5, o bolo aumenta sua possibilidade de fuga")
				if pick == 10:
					return "Seu poder foi aumentado mais 5"
				elif pick == 11:
					return "Seu poder foi aumentado mais 5"
				elif pick == 12:
					return "Sua chance de fugir aumenta mais 10"
				else:
					while pick != 10 or pick!=11 or pick!=12:
						print("Qual item deseja pegar? ")
						pick = int(input("Sendo possivel pegar o bastao de beisebol(Digite 10),Estilingue(Digite 11) ou o Bolo(Digite 12) "))
						print("O bastao de beisebol aumentara seu poder em 5, o Estilingue em 5, o bolo aumenta sua possibilidade de fuga")
			elif a==3:
				print("Bibliotecaria:Olá, quanto tempo desde a última vez, precisa de ajuda com algo? ")
				time.sleep(2)
				print("Soube que para os alunos do primeiro semestre está meio corrido para entregar o projeto de programação")
				print(Fore.RED+"//Opções de ação: Sim, está muito corrido, você sabe onde esta o professor de Dessoft?(Digite1);não ta tranquilo e não conversar mais(Digite2)")
				time.sleep(2)
				print("//DICA: A bibliotecaria pode desbloquear seu inventario")
				time.sleep(2)
				fala_char_1 = int(input("O que deseja fazer? "))
				if fala_char_1 == 1:
					print("Bibliotecaria: Apenas falarei se você trouxer a caixa vermelha ")
				return fala_char_1

		elif cenario == 'aquario' or 'Aquario':
			desejo = ("Deseja entrar no aquario? (Sim ou Nao) ")
			while desejo != 'Sim'or sim or desejo!="Nao" or "nao":
				print("Invalido, digite novamente corretamente")
				desejo = ("Deseja entrar no aquario? (Sim ou Nao) ")
			if desejo == "Sim":
				print("Por favor digite como se apresenta a opcao")
				time.sleep(2)
				opcao_jogada_aquario =input("Opcoes de jogo: Estudar, Conversar com os amigos, Sair: ")
				if opcao_jogada_aquario == "Estudar" or "estudar":
					print("Voce comecou a estudar design de software, para fazer sua ep")
					time.sleep(5)
					print("Voce se distraiu programando e perdeu o horario, nao encontrando o professor")
					print("Pena, Voce perdeu se vire para conseguir programar toda a EP")
					game_over= True 
				elif opcao_jogada_aquario == "Conversar com os amigos" or "conversar com os amigos":
					#Descrever a consequencia

				elif opcao_jogada_aquario == "Sair":
					#como voltar no if da bibliioteca
					cenario == 'biblioteca' or 'Biblioteca'
			elif desejo == "Nao":
				print("Por favor digite como se apresenta a opcao")
				opcao_jog_fora_aquario = input("Opcao de jogo: Conversar com a bibliotecaria, pegar algum item, mexer nos computadores, sair da biblioteca")
			





