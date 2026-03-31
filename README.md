# 🐎 Grafo do Cavalo (Tabuleiro 3x3)

Modelagem do grafo de movimentação de uma peça de cavalo em um tabuleiro de xadrez 3 × 3, utilizando algoritmos de busca em profundidade (DFS) e busca em largura (BFS) em Python.

📌 Sobre o Projeto

O programa modela as 9 casas de um tabuleiro 3×3 como um grafo não-direcionado:
Vértices: representam as posições no tabuleiro (row, col)
Arestas: representam movimentos válidos do cavalo (movimento em "L")

🎯 Objetivos
Analisar a conectividade do grafo
Identificar casas isoladas
Detectar ciclos de movimentação
Calcular a distância mínima entre vértices

## 🧩 Estrutura do Projeto

```
trabalho-bfs-dfs/
├── dados/                       # Arquivo de entrada do grafo
│   └── xadrez.txt               # Grafo no formato algs4 (V, E, arestas)
├── src/                         # Código-fonte do projeto
│   ├── main.py                  # Ponto de entrada (execução das análises)
│   ├── graph.py                 # Estrutura de dados do grafo
│   ├── cc.py                    # Componentes conexas (DFS)
│   ├── cycle.py                 # Detecção de ciclos (DFS)
│   ├── depth_first_paths.py     # Caminhos usando DFS
│   └── breadth_first_paths.py   # Caminhos mínimos usando BFS
└── README.md                    # Documentação do projeto
```

##🧭 Mapeamento dos Vértices (3×3)

```
Índice	Coordenada	Posição
0	(0,0)	Canto superior esquerdo
1	(0,1)	Topo centro
2	(0,2)	Canto superior direito
3	(1,0)	Meio esquerda
4	(1,1)	Centro (isolado)
5	(1,2)	Meio direita
6	(2,0)	Canto inferior esquerdo
7	(2,1)	Baixo centro
8	(2,2)	Canto inferior direito
```

##🔗 Arestas (Movimentos Válidos do Cavalo)

No tabuleiro 3×3, o cavalo possui apenas 8 conexões possíveis, formando um ciclo entre as bordas:
```
0 - 5   (0,0) → (1,2)
0 - 7   (0,0) → (2,1)
1 - 6   (0,1) → (2,0)
1 - 8   (0,1) → (2,2)
2 - 3   (0,2) → (1,0)
2 - 7   (0,2) → (2,1)
3 - 8   (1,0) → (2,2)
5 - 6   (1,2) → (2,0)
⚠️ O vértice 4 (centro) não possui arestas → nó isolado
```

#▶️ Como Executar

```
Clone o repositório: git clone https://github.com/caiopacely/graph_horse_movements.git
Acesse a pasta: cd trabalho-bfs-dfs-main/src
Execute o programa: python main.py
```
## ❓ Perguntas Respondidas

O programa lê o arquivo `xadrez.txt` e mostra no console:

* **Lista de Adjacência:** como os vértices do grafo estão conectados.

* **Componentes Conexas:** quantidade de componentes e quais vértices pertencem a cada uma (incluindo o vértice 4 isolado).

* **Distância Mínima:** menor caminho entre `(0,0)` e `(2,2)` usando BFS.

* **Análise de Ciclo:** informa se o grafo possui ciclo e sua complexidade.

* **Vértices do Ciclo:** mostra um ciclo encontrado, caso exista.


🔹 DFS vs BFS
Algoritmo	Característica
DFS	Explora profundamente (não garante menor caminho)
BFS	Encontra o menor caminho

#📚 Referência

```
Implementação baseada nos algoritmos de:
Robert Sedgewick
Kevin Wayne
📍 Princeton University
📦 Biblioteca: algs4
```
