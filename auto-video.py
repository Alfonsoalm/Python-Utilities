import yt_dlp
import cv2
import whisper
import os
import warnings

# Ignorar advertencias de PyTorch
warnings.filterwarnings("ignore", category=FutureWarning, module="torch")

# Especifica la ubicación de FFmpeg
FFMPEG_PATH = "C:/ffmpeg/bin/ffmpeg.exe"  # Cambia según tu instalación


def download_video(url, output_directory="videos"):
    """
    Descarga un video desde una URL utilizando yt-dlp.
    Renombra el archivo descargado para eliminar espacios y caracteres especiales.
    """
    print("--------------------")
    print("Descargando video")
    print("--------------------")
    os.makedirs(output_directory, exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height=1080][ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"El video descargado no se encuentra: {video_path}")

    # Renombrar el archivo para quitar espacios
    sanitized_name = os.path.basename(video_path).replace(" ", "_")
    sanitized_path = os.path.join(output_directory, sanitized_name)
    os.rename(video_path, sanitized_path)

    print(f"Video descargado y renombrado en: {sanitized_path}")
    return sanitized_path


def resize_video_for_instagram(video_path, output_directory="output", instagram_format="9:16"):
    """
    Redimensiona y recorta un video para adaptarlo a los formatos de Instagram usando OpenCV.
    """
    print("--------------------")
    print("Reescalando video para Instagram")
    print("--------------------")

    target_dimensions = {
        "1:1": (1080, 1080),
        "4:5": (1080, 1350),
        "9:16": (1080, 1920)
    }

    if instagram_format not in target_dimensions:
        raise ValueError("Formato de Instagram inválido. Usa '1:1', '4:5', o '9:16'.")

    target_width, target_height = target_dimensions[instagram_format]

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"No se puede abrir el video: {video_path}")

    original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    scale = target_height / original_height
    resized_width = int(original_width * scale)
    resized_height = target_height

    crop_x_start = (resized_width - target_width) // 2
    crop_x_end = crop_x_start + target_width

    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "resized_video.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (target_width, target_height))

    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        frame_resized = cv2.resize(frame, (resized_width, resized_height))
        frame_cropped = frame_resized[:, crop_x_start:crop_x_end]
        out.write(frame_cropped)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video reescalado guardado en: {output_file}")
    return output_file


def convert_video_to_audio(video_path):
    """
    Convierte un video a un archivo de audio (WAV) usando FFmpeg.
    """
    print("--------------------")
    print("Extrayendo audio del video")
    print("--------------------")

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_directory = os.path.dirname(video_path)
    audio_path = os.path.join(output_directory, f"{base_name}_audio.wav")

    cmd = [
        FFMPEG_PATH,
        "-y", "-i", video_path, "-ar", "16000", "-ac", "1", "-f", "wav", audio_path
    ]

    print(f"Comando FFmpeg: {' '.join(cmd)}")
    result = os.system(" ".join(cmd))

    if result != 0 or not os.path.exists(audio_path):
        raise RuntimeError(f"FFmpeg falló al convertir {video_path} a {audio_path}")

    print(f"Audio extraído en: {audio_path}")
    return audio_path


def generate_subtitles(video_path):
    """
    Genera subtítulos para un video utilizando el modelo Whisper AI.
    """
    print("--------------------")
    print("Generando subtítulos")
    print("--------------------")
    model = whisper.load_model("base")
    audio_path = convert_video_to_audio(video_path)
    result = model.transcribe(audio_path)
    return result["segments"]


def add_subtitles_to_video(video_path, subtitles, output_directory="output"):
    """
    Agrega subtítulos directamente sobre un video usando OpenCV.
    """
    print("--------------------")
    print("Añadiendo subtítulos al video")
    print("--------------------")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"No se puede abrir el video: {video_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "video_with_subtitles.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    subtitle_index = 0
    for frame_no in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        current_time = frame_no / fps

        while (subtitle_index < len(subtitles) and
               subtitles[subtitle_index]['end'] < current_time):
            subtitle_index += 1

        if subtitle_index < len(subtitles):
            sub = subtitles[subtitle_index]
            if sub['start'] <= current_time <= sub['end']:
                text = sub['text']
                cv2.putText(frame, text, (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video con subtítulos guardado en: {output_file}")
    return output_file


def process_video_for_instagram(url, instagram_format="9:16", output_directory="output"):
    """
    Flujo completo para descargar, redimensionar y agregar subtítulos a un video para Instagram.
    """
    print("--------------------" * 10)
    print("Procesando video para Instagram")
    print("--------------------")
    video_path = download_video(url, output_directory="videos")
    resized_video_path = resize_video_for_instagram(video_path, output_directory=output_directory, instagram_format=instagram_format)
    subtitles = generate_subtitles(video_path)
    final_video_path = add_subtitles_to_video(resized_video_path, subtitles, output_directory=output_directory)
    print(f"Video final listo para Instagram: {final_video_path}")
    return final_video_path


if __name__ == "__main__":
    video_url = "https://youtu.be/dEtuadwCd6c"
    process_video_for_instagram(video_url, instagram_format="9:16")
