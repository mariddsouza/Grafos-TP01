from Grafo import Grafo
from converteJSON import converteJSON

opcao = 1
while (opcao!=0):
    print("\n")
    print("|----------------------------------------------------------------------|")
    print("|----------Teoria e Modelo de Grafos - Trabalho Prático I--------------|")
    print("|                                 1                                     |")
    print("|----------BIBLIOTECA GRAFOS NAO DIRECIONADOS E PONDERADOS-------------|")
    print("|                                                                      |")
    print("|---------------------Selecione uma opção:-----------------------------|")
    print("| (1) - Ler grafo a partir de um arquivo                               |")
    print("| (2) - Converter arquivo JSON para o formato de entrada               |")
    print("| (0) - Sair                                                           |")
    print("|----------------------------------------------------------------------|")
    opcao = int(input())

    if (opcao == 1): 
        print("\n")
        arqInput = input("Insira o nome do arquivo de entrada: ")
        g = Grafo.leArquivo(arqInput)
        nomeOut = input("Insira o nome do arquivo de saida: ")

        with open(nomeOut, "w") as arqOut:
            arqOut.write("\n--------------------------IMPRIMINDO GRAFO--------------------------------------\n")

            g.mostra_matriz(arqOut)
        
            arqOut.write("\n----------------------------------------------------------------------------\n")
            vertice = int(input(f'Selecione o vertice: (1 - {g.vertices})\n'))
            b = [0 for i in range(g.vertices+1)]
            a = [0 for i in range(g.vertices+1)]

            arqOut.write("--------------------------ARQUIVO DE SAIDA--------------------------------------\n")

            arqOut.write(f'Grafo de Ordem: {g.ordemGrafo()}\n')
            arqOut.write("\n")
            arqOut.write(f'Grafo de tamanho: {g.tamanhoGrafo()}\n')
            arqOut.write("\n")
            arqOut.write(f'Vizinhos do vértice {vertice}: {g.retornaVizinhos(vertice)}\n')
            arqOut.write("\n")
            arqOut.write(f'Grau do vertice {vertice}: {g.grauVertice(vertice)}\n')
            arqOut.write(f'Ciclo euleriano: \n')
            g.printEulerTour(arqOut)
            arqOut.write("\n")
            
            grafoAux = Grafo.leArquivo(arqInput)
            arqOut.write("Verifica Articulação")

