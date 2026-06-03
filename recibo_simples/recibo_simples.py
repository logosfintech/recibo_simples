from tkinter import *
from tkinter import messagebox
import webbrowser
import os


def gerar_recibo():

    if cliente.get().strip() == "":
        messagebox.showerror("Erro", "Informe o nome do cliente.")
        return

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">

        <title>Recibo de Prestação de Serviços</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 40px;
                border: 1px solid #000;
                line-height: 1.8;
            }}

            h1 {{
                text-align: center;
                margin-bottom: 40px;
            }}

            .assinatura {{
                margin-top: 80px;
                text-align: center;
            }}

        </style>

    </head>

    <body>

        <h1>RECIBO DE PRESTAÇÃO DE SERVIÇOS</h1>

        <p>
            Recebi de <strong>{cliente.get()}</strong>,
            inscrito(a) no CPF nº <strong>{cpf_cliente.get()}</strong>,
            a importância de <strong>R$ {valor.get()}</strong>,
            referente aos serviços de
            <strong>{servico.get()}</strong>.
        </p>

        <p>
            Por ser verdade, firmo o presente recibo para dar plena e geral
            quitação do valor recebido.
        </p>

        <br><br>

        <p>
            {cidade.get()}, {data_assinatura.get()}
        </p>

        <div class="assinatura">

            ___________________________________________
            <br><br>

            <strong>Rayane Rafaelli Terres</strong><br>

            CPF: 027.276.130-32<br>

            Telefone: (51) 9 9640-9899

        </div>

    </body>
    </html>
    """

    nome_arquivo = f"Recibo_{cliente.get().replace(' ', '_')}.html"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    webbrowser.open(
        "file://" + os.path.realpath(nome_arquivo)
    )

    messagebox.showinfo(
        "Sucesso",
        "Recibo gerado!\n\nNo navegador pressione CTRL + P e escolha 'Salvar como PDF'."
    )


# JANELA

janela = Tk()
janela.title("Gerador de Recibos")
janela.geometry("700x550")


Label(
    janela,
    text="GERADOR DE RECIBO",
    font=("Arial", 16, "bold")
).pack(pady=15)


# CAMPOS

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
    ).pack(anchor="w", padx=15)

    globals()[nome] = Entry(
        janela,
        width=80
    )

    globals()[nome].pack(
        padx=15,
        pady=3
    )


# TIPO DE SERVIÇO

Label(
    janela,
    text="Tipo de Serviço",
    font=("Arial", 10, "bold")
).pack(anchor="w", padx=15, pady=(15, 5))


servico = StringVar()
servico.set("Personal Trainer")


Radiobutton(
    janela,
    text="Personal Trainer",
    variable=servico,
    value="Personal Trainer"
).pack(anchor="w", padx=30)


Radiobutton(
    janela,
    text="Massagista",
    variable=servico,
    value="Massagista"
).pack(anchor="w", padx=30)


# BOTÃO

Button(
    janela,
    text="GERAR RECIBO",
    command=gerar_recibo,
    font=("Arial", 12, "bold"),
    height=2,
    width=20
).pack(pady=25)


janela.mainloop()
