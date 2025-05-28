from collections import defaultdict

class AnalisePreditiva:
    def __init__(self, historico):
        self.historico = historico

    def calcular_risco(self, temperatura, umidade, tipo_vegetacao):
        risco = 0
        # Fatores baseados em regras simples (escalados até 10)
        if temperatura >= 35:
            risco += 3
        elif temperatura >= 28:
            risco += 2
        else:
            risco += 1
        if umidade < 20:
            risco += 3
        elif umidade < 40:
            risco += 2
        elif umidade < 60:
            risco += 1

        vegetacao_fator = {
            "área urbana": 1,
            "pampas": 1,
            "caatinga": 2,
            "cerrado": 2,
            "mata atlântica": 3,
            "amazônia": 3
        }
        risco += vegetacao_fator.get(tipo_vegetacao.lower(), 2)
        return min(risco, 10)  # Cap no máximo em 10

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
            print("✅ Risco BAIXO. Atenção opicional.")
        else:
            print("✅ Risco MÍNIMO. Condições controladas.")
        print("-" * 50)
