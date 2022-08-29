from Funcoes_matrizes import Matriz

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
'''m = [[1,2],[-0.025,0]]

sigma = Matriz.Sigmoide(m)
print(sigma)
print()
print(Matriz.D_Sigmoide(m))
'''

#Teste transposta

'''m = [[1,2],[4,5],[7,8]]

print(Matriz.Transposta(m))
'''

#Teste Prod_Escalar

'''m = [[1,2], [3,4], [5,6]]

print(Matriz.Prod_Escalar(m, 2))'''

#Teste Prod_Hadamard

m = [[1,2],[3,4]]
n = [[5,6],[7,8]]

print(Matriz.Prod_Hadamard(m,n))
