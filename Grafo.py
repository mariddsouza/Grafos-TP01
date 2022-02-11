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