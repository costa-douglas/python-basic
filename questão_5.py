def busca_caracter(frase, busca):
    cont = 0
    for txt in frase:
        if txt == busca:
            cont += 1
    return cont
    


frase = input()
busca = input()

resultado = busca_caracter(frase, busca)

if resultado == 0:
    print('Caractere nao encontrado.')
else:
    print('O caractere buscado ocorre {} vezes na sequencia.'.format(resultado))
