#Apresentação
print('Olá, Bem vindo ao programa!\n')
#Entrada de nome (interação)
nome = input('Qual o seu nome?: ')
#Fim da entrada de nome
print('É um prazer ter você aqui, {}!\n'.format(nome))
#Continuação da apresentação
print('O que eu faço aqui é mostrar:\n')
print('*o dobro do valor')
print('*o triplo do valor')
print('*a raiz quadrada do valor\n')
#Fim da apresentação
#Entrada de dados e interação com o usuário
print('Então vamos iniciar! Você está pronto, {}?\n'.format(nome))
p = input('Se você está pronto, digite "sim" para continuar: ')
print('Vamos lá:\n')
n1 = int(input('digite um número: '))
s = n1 * 2
t = n1 * 3 
r = n1 ** (1/2)
#Fim da entrada de dados
#Saída de dados
print('O dobro de {} é: {}'.format(n1 , s))
print('O triplo de {} é: {}'.format(n1 , t))
print('A raiz quadrada de {} é: {:.2f}\n'.format(n1 , r))
#Fim da saída de dados
#Nome de quem criou o código abaixo
print('########## CODED BY LUCAS SILVA ##########')
