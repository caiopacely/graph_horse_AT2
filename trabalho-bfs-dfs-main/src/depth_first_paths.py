"""
depth_first_paths.py
--------------------
Busca em Profundidade (DFS) a partir de um vértice de origem,
seguindo o estilo da classe DepthFirstPaths da biblioteca algs4.

Permite:
  - Verificar se há caminho entre a origem e qualquer vértice.
  - Recuperar o caminho encontrado pela DFS.
  - Consultar a ordem de visita dos vértices.
  - Listar todos os vértices alcançáveis a partir da origem.
"""

from graph import Graph


class DepthFirstPaths:
    """
    DFS a partir de um vértice de origem em um grafo não-dirigido.
    """

    def __init__(self, g: Graph, s: int):
        """
        Executa DFS no grafo `g` a partir do vértice `s`.

        Parâmetros
        ----------
        g : Graph
            O grafo a ser explorado.
        s : int
            Vértice de origem.
        """
        self._marked = [False] * g.V()   # marked[v] = vértice v já foi visitado?
        self._edge_to = [-1] * g.V()     # edge_to[v] = vértice anterior no caminho até v
        self._source = s
        self._visit_order: list[int] = []  # ordem de visita dos vértices

        self._dfs(g, s)

    # ------------------------------------------------------------------
    # Núcleo recursivo da DFS
    # ------------------------------------------------------------------

    def _dfs(self, g: Graph, v: int) -> None:
        self._marked[v] = True
        self._visit_order.append(v)
        for w in g.adj(v):
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(g, w)

    # ------------------------------------------------------------------
    # Consultas
    # ------------------------------------------------------------------

    def has_path_to(self, v: int) -> bool:
        """Retorna True se existe caminho da origem até v."""
        return self._marked[v]

    def path_to(self, v: int) -> list[int] | None:
        """
        Retorna o caminho da origem até v encontrado pela DFS,
        ou None se não houver caminho.
        """
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self._source:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._source)
        path.reverse()
        return path

    def reachable(self) -> list[int]:
        """Retorna lista de todos os vértices alcançáveis a partir da origem."""
        return [v for v in range(len(self._marked)) if self._marked[v]]

    def visit_order(self) -> list[int]:
        """Retorna a ordem em que os vértices foram visitados pela DFS."""
        return list(self._visit_order)
