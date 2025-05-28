class Drone:
    def __init__(self, id, localizacao_base):
        self.id = id
        self.localizacao_base = localizacao_base
        self.ocorrencia_atual = None
        self.tempo_resposta = 0

    def despachar_para(self, ocorrencia):
        self.ocorrencia_atual = ocorrencia
        self.tempo_resposta = self.calcular_tempo_resposta(ocorrencia)
        return f"Drone {self.id} despachado para {ocorrencia.localizacao} (tempo estimado: {self.tempo_resposta} min)"

    def calcular_tempo_resposta(self, ocorrencia):
        # Distância simulada (0 a 20)
        dist = abs(hash(self.localizacao_base) - hash(ocorrencia.localizacao)) % 20 + 1
        # Severidade influencia na velocidade (maior severidade = menor tempo)
        fator_urgencia = 11 - ocorrencia.severidade  # severidade 10 → fator 1 (mais rápido)
        tempo = dist + fator_urgencia  # tempo final mínimo controlado pela severidade
        return max(2, int(tempo))

    def concluir_missao(self):
        msg = f"Drone {self.id} concluiu missão em {self.ocorrencia_atual.localizacao}."
        self.ocorrencia_atual = None
        return msg
