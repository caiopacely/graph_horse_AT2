from graph import Graph

class Cycle:
    def __init__(self, G):
        self.marked = [False for _ in range(G.V())]
        self.edge_to = [0 for _ in range(G.V())] # Guarda de onde cada vértice veio
        self._cycle = None # Onde guardaremos o caminho do ciclo (pilha/lista)
        
        for s in range(G.V()):
            if not self.marked[s]:
                if self._cycle is not None: break # Já achou um ciclo, para tudo
                self.dfs(G, s, -1)

    def dfs(self, G, v, u):
        self.marked[v] = True
        for w in G.adj(v):
            if self._cycle is not None: return # Ciclo já encontrado
            
            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w, v)
            elif w != u:
                # Ciclo detectado! Vamos reconstruir o caminho
                self._cycle = []
                x = v
                while x != w:
                    self._cycle.append(x)
                    x = self.edge_to[x]
                self._cycle.append(w)
                self._cycle.append(v) # Fecha o ciclo voltando ao início

    def hasCycle(self):
        return self._cycle is not None

    def cycle(self):
        """Retorna o ciclo encontrado como uma lista."""
        return self._cycle