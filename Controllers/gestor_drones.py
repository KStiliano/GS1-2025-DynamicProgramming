from Models.drone import Drone

class GestorDrones:
    def __init__(self, num_drones=3):
        self.drones = [Drone(i + 1, f"Base_{i+1}") for i in range(num_drones)]
        self.historico = []

    def despachar_para_ocorrencia(self, ocorrencia):
        drone_disponivel = next((d for d in self.drones if d.ocorrencia_atual is None), None)
        if drone_disponivel:
            msg = drone_disponivel.despachar_para(ocorrencia)
            ocorrencia.tempo_resposta = drone_disponivel.tempo_resposta
            self.historico.append(ocorrencia)
            return msg
        else:
            return "Nenhum drone disponível no momento."

    def encerrar_ocorrencias(self):
        resultados = []
        for drone in self.drones:
            if drone.ocorrencia_atual:
                resultados.append(drone.concluir_missao())
        return resultados

    def listar_historico(self):
        return self.historico
