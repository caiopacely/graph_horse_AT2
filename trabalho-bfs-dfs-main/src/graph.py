"""
graph.py
--------
Representação de um grafo não-dirigido por lista de adjacência,
seguindo o estilo da biblioteca algs4.

"""


class Graph:
    """Grafo não-dirigido representado por lista de adjacência."""

    # Casas do tabulerio seguindo a ordem 
    CASAS_TAB = [1,2,3,4,5,6,7,8]

    def __init__(self, V: int):
        """Inicializa um grafo com V vértices e nenhuma aresta."""
        if V < 0:
            raise ValueError("O número de vértices deve ser não-negativo.")
        self._V = V
        self._E = 0
        self._adj = [[] for _ in range(V)]

    # ------------------------------------------------------------------
    # Métodos de construção
    # ------------------------------------------------------------------

    def add_edge(self, v: int, w: int) -> None:
        """Adiciona a aresta v-w ao grafo (não-dirigido)."""
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._E += 1

    # ------------------------------------------------------------------
    # Métodos de consulta
    # ------------------------------------------------------------------

    def V(self) -> int:
        """Retorna o número de vértices."""
        return self._V

    def E(self) -> int:
        """Retorna o número de arestas."""
        return self._E

    def adj(self, v: int):
        """Retorna os vizinhos do vértice v."""
        self._validate_vertex(v)
        return iter(self._adj[v])

    # ------------------------------------------------------------------
    # Fábrica: cria grafo a partir de arquivo no formato algs4
    # ------------------------------------------------------------------

    @classmethod
    def from_file(cls, filepath: str) -> "Graph":
        """
        Lê um arquivo no formato algs4 (ignorando linhas iniciadas com '#')
        e retorna o grafo construído.

        Formato esperado (linhas de comentário com # são opcionais):
            <nº de vértices>
            <nº de arestas>
            <v> <w>
            ...
        """
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [
                linha.strip()
                for linha in f
                if linha.strip() and not linha.strip().startswith("#")
            ]

        V = int(lines[0])
        E_esperado = int(lines[1])
        g = cls(V)

        for linha in lines[2:2 + E_esperado]:
            partes = linha.split()
            v, w = int(partes[0]), int(partes[1])
            g.add_edge(v, w)

        return g

    # ------------------------------------------------------------------
    # Utilitários
    # ------------------------------------------------------------------

    def _validate_vertex(self, v: int) -> None:
        if not (0 <= v < self._V):
            raise ValueError(f"Vértice {v} está fora do intervalo [0, {self._V - 1}].")

    def listaAdj(self):
        """Imprime a lista de adjacência de todos os vértices."""
        print(f"{'ID':<5} | {'Adjacentes'}")
        print("-" * 25)
        for c in range(self._V):
            vizinhos = list(self.adj(c))
            print(f"{c:<5} | {vizinhos}")
            
    def __str__(self) -> str:
            linhas = ["\n" + "="*20 + " ESTRUTURA DO GRAFO " + "="*20]
            linhas.append(f"Vértices: {self._V} | Arestas: {self._E}")
            # Cabeçalho da tabela
            linhas.append(f"{'ID':<5} {'Casa (r,c)':<12} {'Lista de Adjacência'}")
            linhas.append("-" * 55)
            
            for v in range(self._V):
                # Obtém o label (ex: (0,0))
                label = self.vertex_label(v)
                
                # Formata os vizinhos como uma lista: [5, 7]
                # w representa o ID e self.vertex_label(w) a coordenada
                vizinhos = [f"{w}{self.vertex_label(w)}" for w in self._adj[v]]
                adj_str = ", ".join(vizinhos) if vizinhos else "Nenhum (Isolado)"
                
                linhas.append(f"{v:<5} {label:<12} [{adj_str}]")
                
            return "\n".join(linhas)
