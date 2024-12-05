import os
import argparse
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# === Funcion para unir todos los pdf de una carpeta ===
def merge_pdfs_from_folder(folder_path, output_file):
    """Combina todos los PDFs de una carpeta en un único archivo."""
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

# === Funcion para unir paginas seleccionadas de un pdf  ===
def merge_selected_pages(input_pdf, page_list, output_pdf):
    """Crea un nuevo PDF combinando solo las páginas especificadas de un archivo."""
    try:
        reader = PdfReader(input_pdf)
        writer = PdfWriter()

        # Validar páginas y agregarlas al nuevo PDF
        for page_num in page_list:
            if page_num - 1 < 0 or page_num - 1 >= len(reader.pages):
                print(f"Página {page_num} está fuera de rango. Se omitirá.")
            else:
                writer.add_page(reader.pages[page_num - 1])

        # Escribir el archivo de salida
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Nuevo PDF creado exitosamente: {output_pdf}")

    except Exception as e:
        print(f"Error al procesar el PDF: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combina o selecciona páginas de PDFs desde la línea de comandos.")
    
    subparsers = parser.add_subparsers(dest="command", help="Subcomandos disponibles")

    # Subcomando para combinar PDFs desde una carpeta
    combine = subparsers.add_parser("combine", help="Combina todos los PDFs de una carpeta.")
    combine.add_argument("folder_path", help="Ruta de la carpeta que contiene los PDFs.")
    combine.add_argument("output_pdf", help="Ruta del archivo PDF combinado de salida.")

    # Subcomando para combinar páginas seleccionadas
    select = subparsers.add_parser("select", help="Combina páginas específicas de un PDF.")
    select.add_argument("input_pdf", help="Ruta del archivo PDF de entrada.")
    select.add_argument("page_list", help="Lista de páginas a combinar, separadas por comas. Ejemplo: 1,3,5.")
    select.add_argument("output_pdf", help="Ruta del archivo PDF de salida.")

    args = parser.parse_args()

    if args.command == "combine":
        merge_pdfs_from_folder(args.folder_path, args.output_pdf)

    elif args.command == "select":
        page_list = list(map(int, args.page_list.split(",")))
        print(page_list)
        merge_selected_pages(args.input_pdf, page_list, args.output_pdf)
        
    else:
        parser.print_help()
