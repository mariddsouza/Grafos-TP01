import json

def converteJSON(inputFile, outputFile):
    with open(inputFile, 'r') as arq:
        arq = arq.read()
        jsonFile = json.loads(arq)
        vertices = jsonFile["data"]["nodes"]["_data"]
        arestas = jsonFile["data"]["edges"]["_data"]
        tamanhoGrafo = len(vertices)
        with open(outputFile, 'w') as out:
            out.write(f'{str(tamanhoGrafo)}\n')
            for idAresta in arestas:
                linha = f'{str(arestas[idAresta]["from"])} {str(arestas[idAresta]["to"])} {str(arestas[idAresta]["label"])}\n'
                out.write(linha)
        print("Salvo como: " + outputFile)
