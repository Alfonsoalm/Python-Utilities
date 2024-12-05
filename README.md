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
8. [Descarga del Repositorio y Ejecución](#descarga-y-ejecución)

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
```bash
python auto-file-manager.py
