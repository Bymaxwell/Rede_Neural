
class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = []

    #Funcão responsável por dar início aos primeiros valores dos pesos e dos bias.
    def randomize(self):
        import random
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                linha.append(random.random())
            self.data.append(linha)
    
    #Função responsável por somar duas matrizes -> Elas devem ter mesma dimensão.
    def soma(Matriz_A, Matriz_B):
        soma = []
        for i in range(len(Matriz_A)):
            soma_linha = []
            for j in range(len(Matriz_A[0])):
                soma_linha.append(Matriz_A[i][j]+Matriz_B[i][j])
            soma.append(soma_linha)
        return soma

    #Funcao responsavel por multiplicar duas matrizes 
    def produto(Matriz_A, Matriz_B):
        produto = []
        for i in range(len(Matriz_A)):
            produto_linha = []
            for j in range(len(Matriz_B[0])):
                soma_produto = 0
                for k in range(len(Matriz_A[0])):
                    soma_produto += Matriz_A[i][k]*Matriz_B[k][j]
                produto_linha.append(soma_produto)
            produto.append(produto_linha)
        return produto

    def subtracao(Matriz_A, Matriz_B):
        sub = []
        for i in range(len(Matriz_A)):
            sub_linha = []
            for j in range(len(Matriz_A[0])):
                sub_linha.append(Matriz_A[i][j]-Matriz_B[i][j])
            sub.append(sub_linha)
        return sub

    def Sigmoide(Matriz_A):
        import math
        sigmoide = []
        for i in range(len(Matriz_A)):
            sigmoide_linha = []
            for j in range(len(Matriz_A[0])):
                sigmoide_linha.append(1/(1+(math.e)**(-Matriz_A[i][j])))
            sigmoide.append(sigmoide_linha)
        return sigmoide





                
       

        

    