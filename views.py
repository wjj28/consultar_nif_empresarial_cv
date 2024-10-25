from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)


# Lendo os dados do arquivo Excel
def load_empresas():
    empresas = []
    excel_file = "company.xlsx"  # Ajuste o caminho se necessário

    # Lê todas as planilhas do arquivo
    xls = pd.ExcelFile(excel_file)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        for _, row in df.iterrows():
            nif = str(row['NIF'])  # Garantir que o NIF é uma string
            empresas.append({
                "nif": nif,
                "nome": row['Nome'],
                "tipo_contribuinte": row['Tipo Contribuinte'],
                "estado": row['Estado'],
            })

    return empresas


# Carregar dados uma vez ao iniciar o aplicativo
empresas = load_empresas()


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/consulta", methods=["POST"])
def consulta():
    nif = request.form.get("nif")
    nome = request.form.get("nome")
    pagina = int(request.form.get("pagina", 1))
    limite = 15  # Número de resultados por página
    inicio = (pagina - 1) * limite
    fim = inicio + limite

    if nif:
        empresa = next((empresa for empresa in empresas if empresa['nif'] == nif), None)
        if empresa:
            return jsonify(resultado=f"Resultado da consulta: {empresa['nome']} (NIF: {nif})", total=1)
        else:
            return jsonify(resultado="NIF não encontrado.", total=0)

    if nome:
        resultado = [empresa for empresa in empresas if nome.lower() in empresa['nome'].lower()]

        total_resultados = len(resultado)

        if total_resultados > 0:
            resultados_pagina = resultado[inicio:fim]
            resposta = f"<div class='resultado-header'>Encontradas {total_resultados} empresas:</div>" + "<br>".join(
                f"{empresa['nome']} (NIF: {empresa['nif']})" for empresa in resultados_pagina)

            buttons = ""
            if pagina > 1:
                buttons += f"<button onclick='mostrarMais({pagina - 1})'>Anterior</button> "
            if total_resultados > fim:
                buttons += f"<button onclick='mostrarMais({pagina + 1})'>Próximo</button>"

            return jsonify(resultado=resposta + "<br>" + buttons, total=total_resultados)


        else:
            return jsonify(resultado="Nome da empresa não encontrado.", total=0)

    return jsonify(resultado="Por favor, insira um NIF ou nome da empresa.", total=0)


if __name__ == "__main__":
    app.run(debug=True)
