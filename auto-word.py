import os
import re
import win32com.client

# Ruta donde se encuentran todos los archivos Word
folder_path = "C:/Users/CTM40/Desktop/Automatizacion/data"
output_file = "Documento_Combinado_final.docx"

# Crear instancia de Word
word = win32com.client.Dispatch("Word.Application")
word.Visible = False  # Hacer Word invisible (opcional)

# Crear un nuevo documento
output_document = word.Documents.Add()

# Función para extraer el número de un nombre de archivo
def extract_number(file_name):
    match = re.search(r'_(/d+)', file_name)  # Busca un número después de "_"
    return int(match.group(1)) if match else float('inf')  # Devuelve un número grande si no encuentra un número

# Obtener la lista de archivos y ordenarlos por número extraído
docx_files = [file for file in os.listdir(folder_path) if file.endswith(".docx")]
docx_files = sorted(docx_files, key=extract_number)  # Ordenar por el número extraído

# Asegurarse de no combinar más archivos de los que existen
num_docs_to_combine = min(800, len(docx_files))  # Combinar máximo 800 documentos o menos si no hay suficientes
print("numero doc: ",num_docs_to_combine)

# Iterar sobre los primeros 'num_docs_to_combine' documentos y copiar tablas
for file_name in docx_files[:num_docs_to_combine]:
    file_path = os.path.join(folder_path, file_name)
    print(f"Procesando: {file_path}")
    source_document = word.Documents.Open(file_path)
    
    # Copiar cada tabla del documento
    for table in source_document.Tables:
        table.Range.Copy()  # Copiar tabla completa
        output_document.Range(output_document.Content.End - 1).Paste()  # Pegar al final del documento
        output_document.Content.InsertAfter("/n")  # Agregar un salto de línea
    
    source_document.Close()

# Guardar el documento combinado
output_document.SaveAs(os.path.join(folder_path, output_file))
output_document.Close()
word.Quit()

print("Se han combinado las tablas con formato completo de los primeros documentos seleccionados.")
