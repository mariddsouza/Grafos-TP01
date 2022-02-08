#Implementa as funções para a biblioteca de Grafos nao direcionados ponderados

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices

        #conteudo das linhas em branco, vertices = numero de linhas
        self.listaAdj = [[] for i in range(self.vertices+1)] 
    

    def adicionaAresta(self, u, v, peso):

        #adiciona v e o peso na linha/vertice u    
        self.listaAdj[u].append([v, peso]) 

        #adiciona u e o peso na linha/vertice v
        self.listaAdj[v].append([u, peso]) 

    
    def imprimeGrafo(self, arqOut):

        for i in range(1,self.vertices+1):
            print(f'{i}:', end='  ')
            arqOut.write(f'{i}: ')

            for j in self.listaAdj[i]:
                print(f'{j} -', end='  ')
                arqOut.write(f'{j} - ')
            print('')
            arqOut.write('\n')

        print('')
        arqOut.write('\n')


    #----------------------------------------------FUNÇÕES DO TRABALHO-----------------------------------------#
    
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
        listaVizinhos = self.listaAdj[u]
        i=0
        while (i<len(listaVizinhos)):
            vizinhos.append(listaVizinhos[i][0])
            i+=1
        return vizinhos
    
    #--------GRAU DO VERTICE------#
    def grauVertice(self, u): 
        return len(self.retornaVizinhos(u))