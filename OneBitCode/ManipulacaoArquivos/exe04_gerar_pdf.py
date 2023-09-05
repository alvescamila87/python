from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', 'B', 16)
pdf.cell(40,10, "PDF Generator: ")
pdf.cell(100,150, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
pdf.output("ArquivosAulas/exe11_arquivo_exemplo2.pdf")