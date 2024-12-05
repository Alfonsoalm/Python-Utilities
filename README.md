# Python-Utilities

## **Descripción General**
`Python-Utilities` es un conjunto de scripts y herramientas en Python diseñados para automatizar tareas repetitivas y optimizar flujos de trabajo en diversas áreas, como la gestión de archivos, manejo de documentos, procesamiento de datos, automatización web, gestión de correos electrónicos, y más.

## **Índice**
1. [Funciones de Gestión de Archivos](#gestión-de-archivos)
2. [Manejo de Documentos Word y PDF](#manejo-de-documentos-word-y-pdf)
3. [Automatización de WhatsApp](#automatización-de-whatsapp)
4. [Automatización de Correo Electrónico](#automatización-de-correo-electrónico)
5. [Gestión de PowerPoint](#gestión-de-powerpoint)
6. [Procesamiento de Videos](#procesamiento-de-videos)
7. [Automatización Web](#automatización-web)
8. [Combinación y Selección de PDFs](#combinación-y-selección-de-pdfs)
9. [Generación y Gestión de Documentos](#generación-y-gestión-de-documentos)
10. [Lectura y Envío de Mensajes de WhatsApp](#lectura-y-envío-de-mensajes-de-whatsapp)

---

## **1. Gestión de Archivos**
Scripts para gestionar archivos y carpetas, incluyendo eliminación de duplicados, organización por extensión, y renombrado masivo.

### **Funcionalidades**
- **Eliminación de archivos duplicados:** Identifica y elimina duplicados basándose en el hash MD5.
- **Organización de archivos:** Ordena archivos en subcarpetas basadas en su extensión.
- **Renombrado masivo:** Renombra archivos de una carpeta según un patrón:
  - Por números secuenciales (`archivo_001.txt`).
  - Por fecha de creación (`archivo_2024-12-05.txt`).
  - Con prefijos o sufijos personalizados.

### **Uso**
```bash```
python auto-file-manager.py

## **2. Manejo de Documentos Word y PDF**
Automatización de tareas comunes con archivos Word y PDF, como generación de documentos, combinación de tablas, conversión a PDF y firma digital.

### **Funcionalidades**
- **Generación de documentos Word y PDF firmados:**
  - Genera documentos Word reemplazando marcadores con valores específicos.
  - Convierte automáticamente los documentos a PDF y aplica firma digital.
- **Combinación de tablas de Word:**
  - Combina tablas de múltiples archivos Word en un solo documento, con salida en Word o PDF.

### **Uso**
```bash```
python auto-word.py
python document-generator.py


## **3. Automatización de WhatsApp**
Scripts para interactuar con WhatsApp Web, enviar mensajes o leer chats automáticamente.

### **Funcionalidades**
- **Leer mensajes recientes:** 
  - Extrae los últimos mensajes de un contacto o grupo en WhatsApp y los guarda en un archivo `.txt`.
  - Diferencia entre mensajes enviados por el usuario y recibidos.
- **Enviar mensajes:**
  - Envía mensajes de texto automáticos a contactos o grupos.
  - Admite mensajes programados para enviarlos en una hora y minuto específicos.
- **Enviar imágenes con mensaje:**
  - Permite el envío de imágenes acompañadas de un mensaje a contactos o grupos.
  - Admite envío inmediato o programado.

### **Uso**
```bash```
python auto-whatsapp.py


## **4. Automatización de Correo Electrónico**
Gestión y automatización de correos electrónicos, como lectura, exportación y envío masivo.

### **Funcionalidades**
- **Lectura de correos:**
  - Accede a correos electrónicos de Gmail utilizando IMAP.
  - Extrae información del remitente, asunto y cuerpo de los correos.
  - Permite filtrar correos por remitente específico.
  - Exporta los correos leídos en formatos `.txt`, `.pdf` o `.docx`.
- **Envío de correos:**
  - Envía correos electrónicos individuales o masivos.
  - Admite incluir copias (CC) y copias ocultas (BCC).
  - Compatible con servidores SMTP como Gmail.

### **Uso**
```bash```
python auto-email.py


## **5. Gestión de PowerPoint**
Automatización para crear y editar presentaciones PowerPoint con imágenes.

### **Funcionalidades**
- **Generación de presentaciones:** 
  - Crea una presentación PowerPoint automáticamente utilizando imágenes de una carpeta.
- **Edición automática:**
  - Agrega imágenes a presentaciones existentes, posicionándolas en las diapositivas.

### **Uso**
```bash```
python auto-powerpoint.py


## **6. Procesamiento de Videos**
Descarga y procesamiento de videos desde YouTube.

### **Funcionalidades**
- **Descarga de videos:**
  - Descarga videos de YouTube en la mejor calidad disponible (audio y video).
- **Compatibilidad con `ffmpeg`:**
  - Integra audio y video en un único archivo `.mp4`.

### **Uso**
```bash```
python auto-video.py

## **7. Automatización Web**
Scripts para interactuar con páginas web usando Selenium.

### **Funcionalidades**
- **Inicio de sesión y scraping:**
  - Automatiza el inicio de sesión en páginas web y extrae contenido específico.
- **Exportación de datos:**
  - Guarda los datos extraídos en formatos como `.csv`.

### **Uso**
```bash```
python auto-web.py

## **8. Combinación y Selección de PDFs**
Automatización para combinar y procesar archivos PDF, permitiendo unir documentos o seleccionar páginas específicas.

### **Funcionalidades**
- **Combinar PDFs desde una carpeta:**
  - Une todos los PDFs en una carpeta en un único archivo.
- **Seleccionar páginas específicas:**
  - Crea un nuevo archivo PDF con las páginas seleccionadas de un archivo existente.

### **Uso**
```bash```
python auto-pdf.py combine <ruta_carpeta> <archivo_salida.pdf>
python auto-pdf.py select <archivo_entrada.pdf> <lista_páginas> <archivo_salida.pdf>


## **9. Generación y Gestión de Documentos**
Automatiza la creación de documentos a partir de plantillas y su procesamiento posterior.

### **Funcionalidades**
- **Reemplazo de marcadores:**
  - Inserta datos dinámicos en plantillas de documentos Word.
- **Conversión automática:**
  - Convierte los documentos generados a formato PDF.
- **Firma digital:**
  - Aplica firmas digitales a los documentos PDF utilizando un certificado PFX.

### **Uso**
```bash```
python document-generator.py


## **10. Lectura y Envío de Mensajes de WhatsApp**
Interactúa automáticamente con WhatsApp Web para gestionar chats.

### **Funcionalidades**
- **Lectura de mensajes recientes:**
  - Guarda los últimos mensajes de un contacto o grupo en un archivo `.txt`.
- **Envío de mensajes:**
  - Envía mensajes automáticos a contactos o grupos.
  - Admite mensajes programados para enviarlos a una hora y minuto específicos.
- **Envío de imágenes:**
  - Envía imágenes acompañadas de mensajes personalizados.

### **Uso**
```bash```
python auto-whatsapp.py
