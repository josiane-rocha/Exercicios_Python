#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Faça um programa que peça um valor monetário e diminua-o em 15%. Seu
programa deve imprimir a mensagem “O novo valor é [valor]”.


valor_monetario = input("Qual o valor do produto? ")
valor_monetario = float(valor_monetario)

desconto = valor_monetario / 100 * 15

total = valor_monetario - desconto
    
print("Voce ganhou um desconto de 15%, seu produto agora é " , total)





2. Faça um programa que leia a validade das informações:
   a. Idade: entre 0 e 150;
   b. Salário: maior que 0;
   c. Sexo: M, F ou Outro;


O programa deve imprimir uma mensagem de erro para cada informação
inválida.

contador = 0

idade = input("Qual a sua idade? ")
while contador >= 150:
    contador = contador + 1
    if contador >= 150:
        print(contador, "Sua idade é: ")
    else: 
        print(contador, "Erro, digite a idade correta entre 0 a 150")

        
salario = input("Qual o seu salário? ")
while contador >= 1:
    contador = contador + 1
    if contador >= 1:
        print(contador, "Seu salário é: ")
    else: 
        print(contador, "Erro, digite o valor correto, esse salário nao é aceito")
       
    
entrada = " "

entrada = input("Qual o seu sexo Feminino, Masculino ou Outro? ")
    
if entrada == 'Feminino':
    print("Agradeço pelas informações")
elif entrada == 'Masculino':
    print("Agradeço pelas informações")
elif entrada == 'Outro':
    print("Agradeço pelas informações")
else: 
    print("Erro, digite o sexo corretamente dentro das opçoes")





3. Vamos fazer um programa para verificar quem é o assassino de um crime.
Para descobrir o assassino, a polícia faz um pequeno questionário com 5
perguntas onde a resposta só pode ser sim ou não:

  get_ipython().set_next_input('  a. Mora perto da vítima');get_ipython().run_line_magic('pinfo', 'vítima')
  get_ipython().set_next_input('  b. Já trabalhou com a vítima');get_ipython().run_line_magic('pinfo', 'vítima')
  get_ipython().set_next_input('  c. Telefonou para a vítima');get_ipython().run_line_magic('pinfo', 'vítima')
  get_ipython().set_next_input('  d. Esteve no local do crime');get_ipython().run_line_magic('pinfo', 'crime')
  get_ipython().set_next_input('  e. Devia para a vítima');get_ipython().run_line_magic('pinfo', 'vítima')
  
Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
2 pontos são apenas suspeitos, necessitando outras investigações. Valores
iguais ou abaixo de 1 são liberados.
 
 
 print('Tabuada do número 9')

print('-' * 15)
print('{} x {:2} = {:2}'.format(tabuada, 1, tabuada*1))
print('{} x {:2} = {:2}'.format(tabuada, 2, tabuada*2))
print('{} x {:2} = {:2}'.format(tabuada, 3, tabuada*3))
print('{} x {:2} = {:2}'.format(tabuada, 4, tabuada*4))
print('{} x {:2} = {:2}'.format(tabuada, 5, tabuada*5))
print('{} x {:2} = {:2}'.format(tabuada, 6, tabuada*6))
print('{} x {:2} = {:2}'.format(tabuada, 7, tabuada*7))
print('{} x {:2} = {:2}'.format(tabuada, 8, tabuada*8))
print('{} x {:2} = {:2}'.format(tabuada, 9, tabuada*9))
print('{} x {:2} = {:2}'.format(tabuada, 10, tabuada*10))
print('-' * 15)





4. Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.


print('=' *50)
print('PROCURANDO O ASSASSINO')
print('=' *50)
print('Se a resposta for afirmativa o suspeito ganhará 1 ponto. Obs responda somente com [S/N]')
pergunta1 = input('Mora perto da vítima?').upper()
pergunta2 = input('Já trabalhou com a vítima?').upper()
pergunta3 = input('Telefonou para a vítima?'). upper()
pergunta4 = input('Esteve no lugar do crime?'). upper()
pergunta5 = input('Devia para a vítima?'). upper()
c = 0
if pergunta1 == 'S':
    c = c + 1
if pergunta2 == 'S':
    c = c + 1
if pergunta3 == 'S':
    c = c + 1
if pergunta4 == 'S':
    c = c + 1
if pergunta5 == 'S':
    c = c + 1
if c == 5:
    print('Caso resolvido! Encontramos o assassino')
elif c == 4 or c == 3:
    print('Você é um dos cúmplices, nos entregue o assassino agora!')
elif  c == 2:
    print('Aguarde, vamos analisar um pouco mais')
    
elif c ==1 or c== 0:
    print('Você está liberado!')

