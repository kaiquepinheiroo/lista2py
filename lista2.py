'''
Exercícios sobre os comandos de condição em python
'''
from datetime import date, datetime
# pip3 install deep-translator
from deep_translator import GoogleTranslator

HOJE = datetime.now()
tradutor = GoogleTranslator(source='en', target='pt')

def exemplo_if_else():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    else:
        if media >= 3:
            print('RECUPERAÇÃO')
        else:
            print('REPROVADO')

def exemplo_if_elif_else():
    media = float(input('Média: '))
    if media >= 6:
        print('APROVADO')
    elif media >= 3:
        print('RECUPERAÇÃO')
    else:
        print('REPROVADO')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    soma = num1 + num2
    if soma > 10:
        print(f'{soma} é maior que 10')
    else:
        print(f'{soma} não é maior que 10')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
# Leitura dos dois valores inteiros
def q2():
     num1=int(input("Digite um numero inteiro: "))
     num2=int(input("Digite outro numero inteiro: "))
     adc=(num1+num2)
     if(adc > 20):
         print(f'{adc} + 8 = {adc+8}')
     elif(adc <= 20):
         print(f'{adc} - 5 = {adc-5}')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
     num=int(input('Insira um número: '))
     if ((num%3)==0):
         print(f'{num} é múltiplo de 3.')
     else:
         print(f'{num} não é múltiplo de 3.')
#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
     num=int(input('Insira um número: '))
     if ((num%5)==0):
         print(f'{num} é divisível por 5.')
     else:
         print(f'{num} não é divisível por 5.')
 

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Digite um número inteiro: '))
    if num % 3 == 0 and num % 7 == 0:
        print(f'{num} é divisível por 3 e 7')
    else:
        print(f'{num} não é divisível por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
f q6():
     salario = round(float(input("Insira o salário bruto: R$")),2)
     prestaçao = round(float(input('Insira o valor da prestação: R$')),2)
     percent = (prestaçao*100)/salario
     if (percent > 30):
         print(f'Valor superior a 30% do salario bruto. O impréstimo não pode ser concedido.')
     else:
         print('Impréstimo autorizado.')    

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
7():
     num = int(input('Insira um número: '))
     if (20 <= num <= 50):
         print(f'{num} está entre 20 e 50.')
     else:
         print(f'{num} não está entre 20 e 50.')
 

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
     num = int(input('Insira um número: '))
     if (num < 20):
         print(f'{num} é menor que 20.')
     elif (num == 20):
         print(f'{num} é igual a 20.')
     elif (num > 20):
         print (f'{num} é maior que 20.')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    data_str = input('Data de Nascimento (dd/mm/aaaa): ')
    data_nascimento = datetime.strptime(data_str, '%d/%m/%Y')

    if (data_nascimento > HOJE):
        print('Data inválida! Você nem nasceu ainda.')
    else:
        print(f'Idade: {int((HOJE - data_nascimento).days/365)} anos.')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    a = int(input('Primeiro inteiro: '))
    b = int(input('Segundo inteiro: '))
    c = int(input('Terceiro inteiro: '))

    if (a < b < c): # equivale a if (a < b and b < c)
        print(f'{a} {b} {c}')
    if (a < c < b):
        print(f'{a} {c} {b}')
    if (b < a < c):
        print(f'{b} {a} {c}')
    if (b < c < a):
        print(f'{b} {c} {a}')
    if (c < a < b):
        print(f'{c} {a} {b}')
    if (c < b < a):
        print(f'{c} {b} {a}')
        
#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    a = int(input('Digite um número inteiro: '))
    maior = a
    b = int(input('Digite um número inteiro: '))
    if b > maior:
        maior = b
    c = int(input('Digite um número inteiro: '))
    if c > maior:
        maior = c
    print(f'O maior número é: {maior}')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos
def q12():
     idade = int(input("Qual é a idade? "))
     if (65 >= idade >= 18):
         print(f'É maior.')
     elif (idade < 18):
         print(f'É menor.')
     elif (idade > 65):
         print('É maior de 65.')
 

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
     nome = input('Nome: ')
     nota1 = float(input('Nota da prova 1:'))
     nota2 = float(input('Nota da prova 2:'))
     media = (nota1 + nota2)/2
     if (media >= 7):
         print (f'Aprovado com média {media}.')
     elif (7 > media >= 3):
         print (f'Média: {media}. \nProva final.')
     else:
         print (f'Média {media}. \nReprovado.')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
     salario = float(input('Insira o salário em R$: '))
     if (salario <= 600):
         print(f'Salário: {salario}. \nDesconto INSS: Isento.')
     elif (600 < salario <= 1200):
         print (f'Salário: {salario}. \nDesconto INSS: 20%.')
     elif (1200 < salario <= 2000):
         print (f'Salário: {salario}. \nDesconto INSS: 25%.')
     else:
         print (f'Salário: {salario}. \nDesconto INSS: 30%.')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    custo = float(input('Insira custo do produto: R$'))
    if (custo < 20):
        print(f'{custo} + 45% = {custo + (custo*0.45)}')
    else:
        print(f'{custo} + 30% = {custo + (custo*0.30)}')


#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input('Insira a idade: '))
    if ( 5 <= idade <= 7):
        print (f'Categoria: Infantil A.')
    elif ( 8 <= idade <= 10):
        print (f'Categoria: Infantil B.')
    elif ( 11 <= idade <= 13):
        print (f'Categoria: Juvenil A.')
    elif ( 14 <= idade <= 17):
        print (f'Categoria: Juvenil B.')
    elif ( 18 <= idade):
        print (f'Categoria: Sênior.')
    else: 
        print (f'Não compete.')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    mes = int(input('Número do Mês: '))
    if mes < 1 or mes > 12:
        print('Mês Inválido!')
    else:
        data = datetime.strptime(f'01/{mes}/25', '%d/%m/%y')
        mes_extenso = data.strftime('%B')
        print(tradutor.tanslate("Month: " + mes_extenso))


#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

questao = int(input('Questão a executar: '))
eval(f'q{questao}()')
