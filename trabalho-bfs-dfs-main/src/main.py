"""
main.py
-------
Programa principal: modela o grafo de movimentação de um Cavalo em um 
tabuleiro 3x3 e responde perguntas sobre conectividade, ciclos e 
distâncias mínimas usando DFS (Busca em Profundidade) e BFS (Busca em Largura).

Mapeamento dos vértices (Tabuleiro 3x3):
    0: (0,0)  1: (0,1)  2: (0,2)
    3: (1,0)  4: (1,1)  5: (1,2)
    6: (2,0)  7: (2,1)  8: (2,2)

Uso:
    python main.py
    (o programa executa as análises sobre o Grafo do Cavalo 3x3 automaticamente)

Ou com argumentos para busca específica:
    python main.py 0 8
    (calcula o caminho entre o ID 0 (0,0) e o ID 8 (2,2))
"""

import sys
import os

# Garante que os módulos do projeto sejam encontrados
sys.path.insert(0, os.path.dirname(__file__))

from graph import Graph
from cc import CC
from cycle import Cycle
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths

# Caminho para o arquivo de dados (relativo à raiz do projeto)
DADOS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "dados", "xadrez.txt"
)


# -----------------------------------------------------------------------
# Funções auxiliares de formatação
# -----------------------------------------------------------------------


def separador(titulo: str = "", char: str = "=", largura: int = 60) -> None:
    if titulo:
        meio = f"  {titulo}  "
        lados = (largura - len(meio)) // 2
        print(char * lados + meio + char * lados)
    else:
        print(char * largura)


# -----------------------------------------------------------------------
# Programa principal
# -----------------------------------------------------------------------

def main() -> None:
    # --- Carrega o grafo ---
    g = Graph.from_file(DADOS_PATH)

    separador("GRAFO DO CAVALO") 
    separador("Lista de adjacência")   
    g.listaAdj()
      
    separador()     
    cc = CC(g)
    n_componentes = cc.count
    print(f"Componentes conexas: {n_componentes}")

    for i in range(n_componentes):
        vertices = []
        for v in range(g.V()):
            if cc.id[v] == i: 
                vertices.append(str(v))
        print(f"Vértices da componente {i}: {' '.join(vertices)}")
    separador()  
    
    cycle = Cycle(g)
    tem_ciclo = "Sim" if cycle.hasCycle() else "Não" 
    print(f"O grafo possui ciclo: {tem_ciclo}")
    
    if cycle.hasCycle():
    # Pega a lista do ciclo
        caminho = cycle.cycle()
        resultado = " ".join(map(str, caminho))       
        print(f"Um ciclo encontrado: {resultado}")
    else:
        print("O grafo não possui ciclos.")
    separador() 
    
    
   #Define origem (0,0) e destino (2,2)
    origem = 0  
    destino = 8 
    bfs = BreadthFirstPaths(g, origem)  #Executa a BFS

    if bfs.has_path_to(destino):
        distancia = bfs.dist_to(destino)  
        caminho = bfs.path_to(destino)    
        
        print(f"Distância mínima entre (0,0) e (2,2): {distancia}")
        print(f"Caminho: {' -> '.join(map(str, caminho))}")
    else:
        print("Não há caminho possível.")
    
    separador() 
        
if __name__ == "__main__":
    main()
