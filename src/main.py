import networkx as nx
import matplotlib.pyplot as plt
#import json

# CRIANDO E IMPRIMINDO UM GRAFO #

#inicializando estruturas básicas do grafo
class Adj:
    def __init__(self, data, peso):
        self.vertex = data
        self.peso = peso
        self.proximo = None
        self.explored = False

#vértices
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.G = nx.Graph() #Usando networkx (Verificar se é Graph ou grafo)
        self.Time = 0
        self.grafo = [None]*self.V

    def add_edge(self, vizinho1, vizinho2, peso):
        no = Adj(vizinho2, peso)
        no.proximo = self.grafo[vizinho1]
        self.grafo[vizinho1] = no

        no = Adj(vizinho1, peso)
        no.proximo = self.grafo[vizinho2]
        self.grafo[vizinho2] = no

        self.G.add_node(vizinho1)
        self.G.add_node(vizinho2)
        self.G.add_edge(vizinho1, vizinho2, peso=peso)
    
    #imprimindo grafo
    def imprime_grafo(self):
        for i in range(self.V):
            print("lista do vertice {}\n".format(i), end="")
            temp = self.grafo[i]
            while temp:
                print(" -- {} W: {} || ".format(temp.vertices, temp.peso), end="")
                temp = temp.proximo
            print(" \n")


