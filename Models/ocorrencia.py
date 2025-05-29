class Ocorrencia:
    def __init__(self, id, localizacao, intensidade, causa, clima, vegetacao, temperatura, umidade, vento):
        self.id = id
        self.status = "Pendente"
        self.localizacao = localizacao
        self.intensidade = intensidade  # escala de 1 a 10
        self.causa = causa
        self.clima = clima
        self.vegetacao = vegetacao
        self.temperatura = temperatura
        self.umidade = umidade
        self.vento = vento  # leve, moderado, forte
        self.severidade = self.calcular_severidade()

    def calcular_severidade(self):
        peso_intensidade = self.intensidade / 10  # de 0.0 a 1.0
        peso_vento = {"leve": 0.1, "moderado": 0.3, "forte": 0.5}[self.vento.lower()]
        peso_umidade = max(0, (100 - self.umidade) / 100) * 0.3  # menor umidade = mais risco
        peso_temp = max(0, (self.temperatura - 28) / 30) * 0.3  # acima de 28°C = mais risco
        peso_vegetacao = {"área urbana": 0.1, "pampas": 0.2, "caatinga": 0.4, "cerrado": 0.6, "mata atlântica": 0.8, "amazônia": 0.8}.get(self.vegetacao.lower(), 0.3)

        severidade_normalizada = peso_intensidade + peso_vento + peso_umidade + peso_temp + peso_vegetacao

        # Escalar para 10
        return round(min(severidade_normalizada * 2, 10), 2)

    def __lt__(self, other):
        return self.severidade > other.severidade  # para usar no heap como max-heap

    def __repr__(self):
        return f"[Ocorrência {self.id}] Local: {self.localizacao}, Severidade: {self.severidade}"
