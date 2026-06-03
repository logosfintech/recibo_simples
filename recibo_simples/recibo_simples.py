from tkinter import *
from tkinter import messagebox
import webbrowser
import os


def gerar_recibo():

    if not cliente.get().strip():
        messagebox.showerror(
            "Erro",
            "Informe o nome do cliente."
        )
        return

    try:

        # Pasta onde está o arquivo main.py
        pasta_atual = os.path.dirname(
            os.path.abspath(__file__)
        )

        # Caminho completo do template
        caminho_template = os.path.join(
            pasta_atual,
            "index.html"
        )

        with open(
            caminho_template,
            "r",
            encoding="utf-8"
        ) as arquivo:

            template = arquivo.read()

        html = template.format(
            cliente=cliente.get(),
            cpf_cliente=cpf_cliente.get(),
            valor=valor.get(),
            servico=servico.get(),
            cidade=cidade.get(),
            data_assinatura=data_assinatura.get()
        )

        nome_arquivo = "recibo.html"

        caminho_recibo = os.path.join(
            pasta_atual,
            nome_arquivo
        )

        with open(
            caminho_recibo,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(html)

        webbrowser.open(
            "file://" + os.path.realpath(caminho_recibo)
        )

        messagebox.showinfo(
            "Sucesso",
            "Recibo gerado com sucesso!\n\nPressione CTRL + P no navegador para salvar em PDF."
        )

    except FileNotFoundError:

        messagebox.showerror(
            "Erro",
            "O arquivo index.html não foi encontrado."
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            f"Ocorreu um erro:\n\n{erro}"
        )


# ==========================
# JANELA
# ==========================

janela = Tk()
janela.title("Gerador de Recibo")
janela.geometry("700x550")
janela.resizable(False, False)

Label(
    janela,
    text="GERADOR DE RECIBO",
    font=("Arial", 16, "bold")
).pack(pady=15)

# ==========================
# CAMPOS
# ==========================

campos = [
    ("Nome do Cliente", "cliente"),
    ("CPF do Cliente", "cpf_cliente"),
    ("Valor (R$)", "valor"),
    ("Cidade", "cidade"),
    ("Data da Assinatura", "data_assinatura")
]

for texto, nome in campos:

    Label(
        janela,
        text=texto
    ).pack(
        anchor="w",
        padx=15
    )

    globals()[nome] = Entry(
        janela,
        width=80
    )

    globals()[nome].pack(
        padx=15,
        pady=3
    )

# ==========================
# TIPO DE SERVIÇO
# ==========================

Label(
    janela,
    text="Tipo de Serviço",
    font=("Arial", 10, "bold")
).pack(
    anchor="w",
    padx=15,
    pady=(15, 5)
)

servico = StringVar()
servico.set("Personal Trainer")

Radiobutton(
    janela,
    text="Personal Trainer",
    variable=servico,
    value="Personal Trainer"
).pack(
    anchor="w",
    padx=30
)

Radiobutton(
    janela,
    text="Massagista",
    variable=servico,
    value="Massagista"
).pack(
    anchor="w",
    padx=30
)

# ==========================
# BOTÃO
# ==========================

Button(
    janela,
    text="GERAR RECIBO",
    command=gerar_recibo,
    font=("Arial", 12, "bold"),
    width=20,
    height=2
).pack(
    pady=25
)

janela.mainloop()