from Funcoes_matrizes import Matriz

class Rede_Neural:
    def __init__(self, i_nodes, h_nodes, o_nodes):
        self.i_nodes = i_nodes
        self.h_nodes = h_nodes
        self.o_nodes = o_nodes

        self.bias_ih = Matriz(self.h_nodes, 1)
        self.bias_ho = Matriz(self.o_nodes, 1)
 
        self.pesos_ih = Matriz(self.h_nodes, self.i_nodes)
        self.pesos_ho = Matriz(self.o_nodes, self.h_nodes) 

        self.learning_rate = 0.1

   






    