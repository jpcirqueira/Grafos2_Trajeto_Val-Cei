import dijkstra

grafo_valparaiso_ceilandia = { 
        "Valparaiso" : { "SantaMaria" : 3.5 },
        "SantaMaria" : {"EPTC": 9.5, "GuaraII":22.5, "CruzeiroNovo": 32.4},
        "GuaraII" : { "CruzeiroNovo": 9.9, "SamambaiaSul": 14.2 },
        "EPTC" : { "GuaraII": 13, "CruzeiroNovo": 23.9, "SamambaiaSul":16.9},
        "CruzeiroNovo" : { "Ceilandia": 26.4 },
        "SamambaiaSul": {"Ceilandia": 13.1 , "BR-070": 24.3},
        "BR-070": {"Ceilandia": 9.6},
        "Ceilandia": { }
        }

print("os pontos de referencias de valparaiso a ceilandia: Santa Maria, EPTC, Guara II, Cruzeiro Novo, Samambaia Sul , BR-070")

dijkstra.dijkstra_distancia(grafo_valparaiso_ceilandia,"Valparaiso","Ceilandia")
##dijkstra.dijkstra_distancia(grafo,"A","E")