import os
import hashlib
from datetime import datetime

# === Función para calcular hash de un archivo ===
def calculate_hash(file_path, chunk_size=8192):
    """
    Calcula el hash MD5 de un archivo para identificar duplicados.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# === Función para encontrar archivos duplicados ===
def find_duplicates(folder_path):
    """
    Encuentra archivos duplicados en una carpeta.
    Retorna un diccionario donde la clave es el hash del archivo
    y el valor es una lista de archivos que comparten ese hash.
    """
    hashes = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash in hashes:
                hashes[file_hash].append(file_path)
            else:
                hashes[file_hash] = [file_path]
    return {k: v for k, v in hashes.items() if len(v) > 1}

# === Función para eliminar archivos duplicados ===
def delete_duplicates(folder_path):
    """
    Encuentra y elimina archivos duplicados en una carpeta.
    """
    duplicates = find_duplicates(folder_path)
    
    if duplicates:
        print("\nArchivos duplicados encontrados:")
        for files in duplicates.values():
            print("\n".join(files))
        
        confirm = input("\n¿Quieres eliminar los duplicados automáticamente? (s/n): ").lower()
        if confirm == 's':
            for file_list in duplicates.values():
                # Mantener solo el primer archivo y eliminar el resto
                for file_path in file_list[1:]:
                    try:
                        os.remove(file_path)
                        print(f"Eliminado: {file_path}")
                    except Exception as e:
                        print(f"Error al eliminar {file_path}: {e}")
            print("\nArchivos duplicados eliminados.")
        else:
            print("\nNo se eliminaron archivos.")
    else:
        print("\nNo se encontraron archivos duplicados.")

# === Función para organizar archivos por tipo ===
def organize_files(folder_path):
    """
    Organiza archivos en subcarpetas basadas en su extensión.
    """
    if not os.path.exists(folder_path):
        print("La carpeta no existe.")
        return
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1]
            folder_name = os.path.join(folder_path, file_extension.lower())
            os.makedirs(folder_name, exist_ok=True)
            new_file_path = os.path.join(folder_name, file)
            os.rename(file_path, new_file_path)
            print(f"Movido: {file} -> {folder_name}")

# === Función para renombrar archivos ===
def rename_files(folder_path, mode, prefix="", suffix="", replace_text=None, replace_with=None):
    """
    Renombra archivos en una carpeta según el modo especificado.
    
    Args:
        folder_path (str): Ruta de la carpeta con los archivos.
        mode (str): Modo de renombrado ('sequential', 'creation_date', 'custom').
        prefix (str): Prefijo que se añadirá al nombre del archivo.
        suffix (str): Sufijo que se añadirá al nombre del archivo.
        replace_text (str): Texto a buscar en el nombre del archivo.
        replace_with (str): Texto para reemplazar 'replace_text'.
    """
    if not os.path.exists(folder_path):
        print("La carpeta especificada no existe.")
        return

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("No se encontraron archivos en la carpeta.")
        return

    for i, filename in enumerate(files):
        file_path = os.path.join(folder_path, filename)
        file_name, file_extension = os.path.splitext(filename)

        # Generar el nuevo nombre basado en el modo seleccionado
        if mode == "sequential":
            new_name = f"{prefix}{i + 1:03d}{suffix}{file_extension}"  # Ejemplo: archivo_001.txt
        elif mode == "creation_date":
            creation_time = os.path.getctime(file_path)
            formatted_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")
            new_name = f"{prefix}{formatted_date}{suffix}{file_extension}"  # Ejemplo: archivo_2023-12-01.txt
        elif mode == "custom":
            new_name = f"{prefix}{file_name}{suffix}"
            if replace_text and replace_with:
                new_name = new_name.replace(replace_text, replace_with)
        else:
            print(f"Modo '{mode}' no reconocido. Saltando archivo.")
            continue

        # Verificar y asegurar que el nuevo nombre sea único
        new_file_path = os.path.join(folder_path, new_name)
        counter = 1
        while os.path.exists(new_file_path):
            # Si ya existe, añadir un número al final del archivo
            new_name = f"{prefix}{formatted_date}_{counter}{suffix}{file_extension}"
            new_file_path = os.path.join(folder_path, new_name)
            counter += 1

        # Renombrar el archivo
        os.rename(file_path, new_file_path)
        print(f"Renombrado: {filename} -> {new_name}")

    print("Renombrado completado.")


if __name__ == "__main__":
    print("\n=== File Manager ===")

    folder = "./documentos_entrada/docx"
    # print(f"Procesando la carpeta: {folder}")
    
    # Eliminar archivos duplicados
    # print("\n=== Eliminando archivos duplicados ===")
    # delete_duplicates(folder)
    
    # Organizar archivos por tipo
    # print("\n=== Organizando archivos por tipo ===")
    # organize_files(folder)

    print("\n=== Renombrando archivos ===")
    rename_files(
        folder_path=folder,
        mode="sequential",  # Opciones: 'sequential', 'creation_date', 'custom'
        prefix="archivo_",
        suffix=".txt",
        replace_text="",
        replace_with=""
    )
    print("\nProcesamiento completado.")

