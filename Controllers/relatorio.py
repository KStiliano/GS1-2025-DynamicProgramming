from collections import Counter
from collections import defaultdict

class GeradorRelatorios:
    def __init__(self, historico):
        self.historico = historico

    def gerar_relatorio(self):
        if not self.historico:
            print("⚠️ Nenhuma ocorrência registrada.")
            return
        print("\n📋 RELATÓRIO DE ATENDIMENTO - [NOME DO APP]")
        print("-" * 50)
        total_ocorrencias = len(self.historico)
        tempos_resposta = [tempo for _, _, tempo in self.historico]
        severidades = [oc.severidade for oc, _, _ in self.historico]
        causas = [oc.causa for oc, _, _ in self.historico]
        regioes = [oc.localizacao for oc, _, _ in self.historico]
        tempo_medio = sum(tempos_resposta) / total_ocorrencias
        max_severidade = max(severidades)
        ocorrencia_mais_grave = next((oc for oc, _, _ in self.historico if oc.severidade == max_severidade), None)
        print(f"Total de ocorrências atendidas: {total_ocorrencias}")
        print(f"Tempo médio de resposta: {tempo_medio:.2f} min")
        print(f"Ocorrência mais severa:")
        print(f"  Local: {ocorrencia_mais_grave.localizacao}")
        print(f"  Severidade: {ocorrencia_mais_grave.severidade}")
        print(f"  Causa: {ocorrencia_mais_grave.causa}")
        print(f"  Vegetação: {ocorrencia_mais_grave.tipo_vegetacao}")
        print("\n▶️ Ocorrências por região:")
        for regiao, qtd in Counter(regioes).items():
            print(f"  {regiao}: {qtd}")
        print("\n▶️ Causas registradas:")
        for causa, qtd in Counter(causas).items():
            print(f"  {causa}: {qtd}")
        print("\n▶️ Ocorrências detalhadas:")
        for i, (oc, drone_id, tempo) in enumerate(self.historico, 1):
            print(f"  {i}. Região: {oc.localizacao} | Causa: {oc.causa} | Severidade: {oc.severidade:.2f} | Drone: {drone_id} | Tempo: {tempo} min")
        print("-" * 50)

        def gerar_relatorio_regional(ocorrencias):
            relatorio = defaultdict(lambda: {
                "total": 0,
                "soma_severidade": 0,
                "resolvidas": 0,
                "pendentes": 0,
                "soma_tempo_resposta": 0
            })
            for o in ocorrencias:
                regiao = o.regiao
                relatorio[regiao]["total"] += 1
                relatorio[regiao]["soma_severidade"] += o.severidade
                relatorio[regiao]["soma_tempo_resposta"] += o.tempo_resposta or 0
                if o.status.lower() == "resolvida":
                    relatorio[regiao]["resolvidas"] += 1
                else:
                    relatorio[regiao]["pendentes"] += 1
            print("\n📋 RELATÓRIO REGIONAL DE OCORRÊNCIAS")
            print("=" * 60)
            for regiao, dados in relatorio.items():
                total = dados["total"]
                media_severidade = dados["soma_severidade"] / total
                tempo_medio = dados["soma_tempo_resposta"] / total
                print(f"🗺️ Região: {regiao}")
                print(f"  • Total de Ocorrências: {total}")
                print(f"  • Média de Severidade: {media_severidade:.2f} / 10")
                print(f"  • Resolvidas: {dados['resolvidas']}")
                print(f"  • Pendentes: {dados['pendentes']}")
                print(f"  • Tempo Médio de Resposta: {tempo_medio:.2f} minutos")
                print("-" * 60)
