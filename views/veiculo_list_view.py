import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from tkinter import ttk
from model.veiculo import VeiculoFactory, Categoria

veiculos = []

def atualizar_lista():
    listbox.delete(0, tk.END)
    for v in veiculos:
        listbox.insert(tk.END, f"{v.placa} - {v.categoria.value}")


def ver_info():
    try:
        indice = listbox.curselection()[0]
        v = veiculos[indice]

        info = v.exibir_dados()
        messagebox.showinfo("Informações do Veículo", info)

    except:
        messagebox.showerror("Erro", "Selecione um veículo!")


def remover():
    try:
        indice = listbox.curselection()[0]
        veiculos.pop(indice)
        atualizar_lista()
    except:
        messagebox.showerror("Erro", "Selecione um veículo!")

# TELA DE CADASTRO

def abrir_cadastro():
    janela2 = tk.Toplevel(janela)
    janela2.title("Novo Veículo")
    janela2.geometry("300x300")

    Label(janela2, text="Placa").pack()
    ent_placa = Entry(janela2)
    ent_placa.pack()

    Label(janela2, text="Tipo").pack()
    combo_tipo = ttk.Combobox(janela2, values=["carro", "motorhome"])
    combo_tipo.pack()

    Label(janela2, text="Categoria").pack()
    combo_cat = ttk.Combobox(janela2, values=["ECONOMICO", "EXECUTIVO"])
    combo_cat.pack()

    Label(janela2, text="Taxa diária").pack()
    ent_taxa = Entry(janela2)
    ent_taxa.pack()

    def salvar():
        placa = ent_placa.get()
        tipo = combo_tipo.get()
        categoria = combo_cat.get()
        taxa = ent_taxa.get()

        # Validação simples
        if not (placa and tipo and categoria and taxa):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            taxa = float(taxa)

            cat_enum = Categoria[categoria]

            veiculo = VeiculoFactory.criar_veiculo(
                tipo, placa, cat_enum, taxa
            )

            veiculos.append(veiculo)

            atualizar_lista()
            janela2.destroy()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    Button(janela2, text="Salvar", command=salvar).pack(pady=10)

# TELA PRINCIPAL

janela = tk.Tk()
janela.title("Veículos Cadastrados")
janela.geometry("400x400")

Label(janela, text="Lista de Veículos", pady=10).pack()

listbox = tk.Listbox(janela)
listbox.pack(fill=tk.BOTH, expand=True)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

Button(frame_botoes, text="Novo", command=abrir_cadastro).pack(side=tk.LEFT, padx=5)
Button(frame_botoes, text="Ver Informações", command=ver_info).pack(side=tk.LEFT, padx=5)
Button(frame_botoes, text="Remover", command=remover).pack(side=tk.LEFT, padx=5)

janela.mainloop()