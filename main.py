from Grafo import Grafo
from converteJSON import converteJSON

opcao = 1
while (opcao!=0):
    print("\n")
    print("|----------------------------------------------------------------------|")
    print("|----------Teoria e Modelo de Grafos - Trabalho Prático I--------------|")
    print("|                                                                      |")
    print("|----------BIBLIOTECA GRAFOS NAO DIRECIONADOS E PONDERADOS-------------|")
    print("|                                                                      |")
    print("|---------------------Selecione uma opção:-----------------------------|")
    print("| (1) - Ler grafo a partir de um arquivo                               |")
    print("| (2) - Converter arquivo JSON para o formato de entrada               |")
    print("| (0) - Sair                                                           |")
    print("|----------------------------------------------------------------------|")
    opcao = int(input())