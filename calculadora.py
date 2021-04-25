print("\t FRRE CALCULATOR!!!\n ")

continuar = input(" \t Por favor digite seu nome: \n")

print(" t\ BEM VINDO", continuar)

print(" \t Para continuar, escolha uma das seguintes opções: \n")

while True:
    start = input("Para contas básicas: \n'1'\n"
    "Para circulos: \n'2'\n"
    "Para equeção de segundo grau: \n'3'\n"
    "Para potências e raízes: \n'4'\n"
    "Para conversor de unidade: \n'5'\n"
    "Para geometria: \n'6'\n"
    "Para função: \n'7'\n"
    "Para velocidade média: \n'8'\n"
    "Para sair do programa: \n'9'\n")

    if start == 'n':
        print("\t OBRIGADO POR USAR MEU PROGRAMA!!!\n")
        exit()

    if start == '1':
        print("\t CONTAS BÁSICAS: \n")

        import math

        primeiro = input("\t Digite o primeiro número:\n ")
        segundo  = input("\t Digite o segundo  número:\n" )
        operacao = input("\t Digite a operação: \n")

        resultado = None
        if operacao == '+':
            resultado = float(primeiro) + float(segundo)
        elif operacao == '-':
            resultado = float(primeiro) - float(segundo)
        elif operacao == '*':
            resultado = float(primeiro) * float(segundo)
        elif operacao == '/':
            resultado = float(primeiro) / float(segundo)
        else:
            print("\t IMPOSSÍVEL REALIZAR A OPERAÇÃO!!!\n")

        if resultado:
            print("\t RESULTADO: {0}".format(resultado))

            break

        continue

    if start == '2':
        print("\n CIRCULOS: \n")

        print("\t PARA CONTINUAR, ESCOLHA UMA DAS SEGUINTES OPÇÕES: \n")

        a = input("ÁREA DO CIRCULO -----> \n'1'\n"
        "COMPRIMENTO DO CIRCULO -----> \n'2'\n"
        "SAIR -----> \n'n'\n")

    if a == 'n':
        print("\t ORIGADO POR USAR MEU PRIGRAMA!!!\n")

        exit()

    if a == '1':
        print("\t COMPRIMENTO DO CIRCULO: \n")

        import math

        pi = 3,14

        r = input("DIGITE O VALOR DO RAIO: ")

        resposta = (float(r) * float(r)) * pi

        print("\n A ÁREA DO CIRCULO É: ",resposta,"\n")

        break

    if a == '2':
        print("\t COMPRIMENTO DO CIRCULO: \n")

        import math

        pi = 3.14

        r = input("DIGITE O VALOR DO RAIO: ")

        resposta = (float(r) * 2) * pi

        print("\t O COMPRIMENTO DO CIRCULO É:",resposta,"\n")

        break

    else:
        print("\t CARACTERE INVÁLIDO!!!\n")

        continue