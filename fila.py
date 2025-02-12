import tkinter as tk
from tkinter import messagebox

# Define a estrutura dos elementos
class ElementosDaLista:
    def __init__(self, cor, numero):
        self.cor = cor
        self.numero = numero
        self.proximo = None

    def __lt__(self, compara):
        if self.cor.lower() == 'a' and compara.cor.lower() == 'v':
            return True
        elif self.cor.lower() == 'v' and compara.cor.lower() == 'a':
            return False
        else:
            return self.numero < compara.numero

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def InserirNoInicio(self, nodo):
        if self.head is None or nodo < self.head:
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and nodo > atual.proximo:
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def InserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        atual = self.head
        while atual.proximo is not None:
            atual = atual.proximo
        atual.proximo = nodo

    def Chamar(self):
        if self.head is None:
            return 'Não há pacientes na fila.'
        else:
            paciente_removido = self.head
            self.head = self.head.proximo
            return f'Paciente com cartão {paciente_removido.cor} número {paciente_removido.numero} removido.'

    def ListarPacientes(self):
        pacientes = []
        existe = self.head
        while existe is not None:
            pacientes.append(f'Cartão {existe.cor}, número {existe.numero}')
            existe = existe.proximo
        return pacientes

def verificarNumero(lista, numero):
    existe = lista.head
    while existe is not None:
        if existe.numero == numero:
            return False
        existe = existe.proximo
    return True

# Função para a interface com o tkinter
class InterfaceGrafica:
    def __init__(self, root):
        self.fila = ListaEncadeada()
        self.root = root
        self.root.title("Sistema de Fila de Pacientes")

        # Elementos gráficos
        self.label = tk.Label(root, text="Bem-vindo! RU: 3767463", font=("Arial", 12))
        self.label.pack()

        self.cor_label = tk.Label(root, text="Informe a cor do cartão (A/V):")
        self.cor_label.pack()
        self.cor_entry = tk.Entry(root)
        self.cor_entry.pack()

        self.numero_label = tk.Label(root, text="Informe o número do cartão:")
        self.numero_label.pack()
        self.numero_entry = tk.Entry(root)
        self.numero_entry.pack()

        # Funções para os botões
        self.botao_inserir = tk.Button(root, text="Inserir Paciente", command=self.inserir_paciente)
        self.botao_inserir.pack()

        self.botao_listar = tk.Button(root, text="Mostrar Pacientes", command=self.mostrar_pacientes)
        self.botao_listar.pack()

        self.botao_chamar = tk.Button(root, text="Chamar Paciente", command=self.chamar_paciente)
        self.botao_chamar.pack()

        self.botao_sair = tk.Button(root, text="Sair", command=root.quit)
        self.botao_sair.pack()

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack()

    def inserir_paciente(self):
        cor = self.cor_entry.get().strip()
        try:
            numero = int(self.numero_entry.get().strip())
            if verificarNumero(self.fila, numero):
                if cor.lower() == 'a':
                    self.fila.InserirNoInicio(ElementosDaLista(cor, numero))
                    self.text_output.insert(tk.END, f"Paciente com cartão {cor} e número {numero} inserido.\n")
                elif cor.lower() == 'v':
                    self.fila.InserirNoFinal(ElementosDaLista(cor, numero))
                    self.text_output.insert(tk.END, f"Paciente com cartão {cor} e número {numero} inserido.\n")
                else:
                    messagebox.showerror("Erro", "Cor inválida! Informe 'A' ou 'V'.")
            else:
                messagebox.showerror("Erro", "Número de cartão já existe na fila.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido para o cartão.")

    def mostrar_pacientes(self):
        pacientes = self.fila.ListarPacientes()
        if pacientes:
            self.text_output.delete(1.0, tk.END)
            self.text_output.insert(tk.END, "\n".join(pacientes) + "\n")
        else:
            self.text_output.insert(tk.END, "Não há pacientes na fila.\n")

    def chamar_paciente(self):
        mensagem = self.fila.Chamar()
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, mensagem + "\n")

# Configuração do Tkinter
root = tk.Tk()
interface = InterfaceGrafica(root)
root.mainloop()
