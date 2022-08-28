
class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.data = []

    #Funccão responsável por dar início aos primeiros valores dos pesos e dos bias.
    def randomize(self):
        import random
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                linha.append(random.random())
            self.data.append(linha)
                
       

        

    