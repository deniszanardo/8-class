# import random
# import time
# from itertools import chain


# # # loop finito
# # # z = random.randint(1,10)
# # l = [1,2,3]

# # for i in l:
# #     l.append(i)
# #     print(l)

# # lista  = [1,2,3,4,5,6]
# # for x in lista:
# #     print(x)

# # for  z in list(range(1,11)):
# #     print(z)

# # x  =  [x for x in range(1,12) if x % 2 == 0]
# # print(x)


# #  ---------------------------------------
# # enquanto 

# # x  =  10 > 2

# # while x:
# #     print('teste')


# # c  = 0
# # while c <= 10:
# #     print(c)
# #     c  =  c  + 1
# #     time.sleep(2)

# # print('isso esta fora')

# # percorriveis  = iterar 

# # lista
# # tuplas 
# # 'texto'
# # conjuntos = {1,2,3}
# # dic  =  {'a':10, 'b':150}

# # # dict compressions  dicionarios 
# # dicionario =  {x: x ** 2 for x in range(10)}
# # print(dicionario)

# # # set compressions conjuntos 
# # range(10)
# # range(1,10)
# # range(1,10,2)

# # se =  {x for x in range(11)}

# # print(se)


# # lista = [x for x in range(1,7)]
# # print(lista)

# x = []
# for i in range(1,7):
#     x.append(i)
# print(x)    

# # crie um form e digite o nome de 3  pessoas

# # ln = []

# # for i in range(10):
# #     nome = input('nome: ')
# #     ln.append(nome)
# # print(ln)    



# # pergunta =  input('Digite sim ou não')
# # while pergunta  == 'sim':
# #     print('comprar')
# #     pergunta = input('Deseja continuar? >>>')
# # else:
# #     print('obrigada volte sempre')    


# # break 


# # lista  =  [1,2,3]
# # x = int(input('>>>'))
# # while x in lista:
# #     print(x)
# #     if x  % 2 == 0:
# #         break
# #     x = int(input('>>>'))

# # lista  =  [1,2,3]
# # x = int(input('>>>'))
# # while x in lista:
# #     print(x)
# #     if x  % 2 == 0:
# #         continue
# #     x = int(input('>>>'))


# # encadeamento

# # l1 = [1,2,3]
# # l2 = [1,2,3]
# # l3 = [1,2,3]

# # for x in chain(l1,l2,l3):
# #     print(x)

# # l = [x for x in chain(l1,l2,l3)]
# # print(l)

# l1 = [1,2,3]
# l2 = [1,2,3]
# l3 = [1,2,3]

# for i, valor in enumerate(l1, start=1):
#     print(f'{i}, {valor}')

#-----------------------------------exercicio aula anterior 




# v = int(input('>>'))


# if v < 10 or v > 1000 or v % 5 != 0:
#     print('invalida')
# else:
#     p50 = v // 50
#     v  =  v % 50


#     p20 = v // 20
#     v  =  v % 20


#     p10 = v // 10
#     v  =  v % 10


#     p5 = v // 5
#     v  =  v % 5    


#     print('notas de 50', p50)
#     print('notas de 20', p20)
#     print('notas de 10', p10)
#     print('notas de 5', p5)


# # upper torna a lista toda em mairuscula 
# z = list(map(str.upper,["Julia, fernanda"]))
# print(z)
# # # loop finito
# # # z = random.randint(1,10)

# l = [1,2,3]
# for i in l:
#     l.append(i)
#     print(l)

# lista  = [1,2,3,4,5,6]
# for x in lista:
#     print(x)

# # for  z in list(range(1,11)):
# #     print(z)

# # x  =  [x for x in range(1,12) if x % 2 == 0]
# # print(x)

# ___________________________________________________________________________________________________________________________________________________________________________________
## **2  - Exercícios**

# ### **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. 
# Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# tab = int(input("Digite n: "))
# for count in range(10):
#     c = count * tab
#     print(tab,"x", count, "=", c)



# contador = 0
# while contador < 15:
#     print(contador)
#     contador +=1




# x = []
# for i in range(1,7):
#     x.append(i)
# print(x)


# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer 
# uma contagem regressiva até 0, exibindo cada número. 
# Após o término, exiba `"Fogo!"`.

# contador = 10
# while contador >0:
#     print(contador)
#     contador -=1
# print("fogo")


# ---

# ### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. 
# Calcule e exiba a média das notas válidas (0 a 10). 
# Ignore entradas inválidas e use `continue` quando necessário.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). 
# Dê ao usuário 3 tentativas usando `while`. 
# Se acertar, exiba `"Acesso liberado"` e encerre. 
# Se errar todas, exiba `"Conta bloqueada"`.


# contador = 3
# while contador > 0:
#     print(contador)
#     contador -=1
#     print("acesso negado")






# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. 
# Use `while` para extrair os dígitos um a um.

# ---
# # ___________________________________________________________________________________________________________________________________________________________________________________

# ### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.

# ---

# ### **9 Simulador de Lançamento de Dados**

# Simule 100 lançamentos de um dado de 6 faces.
# Conte quantas vezes cada face foi sorteada e exiba o resultado. 
# Use `for` e `random.randint(1,6)`. (Importe `random`.)

# for and `random.randint(1,6)`. (Importe `random`.)
