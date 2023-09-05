# Projeto Prático II - Gerando Recibo em PDF
from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variáveis

cliente = str(input("Informe o NOME do cliente: "))
consulta = str(input("Informe o TIPO DE CONSULTA: ")).capitalize()
valor = str(input("Informe o VALOR recebido: "))
valor_msg = f"{valor} reais"
valor_extenso = num2words(float(valor), lang='pt-br')
valor_extenso_msg = f"{valor_extenso} reais"
dia = date.today().day
mes = date.today().month
ano = date.today().year


# 2 - Layout de recibo
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("ArquivosAulas/rec.jpg", x=0, y=0)
pdf.text(162, 45, valor_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, valor_extenso_msg)
pdf.text(80, 135, consulta)
pdf.set_text_color(255,255,255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))
nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}.pdf"
pdf.output(f"ArquivosAulas/{nome_arquivo}")
print("Recibo gerado com sucesso!")