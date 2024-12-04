import os
from PyPDF2 import PdfMerger

def merge_pdfs_from_folder(folder_path, output_file):
    # Crear un objeto PdfMerger
    merger = PdfMerger()

    try:
        # Obtener todos los archivos PDF de la carpeta y ordenarlos
        pdf_files = sorted([os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')])

        if not pdf_files:
            print("No se encontraron archivos PDF en la carpeta.")
            return

        print(f"Archivos encontrados: {pdf_files}")

        # Agregar cada archivo PDF al merger
        for pdf in pdf_files:
            merger.append(pdf)

        # Guardar el PDF combinado en el archivo de salida
        merger.write(output_file)
        print(f"Archivos combinados con éxito en '{output_file}'")
    except Exception as e:
        print(f"Error al combinar PDFs: {e}")
    finally:
        merger.close()

# Ruta de la carpeta que contiene los PDFs
folder_path = "Podcast Business English"  # Cambia esto por la ruta de tu carpeta

# Nombre del archivo combinado
output_pdf = "podcast_part1.pdf"

# Combinar los PDFs desde la carpeta
merge_pdfs_from_folder(folder_path, output_pdf)
