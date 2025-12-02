Sistema de Gerenciamento de Tarefas

Este projeto implementa um sistema simples de gerenciamento de tarefas em Python, seguindo as regras propostas na atividade.
O objetivo é permitir criar, atualizar, concluir, arquivar e consultar tarefas de maneira organizada, utilizando boas práticas de programação e persistência em JSON.

Funcionalidades do Sistema
Criar Tarefas

Cada tarefa contém:

Título

Descrição

Prioridade (Urgente, Alta, Média ou Baixa)

Status inicial "Pendente"

Origem da tarefa

Data e hora de criação

ID único gerado automaticamente

Selecionar Tarefa por Prioridade

O sistema identifica a tarefa mais urgente disponível e muda seu status para “Fazendo”.

Atualizar Prioridade

Permite alterar a prioridade de uma tarefa já existente, com validação das opções permitidas.

Concluir Tarefas

Ao concluir uma tarefa:

É registrada a data e hora de conclusão

O status é alterado para “Concluída”

O tempo de execução pode ser calculado no relatório

Arquivar Tarefas Antigas

Tarefas concluídas há mais de 7 dias são automaticamente movidas para o arquivo tarefas_arquivadas.json.

Exclusão Lógica

As tarefas não são apagadas fisicamente.
O status é alterado para “Excluída”.

Relatórios

O sistema permite:

Exibir todas as tarefas

Exibir detalhes completos

Calcular tempo de execução das tarefas concluídas

Listar apenas tarefas arquivadas

Persistência de Dados

Os arquivos utilizados pelo sistema são:

tarefas.json

tarefas_arquivadas.json

Ambos são criados automaticamente caso não existam.

Conceitos Aplicados

Funções separadas por responsabilidade

Variáveis globais e locais

Uso de listas e dicionários

ID incremental

Validação de dados

Tratamento de exceções com try/except

Docstrings nas funções

Prints de execução para testes

Modularização do código

Organização do fluxo principal através de menu

Estrutura dos Arquivos
/projeto
│── sistema_tarefas.py
│── tarefas.json
│── tarefas_arquivadas.json
│── README.md

Como Executar

Instale Python 3

Coloque todos os arquivos na mesma pasta

Execute o comando:

python sistema_tarefas.py


Os arquivos JSON serão criados automaticamente na primeira execução.

Autores

João Victor – Aluno de Análise e Desenvolvimento de Sistemas.
Gabriel Rodrigues
Guilherme Virche
