from pytube import YouTube


# Envuelve el codigo de arriba en una funcion
def descargar_audio(url):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    print("Descarga completada!!")

# Crear funcion para descargar video
def descargar_video(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    # Mostrar barra de progreso de la descarga en porcentaje
    print("Descarga completada!!")


# Crea un menu con bucle while para que el usuario pueda descargar varios videos
while True:
    print("Bienvenido a Youtube Downloader")
    print("1. Descargar audio")
    print("2. Descargar video")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        url = input("Ingrese la URL del video: ")
        descargar_audio(url)
    elif opcion == 2:
        url = input("Ingrese la URL del video: ")
        descargar_video(url)
    elif opcion == 3:
        break
    else:
        print("Opcion no valida")

