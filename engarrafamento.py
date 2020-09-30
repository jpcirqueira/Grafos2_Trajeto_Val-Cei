def main(grafo,inicio,fim, intensidade):
    
        if intensidade == "leve":
                aux = 1.7
        elif intensidade == "moderado":
                aux = 2.4
        elif intensidade == "pesado":
                aux = 3.0

        for nome, dado in grafo.items():
                if nome == inicio:
                        for key in dado:
                                if key == fim:
                                        dado[key] *= aux
                                        return grafo
        return grafo
        