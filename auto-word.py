import os
import re
import win32com.client

# === Funcion para extraer numero del nombre de un archivo ===
def extract_number(file_name):
    """
    Extrae el número de un nombre de archivo basado en un patrón.
    """
    match = re.search(r'_(\d+)', file_name)  # Busca un número después de "_"
    return int(match.group(1)) if match else float('inf')  # Si no encuentra un número, devuelve infinito.

# === Funcion para combinar tablas de archivos word en un archivo final ===
def combine_tables(folder_path, output_file="Documento_Combinado_final", output_format="word"):
    """
    Combina tablas de múltiples documentos Word en un único archivo Word o PDF.

    Args:
        folder_path (str): Ruta donde se encuentran los documentos Word.
        output_file (str): Nombre del archivo de salida sin extensión.
        output_format (str): Formato de salida, "word" o "pdf".
    """
    # Crear instancia de Word
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False  # Hacer Word invisible

    try:
        # Crear un nuevo documento
        output_document = word.Documents.Add()

        # Obtener y ordenar archivos Word por número extraído
        docx_files = [file for file in os.listdir(folder_path) if file.endswith(".docx")]
        docx_files = sorted(docx_files, key=extract_number)  # Ordenar por el número extraído

        # Combinar hasta un máximo de 800 documentos
        num_docs_to_combine = min(800, len(docx_files))
        print(f"Número de documentos a combinar: {num_docs_to_combine}")

        # Iterar sobre los documentos y copiar tablas
        for file_name in docx_files[:num_docs_to_combine]:
            file_path = os.path.join(folder_path, file_name)
            print(f"Procesando: {file_path}")
            source_document = word.Documents.Open(file_path)
            
            for table in source_document.Tables:
                table.Range.Copy()  # Copiar tabla completa
                output_document.Range(output_document.Content.End - 1).Paste()  # Pegar al final del documento
                output_document.Content.InsertAfter("\n")  # Agregar un salto de línea
            
            source_document.Close()

        # Guardar el documento combinado en el formato elegido
        output_path = os.path.join(folder_path, f"{output_file}.{output_format}")
        if output_format == "word":
            output_document.SaveAs(output_path)
        elif output_format == "pdf":
            output_document.SaveAs(output_path, FileFormat=17)  # Formato 17 = PDF en Word COM
        else:
            raise ValueError("Formato de salida no válido. Use 'word' o 'pdf'.")

        print(f"Archivo combinado guardado en: {output_path}")
    
    except Exception as e:
        print(f"Error al combinar documentos: {e}")
    
    finally:
        # Cerrar Word
        output_document.Close()
        word.Quit()


if __name__ == "__main__":
    folder_path = "C:/Users/CTM40/Desktop/Automatizacion/data"

    combine_tables(folder_path, output_file="Documento_Combinado_final", output_format="pdf")
