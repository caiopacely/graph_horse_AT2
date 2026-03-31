"""
breadth_first_paths.py
----------------------
Busca em Largura (BFS) a partir de um vértice de origem,
seguindo o estilo da classe BreadthFirstPaths da biblioteca algs4.

Permite:
  - Verificar se há caminho entre a origem e qualquer vértice.
  - Recuperar o caminho de menor número de arestas (BFS).
  - Consultar a ordem de visita dos vértices.
  - Listar todos os vértices alcançáveis a partir da origem.
"""

from collections import deque
from graph import Graph


class BreadthFirstPaths:
    """
    BFS a partir de um vértice de origem em um grafo não-dirigido.
    Garante o caminho com menor número de arestas entre origem e destino.
    """

    def __init__(self, g: Graph, s: int):
        """
        Executa BFS no grafo `g` a partir do vértice `s`.

        Parâmetros
        ----------
        g : Graph
            O grafo a ser explorado.
        s : int
            Vértice de origem.
        """
        self._marked = [False] * g.V()   # marked[v] = vértice v já foi visitado?
        self._edge_to = [-1] * g.V()     # edge_to[v] = vértice anterior no caminho até v
        self._dist_to = [-1] * g.V()     # dist_to[v] = distância (em arestas) da origem a v
        self._source = s
        self._visit_order: list[int] = []  # ordem de visita dos vértices

        self._bfs(g, s)

    # ------------------------------------------------------------------
    # Núcleo iterativo da BFS
    # ------------------------------------------------------------------

    def _bfs(self, g: Graph, s: int) -> None:
        queue: deque[int] = deque()
        self._marked[s] = True
        self._dist_to[s] = 0
        queue.append(s)
        self._visit_order.append(s)

        while queue:
            v = queue.popleft()
            for w in g.adj(v):
                if not self._marked[w]:
                    self._marked[w] = True
                    self._edge_to[w] = v
                    self._dist_to[w] = self._dist_to[v] + 1
                    queue.append(w)
                    self._visit_order.append(w)

    # ------------------------------------------------------------------
    # Consultas
    # ------------------------------------------------------------------

    def has_path_to(self, v: int) -> bool:
        """Retorna True se existe caminho da origem até v."""
        return self._marked[v]

    def path_to(self, v: int) -> list[int] | None:
        """
        Retorna o caminho de menor número de arestas da origem até v,
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

    def dist_to(self, v: int) -> int:
        """Retorna a distância (número de arestas) da origem até v, ou -1."""
        return self._dist_to[v]

    def reachable(self) -> list[int]:
        """Retorna lista de todos os vértices alcançáveis a partir da origem."""
        return [v for v in range(len(self._marked)) if self._marked[v]]

    def visit_order(self) -> list[int]:
        """Retorna a ordem em que os vértices foram visitados pela BFS."""
        return list(self._visit_order)
