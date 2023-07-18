import pytube
from pytube.cli import on_progress
from pytube import YouTube as YT
import os
from moviepy.editor import AudioFileClip

url_youtube = input("Introduce la url del video: ")

yt = YT(url_youtube, on_progress_callback=on_progress)

out_file = yt.streams.filter(only_audio=True).first().download()

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'

# Convertir el archivo .webm a .mp3
clip = AudioFileClip(out_file)
clip.write_audiofile(new_file)

# Eliminar el archivo .webm original
os.remove(out_file)

print(yt.title + " ha sido descargado correctamente...")