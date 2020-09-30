grafo = { "Rua A" : { "Rua B" : 1, "Rua C":2 },
          "Rua B" : { "Rua D":2, "Rua E":4 },
          "Rua C" : { "Rua E":3 },
          "Rua D" : { "Rua F": 6 },
          "Rua E" : { "Rua F": 6 },
          "Rua F" : { }
          }

def dijkstra(grafo, origem): #retorna a menor distancia de um dado nó para todos os outros possíveis.

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito

    distanciaAtual[atual] =0

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho] > pesoCalc:
                 distanciaAtual[vizinho] = pesoCalc
                 controle[vizinho] = distanciaAtual[vizinho]

        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print(distanciaAtual)


def dijkstra_distancia(grafo, origem, fim): #retorna a menor distancia de um No origem até um No destino e o caminho até ele

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice) #inclui os vertices nos não visitados    
        distanciaAtual[vertice] = float('inf') #inicia os vertices como infinito

    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 print(controle)
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1]) #seleciona o menor vizinho
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor distância da rua  %s até %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    print("O menor caminho é: %s" % print_distancia(distanciaAtual,origem, fim))          
    
def dijkstra_tempo(grafo, origem, fim): #retorna a menor tempo

    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    
    for vertice in grafo.keys():
        naoVisitados.append(vertice)    
        distanciaAtual[vertice] = float('inf') 

    distanciaAtual[atual] = [0,origem] 

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                 distanciaAtual[vizinho] = [pesoCalc,atual]
                 controle[vizinho] = pesoCalc
                 print(controle)
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1])
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor tempo da rua  %s para a rua%s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    ## print("O menor tempo é: %s" % print_distancia(distanciaAtual,origem, fim))          
    

def print_distancia(distancias,inicio, fim):
        if  fim != inicio:
            return "%s -- %s" % (print_distancia(distancias,inicio, distancias[fim][1]),fim)
        else:
            return inicio

