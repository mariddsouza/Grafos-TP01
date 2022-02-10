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


     # Adiciona aresta (não direcionada)
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 

    #Função para remover a aresta u-v do grafo
    def rmvEdge(self, u, v): 
        for index, key in enumerate(self.graph[u]): 
            if key == v: 
                self.graph[u].pop(index) 
        for index, key in enumerate(self.graph[v]): 
            if key == u: 
                self.graph[v].pop(index) 
        ### Importante - auxiliar para verificar pontes ###
  # Função baseada no DFS para contar os vértices alcançaveis por meio do vértice V.
    def DFSCount(self, v, visited): 
        count = 1
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                count = count + self.DFSCount(i, visited)        
        return count 

    # Função que verifica se a aresta u-v pode ser considerada uma aresta no Tour de Euler
    def isValidNextEdge(self, u, v): 
        # A aresta u-v é valida em um dos seguintes casos: 

        # 1) Se v é o único vértice adjacente a u
        if len(self.graph[u]) == 1: 
            return True
        else: 
            ''' 
            2) Caso existam múltiplos vértices adjacentes u-v
            verificar se não é uma ponte
                
            Para checarmos se é uma ponte: 
            2.a) contamos os vértices alcançaveis a partir de u'''  
            visited =[False]*(self.V) 
            count1 = self.DFSCount(u, visited) 

            '''2.b) Remove a aresta (u, v) e após remover verificamos a quantidade de vértices alcançaveis a partir de u novamente'''
            self.rmvEdge(u, v) 
            visited =[False]*(self.V) 
            count2 = self.DFSCount(u, visited) 

            #2.c) Retornamos a aresta ao grafo, pois ela só foi removida para verificar se formavam-se pontes
            self.addEdge(u,v) 

            # 2.d) Se count1 é maior que count2, então a aresta (u, v) é uma ponte e não pode ser removida retornando falso.
            return False if count1 > count2 else True


    # Printa o tour de Euler tour começando pelo vértice u 
    def printEulerUtil(self, u): 
        #Recorre para todos os vértices adjacentes a este vértice
        for v in self.graph[u]: 
            #Se a vertice u-v não for removida e for uma próxima borda válida
            if self.isValidNextEdge(u, v): 
                print("%d-%d " %(u,v)), 
                self.rmvEdge(u, v) 
                self.printEulerUtil(v) 


    
    '''The main function that print Eulerian Trail. It first finds an odd 
    degree vertex (if there is any) and then calls printEulerUtil() 
    to print the path '''
    def printEulerTour(self): 
        #encontre um vertice com grau impar 
        u = 0
        for i in range(self.V): 
            if len(self.graph[i]) %2 != 0 : 
                u = i 
                break
        # Imprimir tour começando do vértice ímpar 
        print ("\n") 
        self.printEulerUtil(u)



    #KRUSKAL
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)
    