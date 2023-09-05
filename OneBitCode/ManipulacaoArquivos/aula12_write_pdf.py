# Projeto Prático I - Gerando Recibo em PDF
# Biblioteca fpdf (pip install fpdf)

from fpdf import FPDF

# 1) Instanciar PDF
pdf = FPDF()

# 2) Adicionar uma page (precisa de uma célula, passo 4)
pdf.add_page()

# 3) Definir a fonte, coordenadas de altura e largura para texto:
pdf.set_font('Arial', 'B', 16)

# 4) Definir cell
pdf.cell(40, 10, 'Hello world!')

# 4) Definir diretório de output
pdf.output('ArquivosAulas/aula11_arquivo_exemplo.pdf')