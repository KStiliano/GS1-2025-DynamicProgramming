import random
from Models.ocorrencia import Ocorrencia
from Controllers.gestor_ocorrencia import GestorOcorrencias
from Controllers.gestor_drones import GestorDrones
from Controllers.relatorio import GeradorRelatorios
from Utils.estruturas import FilaPrioridadeOcorrencias

gestor = GestorOcorrencias()
gestor_drones = GestorDrones()
historico = gestor.listar_ocorrencias()
gerador_relatorios = GeradorRelatorios(historico)
fila_prioridade = FilaPrioridadeOcorrencias()

def exibir_menu():
    print("\n🚨 Bem-vindo ao IgnisControlSIM 🚨")
    print("1. Inserir ocorrência manualmente")
    print("2. Simular ocorrência aleatória")
    print("3. Listar ocorrências registradas")
    print("4. Atender ocorrência")
    print("5. Gerar relatório de combate")
    print("0. Sair")

def inserir_ocorrencia():
    try:
        id = input("ID da ocorrência: ")
        local = input("Localização: ")
        intensidade = int(input("Intensidade do fogo (1-10): "))
        causa = input("Causa: ")
        observacoes = input("Observações: ")
        vegetacao = input("Vegetação: ")
        temperatura = float(input("Temperatura ambiente (°C): "))
        umidade = float(input("Umidade relativa do ar (%): "))
        vento = input("Intensidade do vento (leve, moderado, forte): ")
        ocorrencia = Ocorrencia(id, local, intensidade, causa, observacoes, vegetacao, temperatura, umidade, vento)
        gestor.adicionar_ocorrencia(ocorrencia)
        fila_prioridade.inserir_ocorrencia(ocorrencia)
        print("✅ Ocorrência registrada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao registrar ocorrência: {e}")

def simular_ocorrencia_aleatoria():
    ocorrencias_prontas = [
        Ocorrencia("1", "Manaus", 8, "Natural", "-", "Amazônia", 42, 15, "forte"),
        Ocorrencia("2", "Campinas", 5, "Humana", "-", "Mata Atlântica", 38, 25, "moderado"),
        Ocorrencia("3", "Cuiabá", 7, "Natural", "-", "Cerrado", 40, 20, "forte"),
        Ocorrencia("4", "Recife", 4, "Desconhecida", "-", "Caatinga", 35, 30, "moderado"),
        Ocorrencia("5", "Porto Alegre", 6, "Humana", "-", "Pampas", 32, 50, "leve")
    ]
    ocorrencia = random.choice(ocorrencias_prontas)
    gestor.adicionar_ocorrencia(ocorrencia)
    fila_prioridade.inserir_ocorrencia(ocorrencia)
    print(f"⚠ Ocorrência simulada em {ocorrencia.localizacao} (Severidade: {ocorrencia.severidade:.2f}/10)")

def listar_ocorrencias():
    ocorrencias = gestor.listar_ocorrencias()
    if not ocorrencias:
        print("📭 Nenhuma ocorrência registrada.")
        return
    for o in ocorrencias:
        print(f"📌 ID: {o.id} | Local: {o.localizacao} | Severidade: {o.severidade:.2f}/10 | Status: {o.status}")

def atender_ocorrencia():
    if fila_prioridade.esta_vazia():
        print("🔕 Nenhuma ocorrência pendente.")
        return

    ocorrencia = fila_prioridade.proxima_ocorrencia()
    msg = gestor_drones.despachar_para_ocorrencia(ocorrencia)
    ocorrencia.status = "Resolvida"
    ocorrencia.tempo_resposta = ocorrencia.severidade  # ou outro cálculo
    print(f"🚁 {msg}")

def gerar_relatorio():
    ocorrencias = gestor.listar_ocorrencias()
    relatorio = gerador_relatorios.gerar_relatorio()

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_ocorrencia()
        elif opcao == "2":
            simular_ocorrencia_aleatoria()
        elif opcao == "3":
            listar_ocorrencias()
        elif opcao == "4":
            atender_ocorrencia()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("👋 Encerrando o sistema IgnisControlSIM.")
            break
        else:
            print("❗ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()