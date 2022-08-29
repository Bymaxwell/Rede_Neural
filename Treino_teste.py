from Funcoes_matrizes import Matriz
from Rede_Neural import Rede_Neural

#Teste randomzise
'''Teste = Matriz(3,2)
Teste.randomize()
print(Teste.data)'''

#Teste soma
'''m = [[1,2],[3,4]]
n = [[5,6],[7,8]]

Funcoes = Matriz(1,1)
print(Funcoes.soma(m,n))'''

#Teste produto
'''m = [[1,2],[3,4]]
n = [[5],[6]]

print(Matriz.produto(m, n))
'''


#Teste subtracao
'''m = [[1,2],[7,8]]
n = [[5,4],[3,6]]

print(Matriz.subtracao(m, n))
'''

#Teste Sigmoide

'''m = [[1,0],[0,4]]

print(Matriz.Sigmoide(m))'''

#Teste D_Sigmoide
'''m = [[1,20],[-0.025,0]]

sigma = Matriz.Sigmoide(m)
print(sigma)
print()
print(Matriz.D_Sigmoide(sigma))'''


#Teste transposta

'''m = [[1,2],[4,5],[7,8]]

print(Matriz.Transposta(m))
'''

#Teste Prod_Escalar

'''m = [[1,2], [3,4], [5,6]]

print(Matriz.Prod_Escalar(m, 2))'''

#Teste Prod_Hadamard

'''m = [[1,2],[3,4]]
n = [[5,6],[7,8]]

print(Matriz.Prod_Hadamard(m,n))'''

#Teste Rede Neural

'''Rede = Rede_Neural(3, 2, 2)

for i in range(20):
    entrada = [[1],[2],[3]]
    print(Rede.Rede(entrada))
print()
print()
print('NOVA REDE')
for i in range(20):
    entrada = [[1],[2],[3]]
    print(Rede.Rede(entrada))'''

#Teste Back Propagation

Network = Rede_Neural(2, 4, 2)

entradas = [[[1],[1]], [[1],[0]], [[0],[1]], [[0],[0]]]
saidas = [[[1],[1]], [[0], [1]], [[0], [1]], [[0],[0]]]

import random
while True:
    x = input()
    if x == "Pare":
        break
    if x == "Treino":
        print('Treinando')
        j = 0
        while True:  
            i = random.randint(0,3)
            Network.BackPropagation(entradas[i], saidas[i])
            j += 1
            print(j)
            if j >= 10000:
                break

        
                
    if x == "Teste":
       
        print('Teste iniciado')
        print(Network.bias_ho.data)
        print(Network.bias_ih.data)
        print()
        print(Network.Rede([[1],[1]]))
        print()
        print(Network.Rede([[0],[1]]))
        print()
        print(Network.Rede([[1],[0]]))
        print()
        print(Network.Rede([[0],[0]]))
                
