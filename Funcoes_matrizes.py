
class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = []

    #Funcão responsável por dar início aos primeiros valores dos pesos e dos bias
    def randomize(self):
        import random
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                linha.append(random.random())
            self.data.append(linha)
    
    #Função responsável por somar duas matrizes -> Elas devem ter mesma dimensão
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

    #Função responsável por subtratir duas matrizes
    def subtracao(Matriz_A, Matriz_B):
        sub = []
        for i in range(len(Matriz_A)):
            sub_linha = []
            for j in range(len(Matriz_A[0])):
                sub_linha.append(Matriz_A[i][j]-Matriz_B[i][j])
            sub.append(sub_linha)
        return sub

    #Função que aplica a sigmoide aos valores de uma matriz
    def Sigmoide(Matriz_A):
        import math
        sigmoide = []
        for i in range(len(Matriz_A)):
            sigmoide_linha = []
            for j in range(len(Matriz_A[0])):
                sigmoide_linha.append(1/(1+(math.e)**(-Matriz_A[i][j])))
            sigmoide.append(sigmoide_linha)
        return sigmoide

    #Função que aplica a derivada da função sigmoide aos valores de uma matriz que já passou pela Sigmoide
    def D_Sigmoide(Matriz_A):
        import math
        d_sigmoide = []
        for i in range(len(Matriz_A)):
            d_sigmoide_linha = []
            for j in range(len(Matriz_A[0])):
                d_sigmoide_linha.append(Matriz_A[i][j]*(1-Matriz_A[i][j]))
            d_sigmoide.append(d_sigmoide_linha)
        return d_sigmoide     

    #Função que fornece a transposta de uma matriz
    def Transposta(Matriz_A):
        transposta = []
        for i in range(len(Matriz_A[0])):
            linha = []
            for j in range(len(Matriz_A)):
                linha.append(Matriz_A[j][i])
            transposta.append(linha)
        return transposta

    #Função que realiza o produto de uma matriz por um escalar
    def Prod_Escalar(Matriz_A, e):
        p_escalar = []
        for i in range(len(Matriz_A)):
            p_linha = []
            for j in range(len(Matriz_A[0])):
                p_linha.append(Matriz_A[i][j]*e)
            p_escalar.append(p_linha)
        return p_escalar

    #Função que realiza o produto Hadamard entre duas matrizes -> Devem ter mesmas dimensões
    def Prod_Hadamard(Matriz_A, Matriz_B):
        p_hadamard = []
        for i in range(len(Matriz_A)):
            p_hadamard_linha = []
            for j in range(len(Matriz_A[0])):
                p_hadamard_linha.append(Matriz_A[i][j]*Matriz_B[i][j])
            p_hadamard.append(p_hadamard_linha)
        return p_hadamard



                




                
       

        

    