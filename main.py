import random
from Models.ocorrencia import Ocorrencia
from Controllers.gestor_ocorrencia import GestorOcorrencias
from Controllers.gestor_drones import GestorDrones
from Controllers.relatorio import GeradorRelatorios
from Controllers.analise import AnalisePreditiva
from Utils.estruturas import FilaPrioridadeOcorrencias

# Instâncias principais
gestor = GestorOcorrencias()
gestor_drones = GestorDrones()
historico = gestor_drones.listar_historico()
gerador_relatorios = GeradorRelatorios(historico)
fila_prioridade = FilaPrioridadeOcorrencias()
analise = AnalisePreditiva(historico)

def exibir_menu():
    print("\n🚨 Bem-vindo ao IgnisControlSIM 🚨")
    print("1. Inserir ocorrência manualmente")
    print("2. Simular ocorrência aleatória")
    print("3. Listar ocorrências registradas")
    print("4. Filtrar ocorrências")
    print("5. Atender ocorrência")
    print("6. Gerar relatório de combate")
    print("7. Análise preditiva de risco")
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
        print(f"📌 ID: {o.id} | Local: {o.localizacao} | Severidade: {o.severidade:.2f} | Status: {o.status}")

def atender_ocorrencia():
    if fila_prioridade.esta_vazia():
        print("🚫 Nenhuma ocorrência na fila de prioridade.")
        return
    ocorrencia = fila_prioridade.proxima_ocorrencia()
    resposta = gestor_drones.despachar_para_ocorrencia(ocorrencia)
    ocorrencia.status = "Em andamento"
    print(resposta)

def gerar_relatorio():
    gerador_relatorios.gerar_relatorio()

def executar_analise():
    try:
        temperatura = float(input("Temperatura (°C): "))
        umidade = float(input("Umidade (%): "))
        tipo_vegetacao = input("Tipo de vegetação: ")
        analise.gerar_relatorio_de_risco(temperatura, umidade, tipo_vegetacao)
    except Exception as e:
        print(f"❌ Erro na análise preditiva: {e}")

def filtrar_ocorrencias():
    print("\n🔍 Filtro de Ocorrências")
    vegetacao = input("Filtrar por vegetação (ou pressione Enter para ignorar): ")
    severidade = input("Filtrar por severidade exata (ou pressione Enter para ignorar): ")
    status = input("Filtrar por status (ou pressione Enter para ignorar): ")

    try:
        severidade = float(severidade) if severidade else None
    except:
        print("❌ Severidade inválida. Ignorando filtro.")
        severidade = None
    filtro = {
        "vegetacao": vegetacao if vegetacao else None,
        "severidade": severidade,
        "status": status if status else None
    }
    resultados = gestor.filtrar_ocorrencias(filtro)
    if not resultados:
        print("⚠️ Nenhuma ocorrência encontrada com os critérios informados.")
    else:
        print(f"\n📌 {len(resultados)} ocorrência(s) encontrada(s):")
        for o in resultados:
            print(f"ID: {o.id} | Local: {o.localizacao} | Vegetação: {o.vegetacao} | Severidade: {o.severidade} | Status: {o.status}")

def main():
    while True:
        exibir_menu()
        escolha = input("\nEscolha uma opção: ")
        if escolha == "1":
            inserir_ocorrencia()
        elif escolha == "2":
            simular_ocorrencia_aleatoria()
        elif escolha == "3":
            listar_ocorrencias()
        elif escolha == "4":
            filtrar_ocorrencias()
        elif escolha == "5":
            atender_ocorrencia()
        elif escolha == "6":
            gerar_relatorio()
        elif escolha == "7":
            executar_analise()
        elif escolha == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()