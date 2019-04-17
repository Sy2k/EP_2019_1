# EP 2019-1: Escape Insper
#Stephanie : stephaniel@al.insper.edu.br
#Ellen : ellenbs@al.insper.edu.br
#Ellen - dicionarios 
def carregar_cenarios():
    cenarios = {
            "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
            "andar professor": {
                    "titulo": "Andar do desespero",
                    "descricao": "Voce chegou ao andar da sala do seu professor",
                    "opcoes": {
                            "inicio": "Tomar o elevador para o saguao de entrada",
                            "professor": "Falar com o professor"
            }
        },
            "professor": {
                    "titulo": "O monstro do Python",
                    "descricao": "Voce foi pedir para o professor adiar o EP. "
                    "O professor revelou que é um monstro disfarçado "
                    "e devorou sua alma.",
                    "opcoes": {}
        },
            "biblioteca": {
                    "titulo": "Caverna da tranquilidade",
                    "descricao": "Voce esta na biblioteca",
                    "opcoes": {
                            "inicio": "Voltar para o saguao de entrada",
                            "aquario": {
                                    "titulo":"Lugar da privacidade",
                                    "descricao":"voce entrou na sala de estudo em grupo",
                                    "opcoes":{
                                            "Estudar": "Você perdeu o horário e não encontrou o professor",
                                            "Conversar com os amigos":{
                                                    "Um de seus amigos é um monstro": {
                                                            "Lutar": "salvou seus amigos do monstro",
                                                            "Fugir": "deixou seus amigos para serem devorados"
                                                    }
                                            }
                                    }
                            }
                    }
        },
            "Computadores": {
                    "titulo":"Terra da Internet",
                    "descricao":"voce pode navegar na internet",
                    "opcoes":{
                            "Facebook":"",
                            "BlackBoard": ""  }
            },
            "Refeitorio":{
                    "titulo": "Terra da comilança",
                    "descricao":"voce pode explorar ou ir embora",
                    "opcoes":{
                            "comer" : "a comida esta envenenada",
                            "voltar":""
                            }
                    }
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual["titulo"])
        print ("----------------")
        print(cenario_atual["descricao"])
        print()
        print("para se teletransportar, voce deve saber o nome correto de cada sala" )

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""
        
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
        escolha_sala = input("deseja se teletransportar para algum lugar?" )
        if escolha_sala == "nao":
                print ("voce continua na mesma sala")
        elif escolha_sala in cenarios:
            if escolha_sala != cenario_atual:
                cenario_atual = escolha_sala 
        else:
            print("sala invalida")

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()


