from geradorTestes import ColecaoDados

gerador = ColecaoDados()
lista_opcoes = []
dado = ''

def opcoes():
    print("----------------------------------------------")
    print("Bem vindo ao Gerador de testes")
    print("Escolha uma(s) opções, ou digite 'parar' para sair")
    print("1-Nome")
    print("2-Telefone")
    print("3-Email")    
    opcao = input("Digite uma ou mais opçoes, ou parar!").replace(',','')
    return opcao

while True:
        opcao = opcoes()
        if opcao != "parar":
            for item in opcao:
                if item == '1':
                    dado = gerador.gerar_nomes()
                    #lista_opcoes.append(nome)
                elif item == '2':
                    dado = gerador.gerar_telefones()
                    #lista_opcoes.append(telefone)    
                elif item == '3':
                    dado = gerador.gerar_email() 
                    #lista_opcoes.append(email)       

                lista_opcoes.append(dado)
        else:
            print("Saindo do programa")
            break

