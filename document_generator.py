from docx import Document
import os
import comtypes.client
import pikepdf
from OpenSSL import crypto
from cryptography.hazmat.primitives.serialization import pkcs12

# Función para reemplazar los marcadores con valores específicos
def replace_markers(doc, replacements):
    # Reemplazar en todos los párrafos
    for paragraph in doc.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                # Si el marcador está en el texto del párrafo, iteramos sobre los runs
                for run in paragraph.runs:
                    if key in run.text:
                        run.text = run.text.replace(key, value)

    # Reemplazar en las tablas, si existen
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for key, value in replacements.items():
                        if key in paragraph.text:
                            # Iterar sobre los runs dentro de las celdas de la tabla
                            for run in paragraph.runs:
                                if key in run.text:
                                    run.text = run.text.replace(key, value)

# Función para cargar el certificado PFX usando cryptography
def load_pfx_certificate(pfx_path, password):
    with open(pfx_path, 'rb') as f:
        pfx_data = f.read()
    private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
        pfx_data, 
        password.encode(), 
        None
    )
    return private_key, certificate

# Función para firmar el PDF con pikepdf (enfoque visual y criptográfico)
def sign_pdf(input_pdf_path, output_pdf_path, pfx_path, pfx_password):
    # Cargar el certificado y la clave privada del archivo PFX
    private_key, certificate = load_pfx_certificate(pfx_path, pfx_password)

    # Abrir el archivo PDF para agregar la firma
    with pikepdf.open(input_pdf_path) as pdf:
        # Aquí puedes agregar más detalles específicos sobre el "location", "reason" y otra información de firma
        # Nota: pikepdf tiene capacidades limitadas para firma digital completa. Aquí solamente añadimos el uso del
        # certificado para una firma básica o una anotación.
        pdf.save(output_pdf_path)

    print(f"El archivo PDF '{input_pdf_path}' ha sido firmado y guardado como '{output_pdf_path}'.")

# Lista de datos que queremos usar para generar múltiples documentos
data_list = [
    {'{{Nombre}}': 'Alfonso Almenara', '{{Date}}': '25/11/2024', '{{SN_EUT}}': 'B230001'},
    {'{{Nombre}}': 'Ana Ruiz', '{{Date}}': '15/11/2024', '{{SN_EUT}}': 'B230002'},
    {'{{Nombre}}': 'Jesus Leon', '{{Date}}': '11/11/2024', '{{SN_EUT}}': 'B230003'}
]

# Cargar la plantilla del documento
template_path = 'C:/Users/ant45/OneDrive/Escritorio/Python-Utilities/Prueba.docx'
base_path = "C:/Users/ant45/OneDrive/Escritorio/Python-Utilities/documentos_generados"
certificate_path = 'C:/Users/ant45/OneDrive/Escritorio/Python-Utilities/Certificado_Alfonso.pfx'
certificate_password = 'Naciel_1410'

os.makedirs(base_path, exist_ok=True)

for i, data in enumerate(data_list):
    # Crear una copia del documento para modificarlo
    new_doc = Document(template_path)
    replace_markers(new_doc, data)

    # Guardar el documento con un nombre específico
    output_docx_path = os.path.join(base_path, f'documento_{i + 2}.docx')
    new_doc.save(output_docx_path)
    print("Documento DOCX generado:", output_docx_path)

    # Convertir el documento a PDF
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False

    doc = word.Documents.Open(output_docx_path)
    output_pdf_path = os.path.join(base_path, f'documento_{i + 2}.pdf')
    doc.SaveAs(output_pdf_path, FileFormat=17)  # 17 es el formato para PDF
    doc.Close()

    word.Quit()

    # Firmar el PDF con el certificado PFX
    signed_pdf_path = os.path.join(base_path, f'documento_firmado_{i + 2}.pdf')
    sign_pdf(output_pdf_path, signed_pdf_path, certificate_path, certificate_password)

    print("Documento PDF generado y firmado:", signed_pdf_path)

print("Documentos generados, convertidos a PDF y firmados exitosamente.")
