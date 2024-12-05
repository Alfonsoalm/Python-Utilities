import yt_dlp as youtube_dl
import shutil

# === Funcion para verificar formato ffmpeg ===
def verificar_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("ERROR: ffmpeg no está instalado. Por favor instala ffmpeg para continuar.")
        return False
    return True

# === Funcion para descargar video ===
def descargar_video(url):
    try:
        if not verificar_ffmpeg():
            return
        
        # Opciones de configuración para yt_dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Descargar el mejor video y el mejor audio disponibles
            'merge_output_format': 'mp4',           # Unir audio y video en formato MP4
            'outtmpl': '%(title)s.%(ext)s',         # Guardar el archivo con el título del video
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Descarga completada!")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=x_HUN6xxopY"
    descargar_video(url)