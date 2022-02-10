class Grafo:
    #Implementa Grafos nao direcionados ponderados

    def __init__(self, vertices):
        self.vertices = vertices
        self.listaAdj = [[] for i in range(self.vertices+1)] #conteudo das linhas em branco, vertices = numero de linhas

    def adicionaAresta(self, u, v, peso):
        self.listaAdj[u].append([v, peso]) #adiciona v e o peso na linha/vertice u
        self.listaAdj[v].append([u, peso]) #adiciona u e o peso na linha/vertice v

    def imprimeGrafo(self):
        for i in range(1,self.vertices+1):
            print(f'{i}:', end='  ')
            '''arqOut.write(f'{i}: ')'''
            for j in self.listaAdj[i]:
                print(f'{j} -', end='  ')
                '''arqOut.write(f'{j} - ')'''
            print('')
            '''arqOut.write('\n')'''
        print('')
        '''arqOut.write('\n')'''


    def exibeInformacoes(self, v):
        print(f'Grafo de Ordem: {self.ordemGrafo()}')
        print(f'Grafo de tamanho: {self.tamanhoGrafo()}')
        print(f'Vizinhos do vértice {v}: {self.retornaVizinhos(v)}')
        print(f'Grau do vértice {v}: {self.grauVertice(v)}')
        visited = [False for i in range(self.vertices + 1)]
        temp = []
        print(f'Lista da busca: {self.DFSlista(v, visited, temp)[0]}')
        print(f'Número de componentes conexas: {self.NumberOfconnectedComponents()}')
        print(f'Vértices de componentes conexas: {self.connectedComponents()}')
                
    def ordemGrafo(self):
        return self.vertices

    def tamanhoGrafo(self): #tamanho = nVértices + nArestas (n arestas = Soma dos Graus dos vertices/2)
        somaGraus = 0
        for i in range(self.vertices):
            somaGraus += self.grauVertice(i)

        return int(self.vertices + somaGraus/2)

    def retornaVizinhos(self, u):
        vizinhos = []
        listaVizinhos = self.listaAdj[u]
        i=0
        while (i<len(listaVizinhos)):
            vizinhos.append(listaVizinhos[i][0])
            i+=1
        return vizinhos

    def grauVertice(self, u): #Grau = n de vertices ligados a ele/ n de vizinhos
        return len(self.retornaVizinhos(u))

    @staticmethod
    def leArquivo(nomeArquivo): #Função para ler e criar grafo a partir de arquivo, retorna o grafo criado
        with open(nomeArquivo, 'r') as arq: #Para chamar utilize nomeGrafo = Grafo.leArquivo(nomeArquivo)
            vertices = arq.readline() #lê a primeira linha
            vertices = int(vertices)
            g = Grafo(vertices) #cria o grafo G com a quantidade de vértices
            for line in arq:
                u, v, peso = line.rstrip('\n').split(' ')
                g.adicionaAresta(int(u), int(v), float(peso))
        return g
    def dfs(self, vertice):
        visitados = set()
        teste=[]
        def dfs_iterativa(self, vertice_fonte):
            visitados.add(vertice_fonte)
            falta_visitar = [vertice_fonte]
            
            while falta_visitar:
                vertice = falta_visitar.pop()
                for vizinho in self.listaAdj[vertice]:
                    teste.append(vizinho[0])
                    if vizinho[0] not in visitados:
                        visitados.add(vizinho[0])
                        falta_visitar.append(vizinho[0])

        dfs_iterativa(self, vertice)
        return teste
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

    def _DFS(self, s, visited, temp):  # prints all vertices in DFS manner from a given source.
                    # Initially mark all verices as not visited


        # Create a stack for DFS
        stack = []

            # Push the current source node.
        stack.append(s)

        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                temp.append(s)
                #print(s, end=' ')
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.listaAdj[s]:
                    if (not visited[node[0]]):
                        stack.append(node[0])
                        #print(f'Arestas de Retorno: {s} - {node[0]}')
        return temp

    def DFSlista(self, s, visited, temp):  # prints all vertices in DFS manner from a given source.
        # Initially mark all verices as not visited
        # Create a stack for DFS
        stack = []
        arestas = []
        # Push the current source node.
        stack.append(s)
        while (len(stack)):
            # Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if (not visited[s]):
                temp.append(s)
                # print(s, end=' ')
                visited[s] = True
            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.listaAdj[s]:

                if (not visited[node[0]]):
                    stack.append(node[0])
                    arestas.append([s , node[0]])
        while 0 in temp:
            temp.remove(0)
        return temp, arestas

    def ehArticulacao(self, vertice):#Remove o vertice selecionado, se
                                    #Numero de componentes conexas aumenta, é articulação
        ccInicial = self.NumberOfconnectedComponents() #antes de remover o vertice
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

    def ehPonte(self, v1):
        v2 = int(input(f'Selecione um segundo vértice para verificar se a aresta é ponte: (1 - {self.vertices}): \n'))
        ccInicial = self.NumberOfconnectedComponents()  # antes de remover o vertice
        for aresta in self.listaAdj[v1]:
            if (aresta[0] == v2):
                self.listaAdj[v1].remove(aresta)
        ccFinal = self.NumberOfconnectedComponents()
        if (ccFinal > ccInicial):
            return f'A aresta {v1} - {v2} é ponte\n'
        else:
            return f'A aresta {v1} - {v2} não é ponte\n'

    def getPesoAresta(self, v1, v2):
        aresta = []
        vizinhosV1 = self.listaAdj[v1]
        for j in range(len(vizinhosV1)):
            if (vizinhosV1[j][0] == v2):
                aresta = vizinhosV1[j][1]
        return aresta
