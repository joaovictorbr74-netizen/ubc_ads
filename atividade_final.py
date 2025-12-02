# =============================================================
# PROJETO: Calculadora em Python
#integrantes :
#Davi Henrique Viana da Silva 43494633
#Gabriel Rodrigues Da Silva 41780841
#Guilherme Virche Dos Santos 42574773
#João Victor Nogueira Galvão 42721482
# =============================================================

import json
import os
from datetime import datetime, timedelta

# ============================
# VARIÁVEIS GLOBAIS
# ============================

tarefas = []
tarefas_arquivadas = []
proximo_id = 1  # será atualizado ao carregar o arquivo


# ============================
# FUNÇÕES DE ARQUIVOS
# ============================

def verificar_arquivos():
    """Verifica se os arquivos JSON existem; caso contrário, cria automaticamente."""
    print("Executando a função verificar_arquivos")

    arquivos = ["tarefas.json", "tarefas_arquivadas.json"]

    for arquivo in arquivos:
        if not os.path.exists(arquivo):
            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)


def carregar_arquivos():
    """Carrega os dados dos arquivos JSON para as variáveis globais."""
    print("Executando a função carregar_arquivos")
    global tarefas, tarefas_arquivadas, proximo_id

    with open("tarefas.json", "r", encoding="utf-8") as f:
        tarefas = json.load(f)

    with open("tarefas_arquivadas.json", "r", encoding="utf-8") as f:
        tarefas_arquivadas = json.load(f)

    # Atualiza próximo ID
    if tarefas:
        maior_id = max(t["id"] for t in tarefas)
        proximo_id = maior_id + 1


def salvar_arquivos():
    """Salva as listas de tarefas e arquivadas nos arquivos JSON."""
    print("Executando a função salvar_arquivos")

    with open("tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)

    with open("tarefas_arquivadas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas_arquivadas, f, ensure_ascii=False, indent=4)


# ============================
# FUNÇÕES DE VALIDAÇÃO
# ============================

def validar_opcao(msg, opcoes):
    """Valida entrada de opções restringidas."""
    print("Executando a função validar_opcao")

    while True:
        entrada = input(msg).strip().lower()
        if entrada in opcoes:
            return entrada
        print("Opção inválida. Tente novamente.")


# ============================
# FUNÇÕES PRINCIPAIS
# ============================

def criar_tarefa():
    """
    Cria uma nova tarefa solicitando informações ao usuário,
    valida os dados e adiciona à lista global.
    """
    print("Executando a função criar_tarefa")
    global proximo_id, tarefas

    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")

    prioridade = validar_opcao(
        "Prioridade (urgente, alta, media, baixa): ",
        ["urgente", "alta", "media", "baixa"]
    )

    origem = validar_opcao(
        "Origem (email, telefone, chamado): ",
        ["email", "telefone", "chamado"]
    )

    nova_tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "pendente",
        "origem": origem,
        "criada_em": datetime.now().isoformat(),
        "concluida_em": None
    }

    tarefas.append(nova_tarefa)
    print(f"Tarefa criada com sucesso! ID: {proximo_id}")
    proximo_id += 1


def verificar_urgencia():
    """
    Seleciona a tarefa mais urgente disponível e coloca seu status como 'Fazendo'.
    """
    print("Executando a função verificar_urgencia")
    global tarefas

    prioridades = ["urgente", "alta", "media", "baixa"]

    for p in prioridades:
        candidatos = [t for t in tarefas if t["status"] == "pendente" and t["prioridade"] == p]
        if candidatos:
            tarefa = candidatos[0]
            tarefa["status"] = "fazendo"
            print(f"Tarefa selecionada: {tarefa['titulo']} (ID {tarefa['id']})")
            return

    print("Nenhuma tarefa disponível.")


def atualizar_prioridade():
    """
    Altera a prioridade de uma tarefa existente.
    """
    print("Executando a função atualizar_prioridade")

    try:
        id_tarefa = int(input("Informe o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            nova_prioridade = validar_opcao(
                "Nova prioridade (urgente, alta, media, baixa): ",
                ["urgente", "alta", "media", "baixa"]
            )
            tarefa["prioridade"] = nova_prioridade
            print("Prioridade atualizada com sucesso!")
            return

    print("Tarefa não encontrada.")


def concluir_tarefa():
    """
    Finaliza uma tarefa e registra a data de conclusão.
    """
    print("Executando a função concluir_tarefa")

    try:
        id_tarefa = int(input("Informe o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "concluída"
            tarefa["concluida_em"] = datetime.now().isoformat()
            print("Tarefa concluída!")
            return

    print("Tarefa não encontrada.")


def arquivar_antigas():
    """
    Arquiva automaticamente tarefas concluídas há mais de 7 dias.
    """
    print("Executando a função arquivar_antigas")
    global tarefas, tarefas_arquivadas

    agora = datetime.now()
    novas_ativas = []

    for tarefa in tarefas:
        if tarefa["status"] == "concluída" and tarefa["concluida_em"]:
            concluida = datetime.fromisoformat(tarefa["concluida_em"])
            if agora - concluida > timedelta(days=7):
                tarefa["status"] = "arquivado"
                tarefas_arquivadas.append(tarefa)
                continue

        novas_ativas.append(tarefa)

    tarefas = novas_ativas


def excluir_tarefa():
    """
    Realiza exclusão lógica de uma tarefa (status = 'excluída').
    """
    print("Executando a função excluir_tarefa")

    try:
        id_tarefa = int(input("Informe o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "excluída"
            print("Tarefa excluída logicamente.")
            return

    print("Tarefa não encontrada.")


def relatorio():
    """Exibe todas as informações das tarefas."""
    print("Executando a função relatorio")

    for t in tarefas:
        print("\n---------------------")
        print(f"ID: {t['id']}")
        print(f"Título: {t['titulo']}")
        print(f"Status:

