from collections import Counter

class GeradorRelatorios:
    def __init__(self, historico):
        self.historico = historico

    def gerar_relatorio(self):
        if not self.historico:
            print("⚠️ Nenhuma ocorrência registrada.")
            return
        print("\n📋 RELATÓRIO DE ATENDIMENTO - IgnisControlSIM")
        print("-" * 50)
        total_ocorrencias = len(self.historico)
        tempos_resposta = [oc.tempo_resposta for oc in self.historico]
        severidades = [oc.severidade for oc in self.historico]
        causas = [oc.causa for oc in self.historico]
        regioes = [oc.localizacao for oc in self.historico]
        tempo_medio = sum(tempos_resposta) / total_ocorrencias
        max_severidade = max(severidades)
        ocorrencia_mais_grave = next((oc for oc in self.historico if oc.severidade == max_severidade), None)
        print(f"Total de ocorrências atendidas: {total_ocorrencias}")
        print(f"Tempo médio de resposta: {tempo_medio:.2f} min")
        print(f"Ocorrência mais severa:")
        print(f"  Local: {ocorrencia_mais_grave.localizacao}")
        print(f"  Severidade: {ocorrencia_mais_grave.severidade}")
        print(f"  Causa: {ocorrencia_mais_grave.causa}")
        print(f"  Vegetação: {ocorrencia_mais_grave.vegetacao}")
        print("\n▶️ Ocorrências por região:")
        for regiao, qtd in Counter(regioes).items():
            print(f"  {regiao}: {qtd}")
        print("\n▶️ Causas registradas:")
        for causa, qtd in Counter(causas).items():
            print(f"  {causa}: {qtd}")
        print("\n▶️ Ocorrências detalhadas:")
        for i, oc in enumerate(self.historico, 1):
            print(f"  {i}. Região: {oc.localizacao} | Causa: {oc.causa} | Severidade: {oc.severidade:.2f} | Tempo: {oc.tempo_resposta} min")
        print("-" * 50)
