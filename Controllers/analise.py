class AnalisePreditiva:
    def __init__(self, historico):
        self.historico = historico
        self.cache = {}

    def calcular_risco(self, temperatura, umidade, tipo_vegetacao):
        chave = (round(temperatura, 1), round(umidade, 1), tipo_vegetacao.lower())
        if chave in self.cache:
            return self.cache[chave]

        def risco_rec(temperatura, umidade, vegetacao):
            if temperatura < 28:
                risco_temp = 1
            elif temperatura < 35:
                risco_temp = 2
            else:
                risco_temp = 3
            if umidade < 25:
                risco_umid = 3
            elif umidade < 40:
                risco_umid = 2
            elif umidade < 60:
                risco_umid = 1
            else:
                risco_umid = 0
                
            vegetacao_fator = {
                "área urbana": 1,
                "pampas": 1,
                "caatinga": 2,
                "cerrado": 2,
                "mata atlântica": 3,
                "amazônia": 3
            }
            
            risco_veg = vegetacao_fator.get(vegetacao, 2)
            total = risco_temp + risco_umid + risco_veg
            return min(total, 10)
        resultado = risco_rec(temperatura, umidade, tipo_vegetacao.lower())
        self.cache[chave] = resultado
        return resultado

    def gerar_relatorio_de_risco(self, temperatura, umidade, tipo_vegetacao):
        risco = self.calcular_risco(temperatura, umidade, tipo_vegetacao)
        print("\n🔎 ANÁLISE PREDITIVA DE RISCO DE QUEIMADA")
        print("-" * 50)
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Tipo de Vegetação: {tipo_vegetacao.capitalize()}")
        print(f"\n→ Grau estimado de risco de queimada: {risco}/10")
        if risco >= 9:
            print("⚠️⚠️⚠️ Risco ALTÍSSIMO! Medidas urgentes são recomendadas.")
        elif risco >= 7:
            print("⚠️⚠️ Risco ALTO. Monitoramento constante necessário.")
        elif risco >= 4:
            print("⚠️ Risco MODERADO. Atenção recomendada.")
        elif risco >= 2:
            print("✅ Risco BAIXO. Atenção opcional.")
        else:
            print("✅ Risco MÍNIMO. Condições controladas.")
        print("-" * 50)
