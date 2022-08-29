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

    #Função responsável por realizar as operações da Rede Neural e entregar as saídas -> Entrada é uma matriz de uma coluna
    def Rede(self, entrada):
        #FeedForward
        hidden = Matriz.produto(self.pesos_ih.data, entrada)
        hidden = Matriz.soma(hidden, self.bias_ih.data)
        hidden = Matriz.Sigmoide(hidden)

        output = Matriz.produto(self.pesos_ho.data, hidden)
        output = Matriz.soma(output, self.bias_ho.data)
        output = Matriz.Sigmoide(output)

        return output

    def BackPropagation(self, entrada, resultado_esperado):
        #FeedForward
        hidden = Matriz.produto(self.pesos_ih.data, entrada)
        hidden = Matriz.soma(hidden, self.bias_ih.data)
        hidden = Matriz.Sigmoide(hidden)

        output = Matriz.produto(self.pesos_ho.data, hidden)
        output = Matriz.soma(output, self.bias_ho.data)
        output = Matriz.Sigmoide(output)

        #BackPropagation

        #Output --> Hidden
        hidden_T = Matriz.Transposta(hidden)
        error_output = Matriz.subtracao(resultado_esperado, output)
        derivate_output = Matriz.D_Sigmoide(output)
        pesos_ho_deltas = Matriz.Prod_Hadamard(error_output, derivate_output)
        pesos_ho_deltas = Matriz.Prod_Escalar(pesos_ho_deltas, self.learning_rate)

        self.bias_ho.data = Matriz.soma(self.bias_ho.data, pesos_ho_deltas)

        pesos_ho_deltas = Matriz.produto(pesos_ho_deltas, hidden_T)

        self.pesos_ho.data = Matriz.soma(self.pesos_ho.data, pesos_ho_deltas)

        #Hidden --> Input
        input_T = Matriz.Transposta(entrada)
        pesos_ho_T = Matriz.Transposta(self.pesos_ho.data)
        error_hidden = Matriz.produto(pesos_ho_T, error_output)
        derivate_hidden = Matriz.D_Sigmoide(hidden)
        pesos_hi_deltas = Matriz.Prod_Hadamard(error_hidden, derivate_hidden)
        pesos_ih_deltas = Matriz.Prod_Escalar(pesos_hi_deltas, self.learning_rate)

        self.bias_ih.data = Matriz.soma(self.bias_ih.data, pesos_ih_deltas)

        pesos_ih_deltas = Matriz.produto(pesos_ih_deltas, input_T)

        self.pesos_ih.data = Matriz.soma(self.pesos_ih.data, pesos_ih_deltas)



   






    