import pytube
from pytube.cli import on_progress
from pytube import YouTube as YT

url_youtube = input("Introduce la url del video: ")

yt =YT (url_youtube,on_progress_callback=on_progress)

yt.streams.get_audio_only().download()
