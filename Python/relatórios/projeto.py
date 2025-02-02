import PyPDF2
import os

merger= PyPDF2.PdfMerger()

lista_relatórios= os.listdir("relatórios")
lista_relatórios.sort()
print(lista_relatórios)

for relatórios in lista_relatórios:
    if ".pdf" in relatórios:
        merger.append(f"relatórios/{relatórios}")

        merger.write("PDF relatóriosfinais.pdf")