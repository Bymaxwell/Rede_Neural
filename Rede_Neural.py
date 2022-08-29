from Funcoes_matrizes import Matriz

class Rede_Neural:
    def __init__(self, i_nodes, h_nodes, o_nodes):
        self.i_nodes = i_nodes
        self.h_nodes = h_nodes
        self.o_nodes = o_nodes

        self.bias_ih = Matriz(self.h_nodes, 1)
        self.bias_ih.randomize()
        self.bias_ho = Matriz(self.o_nodes, 1)
        self.bias_ho.randomize()
 
        self.pesos_ih = Matriz(self.h_nodes, self.i_nodes)
        self.pesos_ih.randomize()
        self.pesos_ho = Matriz(self.o_nodes, self.h_nodes) 
        self.pesos_ho.randomize()

        self.learning_rate = 0.1

    def Rede(self, entrada):
        #FeedForward
        hidden = Matriz.produto(self.pesos_ih.data, entrada)
        hidden = Matriz.soma(hidden, self.bias_ih.data)
        hidden = Matriz.Sigmoide(hidden)

        output = Matriz.produto(self.pesos_ho.data, hidden)
        output = Matriz.soma(output, self.bias_ho.data)
        output = Matriz.Sigmoide(output)

        return output

   






    