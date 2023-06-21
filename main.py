from pytube import YouTube
# Pide la URL del video
url = input("Ingresa la URL del video: ")
# Crea el objeto YouTube
yt = YouTube(url)
# Obtener el audio del video
stream = yt.streams.filter(only_audio=True).first()
# Descargar el archivo de audio
stream.download()

