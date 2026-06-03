from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

FORM_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Recibo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 700px;
            margin: 40px auto;
            padding: 20px;
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
        }
        input[type=text] {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            box-sizing: border-box;
        }
        button {
            margin-top: 25px;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .error {
            color: #a00;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>GERADOR DE RECIBO</h1>
    {% if erro %}
        <div class="error">{{ erro }}</div>
    {% endif %}
    <form method="post" action="/gerar">
        <label for="cliente">Nome do Cliente</label>
        <input type="text" id="cliente" name="cliente" value="{{ cliente|default('') }}" required>

        <label for="cpf_cliente">CPF do Cliente</label>
        <input type="text" id="cpf_cliente" name="cpf_cliente" value="{{ cpf_cliente|default('') }}">

        <label for="valor">Valor (R$)</label>
        <input type="text" id="valor" name="valor" value="{{ valor|default('') }}">

        <label for="servico">Tipo de Serviço</label>
        <input type="text" id="servico" name="servico" value="{{ servico|default('Personal Trainer') }}">

        <label for="cidade">Cidade</label>
        <input type="text" id="cidade" name="cidade" value="{{ cidade|default('') }}">

        <label for="data_assinatura">Data da Assinatura</label>
        <input type="text" id="data_assinatura" name="data_assinatura" value="{{ data_assinatura|default('') }}">

        <button type="submit">GERAR RECIBO</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(FORM_HTML, erro=None)


@app.route("/gerar", methods=["POST"])
def gerar_recibo():
    cliente = request.form.get("cliente", "").strip()
    cpf_cliente = request.form.get("cpf_cliente", "").strip()
    valor = request.form.get("valor", "").strip()
    servico = request.form.get("servico", "").strip() or "Personal Trainer"
    cidade = request.form.get("cidade", "").strip()
    data_assinatura = request.form.get("data_assinatura", "").strip()

    if not cliente:
        return render_template_string(
            FORM_HTML,
            erro="Informe o nome do cliente.",
            cliente=cliente,
            cpf_cliente=cpf_cliente,
            valor=valor,
            servico=servico,
            cidade=cidade,
            data_assinatura=data_assinatura
        )

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_template = os.path.join(pasta_atual, "index.html")

    try:
        with open(caminho_template, "r", encoding="utf-8") as arquivo:
            template = arquivo.read()

        html = template.format(
            cliente=cliente,
            cpf_cliente=cpf_cliente,
            valor=valor,
            servico=servico,
            cidade=cidade,
            data_assinatura=data_assinatura
        )

        return html

    except FileNotFoundError:
        return render_template_string(
            FORM_HTML,
            erro="O arquivo index.html não foi encontrado.",
            cliente=cliente,
            cpf_cliente=cpf_cliente,
            valor=valor,
            servico=servico,
            cidade=cidade,
            data_assinatura=data_assinatura
        )
    except Exception as erro:
        return render_template_string(
            FORM_HTML,
            erro=f"Ocorreu um erro: {erro}",
            cliente=cliente,
            cpf_cliente=cpf_cliente,
            valor=valor,
            servico=servico,
            cidade=cidade,
            data_assinatura=data_assinatura
        )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
