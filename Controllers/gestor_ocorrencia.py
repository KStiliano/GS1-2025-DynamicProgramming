class GestorOcorrencias:
    def __init__(self):
        self.historico_ocorrencias = []

    def adicionar_ocorrencia(self, ocorrencia):
        self.historico_ocorrencias.append(ocorrencia)

    def listar_ocorrencias(self):
        return self.historico_ocorrencias

    def filtrar_ocorrencias(self, filtro):
        resultado = []
        for ocorrencia in self.historico_ocorrencias:
            if (
                (not filtro.get("regiao") or ocorrencia.regiao.lower() == filtro["regiao"].lower())
                and (not filtro.get("vegetacao") or ocorrencia.tipo_vegetacao.lower() == filtro["vegetacao"].lower())
                and (not filtro.get("severidade") or ocorrencia.severidade == filtro["severidade"])
                and (not filtro.get("status") or ocorrencia.status.lower() == filtro["status"].lower())
            ):
                resultado.append(ocorrencia)
        return resultado
