#Implementa as funções para a biblioteca de Grafos nao direcionados ponderados

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices

        #conteudo das linhas em branco, vertices = numero de linhas
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
 
    

    def adiciona_aresta(self, u, v, p):
        # estou pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = p  #trocar = por += ser for grafo múltiplo

        self.grafo[v-1][u-1] = p 
    #so pra ficar mais facil de testar
    def mostra_matriz(self, arqOut):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])
            arqOut.write(f'\n{self.grafo[i]}')


    #----------------------------------------------FUNCOES DO TRABALHO-----------------------------------------#
    
    #--------ORDEM DO GRAFO----------------#
    def ordemGrafo(self):
            return self.vertices

    #-------TAMANHO DO GRAFO--------------#
    def tamanhoGrafo(self): 
        somaGraus = 0
        for i in range(self.vertices):
            somaGraus += self.grauVertice(i)
        
        return int(self.vertices + somaGraus/2)

    #--------RETORNA VIZINHOS DE UM VERTICE FORNECIDO--------#
    def retornaVizinhos(self, u):
        vizinhos = []
        c =1
        listaVizinhos = self.grafo[u-1]
        for i in listaVizinhos:
            if i!=0:
                vizinhos.append(c)
            c+=1
        return vizinhos
    
    #--------GRAU DO VERTICE------#
    def grauVertice(self, u): 
        return len(self.retornaVizinhos(u))

    #-------LER GRAFO-----------#
    @staticmethod
    def leArquivo(nomeArquivo): 
        with open(nomeArquivo, 'r') as arq: 

            #lê a primeira linha
            vertices = arq.readline() 
            vertices = int(vertices)

            #cria o grafo G com a quantidade de vértices
            g = Grafo(vertices) 
            for line in arq:
                u, v, peso = line.rstrip('\n').split(' ')
                g.adiciona_aresta(int(u),int(v), float(peso))
            
        return g
    
    