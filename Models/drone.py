class Drone:
    def __init__(self, id, localizacao_base):
        self.id = id
        self.localizacao_base = localizacao_base
        self.ocorrencia_atual = None
        self.tempo_resposta = 0

    def despachar_para(self, ocorrencia):
        self.ocorrencia_atual = ocorrencia
        self.tempo_resposta = self.calcular_tempo_resposta(ocorrencia)
        return f"🚁 Drone {self.id} despachado para {ocorrencia.localizacao} (tempo estimado: {self.tempo_resposta} min)"

    def calcular_tempo_resposta(self, ocorrencia):
        # Distância simulada
        dist = abs(hash(self.localizacao_base) - hash(ocorrencia.localizacao)) % 10 + 1
        severidade = ocorrencia.severidade
        # Severidade influencia na velocidade (maior severidade = menor tempo)
        fator_urgencia = (11 - severidade) ** 1.5
        tempo = dist + fator_urgencia
        return max(2, int(tempo))

    def concluir_missao(self):
        if self.ocorrencia_atual:
            self.ocorrencia_atual.status = "Concluída"
            msg = f"✅ Drone {self.id} concluiu missão em {self.ocorrencia_atual.localizacao}."
            self.ocorrencia_atual = None
            return msg
        return f"Drone {self.id} não possui missão em andamento."
