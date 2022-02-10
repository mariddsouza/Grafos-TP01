from Grafo import Grafo
from converteJSON import converteJSON

opcao = 1
while (opcao!=0):
    print("Selecione uma opção:")
    print("1 - Ler grafo a partir de um arquivo")
    print("2 - Converter arquivo JSON para o formato de entrada")
    print("0 - Sair")
    opcao = int(input())

    if (opcao == 1): # Lê arquivo
        arqInput = input("Digite o nome do arquivo: ")
        g = Grafo.leArquivo(arqInput)
        nomeOut = input("Digite o nome do arquivo de saída: ")
        with open(nomeOut, "w") as arqOut:
            g.imprimeGrafo(arqOut)

            arqOut.write("\n\n-----------------------------------------------------------------------\n\n")
            vertice = int(input(f'Selecione Vertice: (1 - {g.vertices})\n'))
            b = [0 for i in range(g.vertices+1)]
            a = [0 for i in range(g.vertices+1)]
            #g.exibeInformacoes(vertice)
            arqOut.write(f'Grafo de Ordem: {g.ordemGrafo()}\n')
            arqOut.write(f'Grafo de tamanho: {g.tamanhoGrafo()}\n')
            arqOut.write(f'Vizinhos do vértice {vertice}: {g.retornaVizinhos(vertice)}\n')
            arqOut.write(f'Grau do vértice {vertice}: {g.grauVertice(vertice)}\n')
            arqOut.write(f'Número de componentes conexas: {g.NumberOfconnectedComponents()}\n\n')
            grafoAux = Grafo.leArquivo(arqInput)
            arqOut.write(grafoAux.ehArticulacao(vertice))
            arqOut.write(grafoAux.ehPonte(vertice))
            arqOut.write("-----------------------------------------------------------------------\n\n")
            #visited = [False for i in range(g.vertices + 1)]
            #temp = []
            arqOut.write(f'Arestas de retorno: \n\n{g.DFSlista(vertice,b,a)[1]}\n\n\n\n')
            arqOut.write("-----------------------------------------------------------------------\n\n")
            arqOut.write(f'Lista da busca: \n\n{g.DFSlista(vertice,b,a)[0]}\n\n\n\n')
            arqOut.write("-----------------------------------------------------------------------\n\n")
            arqOut.write(f'Vértices de componentes conexas: \n\n{g.connectedComponents()}\n\n')
            print("Salvo como: " + nomeOut)
            print("\n")

    if (opcao == 2): # Lê arquivo JSON
        arqJSON = input("Digite o nome do arquivo JSON: ")
        arqOut = input("Digite o nome do arquivo de saída: ")
        converteJSON(arqJSON, arqOut)
