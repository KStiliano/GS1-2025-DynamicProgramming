import heapq

class FilaPrioridadeOcorrencias:
    def __init__(self):
        self.heap = []

    def inserir_ocorrencia(self, ocorrencia):
        heapq.heappush(self.heap, ocorrencia)

    def proxima_ocorrencia(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def listar_ocorrencias(self):
        return list(self.heap)

    def esta_vazia(self):
        return len(self.heap) == 0
