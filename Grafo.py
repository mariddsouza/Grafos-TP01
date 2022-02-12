#Implementa as funções para a biblioteca de Grafos nao direcionados ponderados
from collections import defaultdict 
min_index=0
class Grafo:
   
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo2 = defaultdict(list)
        self.graph = []
        #conteudo das linhas em branco, vertices = numero de linhas
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.adj = [[] for i in range(vertices)]
        self.Time = 0
    

    def adiciona_aresta(self, u, v, p):
        # estou pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = p  #trocar = por += ser for grafo múltiplo

        self.grafo[v-1][u-1] = p 
    #so pra ficar mais facil de testar
    def mostra_matriz(self, arqOut):
        for i in range(self.vertices):
            arqOut.write(f'\n{self.grafo[i]}')


    #----------------------------------------------FUNCOES DO TRABALHO-----------------------------------------#
    
    #--------ORDEM DO GRAFO----------------#
    def ordemGrafo(self):
            return self.vertices
    #-------Densidade---------------
    def densidade_grafo(self):
        return self.tamanhoGrafo() / self.ordemGrafo()
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
                g.addEdge(int(u)-1,int(v)-1)
                g.addEdgeKruskal(int(u)-1,int(v)-1, float(peso))
                g.addc(int(u),int(v))
            
        return g
    
    
    #-------Euleriano-----------#
    # Adiciona aresta (não direcionada)
    def addEdge(self,u,v): 
        self.grafo2[u].append(v) 
        self.grafo2[v].append(u) 

    #Função para remover a aresta u-v do grafo
    def rmvEdge(self, u, v): 
        for index, key in enumerate(self.grafo2[u]): 
            if key == v: 
                self.grafo2[u].pop(index) 
        for index, key in enumerate(self.grafo2[v]): 
            if key == u: 
                self.grafo2[v].pop(index) 

  ### Importante - auxiliar para verificar pontes ###
  # Função baseada no DFS para contar os vértices alcançaveis por meio do vértice V.
    def DFSCount(self, v, visited): 
        count = 1
        visited[v] = True
        for i in self.grafo2[v]: 
            if visited[i] == False: 
                count = count + self.DFSCount(i, visited)        
        return count 

    # Função que verifica se a aresta u-v pode ser considerada uma aresta no Tour de Euler
    def isValidNextEdge(self, u, v): 
        # A aresta u-v é valida em um dos seguintes casos: 

        # 1) Se v é o único vértice adjacente a u
        if len(self.grafo2[u]) == 1: 
            return True
        else: 
            ''' 
            2) Caso existam múltiplos vértices adjacentes u-v
            verificar se não é uma ponte
                
      Para checarmos se é uma ponte: 
            2.a) contamos os vértices alcançaveis a partir de u'''  
            visited =[False]*(self.vertices) 
            count1 = self.DFSCount(u, visited) 

            '''2.b) Remove a aresta (u, v) e após remover verificamos a quantidade de vértices alcançaveis a partir de u novamente'''
            self.rmvEdge(u, v) 
            visited =[False]*(self.vertices) 
            count2 = self.DFSCount(u, visited) 

            #2.c) Retornamos a aresta ao grafo, pois ela só foi removida para verificar se formavam-se pontes
            self.addEdge(u,v) 

            # 2.d) Se count1 é maior que count2, então a aresta (u, v) é uma ponte e não pode ser removida retornando falso.
            return False if count1 > count2 else True


    # Printa o tour de Euler tour começando pelo vértice u 
    def printEulerUtil(self, u,arqOut,c): 
        #Recorre para todos os vértices adjacentes a este vértice
        for v in self.grafo2[u]: 
            #Se a vertice u-v não for removida e for uma próxima borda válida
            if self.isValidNextEdge(u, v): 
                arqOut.write(f'{u}-{v} , ') 
                self.rmvEdge(u, v) 
                c+=1
                self.printEulerUtil(v,arqOut,c)
                
        if c==0:
            arqOut.write('Não é euleriano\n')
        else:
            return

    def printEulerTour(self,arqOut): 
        #encontre um vertice com grau impar 
        u = 0
        for i in range(self.vertices): 
            if len(self.grafo2[i]) %2 != 0 : 
                u = i
                
                break
        # Imprimir tour começando do vértice ímpar  
        self.printEulerUtil(u,arqOut,0)
  
  #------------------KRUSKAL--------
    
    
    def addEdgeKruskal(self, u, v, w):
        self.graph.append([u, v, w])
 
    # Função para encontrar o conjunto de um elemento i
    # (usa comprensão de caminho)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # vai fazer a união dos conjuntos x e y
    # (usa união por rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Anexa uma árvore de classificação menor sob a raiz da árvore de classificação alta 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        #Se os ranks são os mesmos, então faça um como root e incremente seu rank em 1
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # Função principal que vai gerar a arvore minima usando kruskal
    def KruskalMST(self,arqOut):
 
        result = []  # vai armazenar a arvore resultante
         
        #index usado para ordenação
        i = 0
         
        #usado para o resultado[]
        e = 0
 
        '''Classifica todas as arestas em
        ordem não decrescente pelos pesos.
        Se não tivermos permissão para alterar o
        grafo, podemos criar uma cópia'''
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
 
        parent = []
        rank = []
 
        # Crie subconjuntos vertices com elementos únicos
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
 
        # O número de arestas a serem tomadas é igual a vertices-1
        while e < self.vertices - 1:
 
            # Passo 2: Escolha a menor aresta e incremente o índice para a próxima iteração
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            ''' Se a inclusão desta aresta não causar ciclo, 
            inclua-a no resultado e incremente o 
            índice de resultado para a próxima aresta'''
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Caso contrário, descarte a aresta
 
        minimumCost = 0
        arqOut.write("\nArvore Geradora Minima: \n")
        for u, v, weight in result:
            minimumCost += weight
            arqOut.write(f'{u+1} -- {v+1} == {weight}\n')
            
        arqOut.write(f'Peso total: {minimumCost} \n')

#----------------BFS---------
    def BFS(self,arqOut):
        visited = [0 for i in range(self.vertices)]

        # Add the start node to the queue
        # Node 0 in this case
        queue = [0]

        # Set the visited value of node 0 to visited
        visited[0] = 1

        # Dequeue node 0
        node = queue.pop(0)
        arqOut.write(f'{node+1} - ')

        while True:

            for x in range (0, len(visited)):

                            # Check is route exists and that node isn't visited
                if self.grafo[node][x] != 0 and visited[x] == 0:

                                    # Visit node
                    visited[x] = 1

                                    # Enqueue element
                    queue.append(x)

            # When queue is empty, break		
            if len(queue) == 0:
                break

            else:

                            # Dequeue element from queue
                node = queue.pop(0)
                arqOut.write(f'{node+1} - ')
    
#componentes conexas

    def Util(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v+1)
 
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.Util(temp, i, visited)
        return temp
     # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.vertices):
            visited.append(False)
        for v in range(self.vertices):
            if visited[v] == False:
                temp = []
                cc.append(self.Util(temp, v, visited))
        return cc
    def addc(self, v, w):
        self.adj[v-1].append(w-1)
        self.adj[w-1].append(v-1)

#grafo é ciclo

    def isCyclicUtil(self, v, visited, recStack):
 
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.grafo2[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
 
        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.vertices+1)
        recStack = [False] * (self.vertices+1)
        for node in range(self.vertices):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False

#articulaçao
    def APUtil(self, u, visited, ap, parent, low, disc):
 
        # Count of children in current node
        children = 0
 
        # Mark the current node as visited and print it
        visited[u]= True
 
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
 
        # Recur for all the vertices adjacent to this vertex
        for v in self.grafo2[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False :
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)
 
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])
 
                # u is an articulation point in following cases
                # (1) u is root of DFS tree and has two or more children.
                if parent[u] == -1 and children > 1:
                    ap[u] = True
 
                #(2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True   
                     
                # Update low value of u for parent function calls   
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
 
 
    # The function to do DFS traversal. It uses recursive APUtil()
    def AP(self,verticev,arqOut):
  
        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * (self.vertices)
        disc = [float("Inf")] * (self.vertices)
        low = [float("Inf")] * (self.vertices)
        parent = [-1] * (self.vertices)
        ap = [False] * (self.vertices) # To store articulation points
 
        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.vertices):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)
        ct=0
        for index, value in enumerate (ap):
            if value == True: 
                if index==verticev:
                    arqOut.write(f'\nO {verticev} é Articulaçao!!\n')
                    ct+=1
            else:
                if ct==0:                
                    arqOut.write(f'\nO {verticev} nao é Articulaçao!!\n')
                    ct+=1