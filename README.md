## 🐎 Grafo do Cavalo (Tabuleiro 3x3)

modelagem e análise técnica do Grafo do Cavalo em um tabuleiro de xadrez 3X3, través da implementação de algoritmos fundamentais de teoria dos grafos, utilizando algoritmos de busca em profundidade (DFS) e busca em largura (BFS) em Python.

---

## Apresentação

🔗 **[Assista à apresentação do trabalho aqui](https://www.youtube.com/watch?v=PSVaUfwmq58)**

---

##📌 Sobre o Projeto

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

##▶️ Como Executar

```
Clone o repositório: git clone https://github.com/caiopacely/graph_horse_movements.git
Acesse a pasta: cd trabalho-bfs-dfs-main/src
Execute o programa: python main.py
```

## Perguntas Respondidas

1. Qual é a lista de adjacência do grafo (como os vértices estão conectados)?
2. Quantas componentes conexas existem e quais vértices pertencem a cada uma?
3. Qual é a distância mínima entre `(0,0)` e `(2,2)` utilizando BFS?
4. O grafo possui ciclo?
5. Quais são os vértices de um ciclo encontrado no grafo?


## Referência

Estrutura e nomenclatura baseadas na biblioteca [algs4](https://algs4.cs.princeton.edu/home/) de Sedgewick & Wayne.
