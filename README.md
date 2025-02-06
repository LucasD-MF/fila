# Sistema de Fila com Prioridade em Python

## Descrição
Este é um aplicativo simples desenvolvido em Python que implementa um sistema de fila com prioridade utilizando a estrutura de dados de **Lista Encadeada**. O sistema permite inserir pacientes na fila com base na prioridade de seu cartão (A ou V), onde:
- **A** representa alta prioridade.
- **V** representa baixa prioridade.

Além disso, o sistema possui uma interface gráfica feita com o **Tkinter**, proporcionando uma interação simples para gerenciar os pacientes da fila.

## Funcionalidades

- **Inserção de Pacientes**: Permite inserir pacientes na fila com base na cor do cartão (A ou V) e número.
- **Listagem de Pacientes**: Exibe todos os pacientes na fila, ordenados por prioridade e número.
- **Chamar Paciente**: Remove o paciente da frente da fila, com base na prioridade.
- **Interface Gráfica**: Feita com Tkinter, fácil de usar e interativa.

## Requisitos

- Python 3.x
- Tkinter (geralmente já vem instalado com o Python)
- **Nenhuma biblioteca externa necessária**

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/LucasD-MF/fila.git

## Navegue até o diretório do projeto:

cd fila

## Execute o script Python:

python fila.py

## Como Funciona a Fila
Pacientes com cartão A (alta prioridade) são inseridos no início da fila.
Pacientes com cartão V (baixa prioridade) são inseridos no final da fila.
A prioridade sempre será respeitada, com pacientes de cartão A sendo chamados primeiro.

Desenvolvido por Lucas de Moura Francisco.
