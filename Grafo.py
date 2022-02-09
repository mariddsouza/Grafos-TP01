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
        listaVizinhos = self.listaAdj[u]
        i=0
        while (i<len(listaVizinhos)):
            vizinhos.append(listaVizinhos[i][0])
            i+=1
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
                g.adicionaAresta(int(u), int(v), float(peso))
        return g
    
    #---------VERIFICA ARTICULACAO--------#
    def ehArticulacao(self, vertice):

        #Remove o vertice selecionado, se o numero de componentes conexas aumenta, é articulação    
        #antes de remover o vertice     
        ccInicial = self.NumberOfconnectedComponents() 
        verticeRemovido = []
        for aresta in self.listaAdj[vertice]:
            verticeRemovido.append(aresta)

        self.listaAdj[vertice].clear()
        ccFinal = self.NumberOfconnectedComponents()
        self.listaAdj[vertice] = verticeRemovido

        if (ccFinal > ccInicial):
            return f'O vértice {vertice} é articulação\n'
        else:
            return f'O vértice {vertice} não é articulação\n'

    #-------VERTICES DE CADA COMPONENTE-------#
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.vertices+1):
            visited.append(False)
        for v in range(self.vertices+1):
            if visited[v] == False:
                temp = []
                #cc.append(self.DFSUtil(temp, v, visited))
                cc.append(self._DFS(v, visited, temp))
        return cc[1:]
    
    #------NUMERO DE COMPONENTES CONEXAS DO GRAFO------#
    def NumberOfconnectedComponents(self):
         
        # marcar todos vertices como n visitados
        visited = [False for i in range(self.vertices+1)]
         
        # armazenar o numero de componentes conectados
        count = 0
        temp = []
        for v in range(self.vertices+1):
            if (visited[v] == False):
                #self.DFSUtil2(v, visited)
                self._DFS(v, visited, temp)
                count += 1

        return count-1

    