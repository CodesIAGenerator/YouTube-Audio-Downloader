import tkinter as tk
from tkinter import ttk, messagebox
import pytube
from pytube import YouTube as YT
import os
from moviepy.editor import AudioFileClip
from threading import Thread
import time

def download_audio(url, progressbar):
    try:
        def progress_function(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            progressbar['value'] = percentage_of_completion
            root.update_idletasks()

        yt = YT(url, on_progress_callback=progress_function)

        stream = yt.streams.filter(only_audio=True).first()
        stream.download()

        base, ext = os.path.splitext(stream.default_filename)
        new_file = base + '.mp3'
        # Convert the .webm file to .mp3
        clip = AudioFileClip(stream.default_filename)

        # Estimate conversion time based on clip duration
        estimated_conversion_time = clip.duration / 4
        time_per_update = estimated_conversion_time / 100
        for i in range(100):
            time.sleep(time_per_update)
            progressbar['value'] += 1
            root.update_idletasks()

        clip.write_audiofile(new_file)

        # Remove the original .webm file
        os.remove(stream.default_filename)

        messagebox.showinfo("Success", yt.title + " ha sido descargado correctamente...")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_download(progressbar):
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "URL cannot be empty")
        return
    progressbar['value'] = 0
    progressbar['maximum'] = 200  # Set maximum progress to 200 for audio download
    # Start download in a separate thread so as not to block the GUI
    Thread(target=download_audio, args=(url, progressbar), daemon=True).start()

def download_video(url, progressbar):
    try:
        def progress_function(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            progressbar['value'] = percentage_of_completion
            root.update_idletasks()

        yt = YT(url, on_progress_callback=progress_function)

        stream = yt.streams.get_highest_resolution()
        stream.download()

        messagebox.showinfo("Success", yt.title + " ha sido descargado correctamente...")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_download_video(progressbar):
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "URL cannot be empty")
        return
    progressbar['value'] = 0
    progressbar['maximum'] = 100  # Set maximum progress to 100 for video download
    # Start download in a separate thread so as not to block the GUI
    Thread(target=download_video, args=(url, progressbar), daemon=True).start()

root = tk.Tk()
root.title("YouTube Downloader")

url_label = tk.Label(root, text="YouTube Video URL")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

audio_progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate', maximum=200)
audio_progress_bar.pack()

download_audio_button = tk.Button(root, text="Download Audio", command=lambda: start_download(audio_progress_bar))
download_audio_button.pack()

video_progress_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate', maximum=100)
video_progress_bar.pack()

download_video_button = tk.Button(root, text="Download Video", command=lambda: start_download_video(video_progress_bar))
download_video_button.pack()

root.mainloop()