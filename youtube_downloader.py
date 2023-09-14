from pytube import YouTube
import tkinter as tk

def download_video():
    yt = YouTube(url_entry.get())
    stream = yt.streams.get_highest_resolution()
    output_directory = "./youtube/videos/"
    output_filename = stream.default_filename

    stream.download(output_path=output_directory, filename=output_filename)

def download_audio():
    yt = YouTube(url_entry.get())
    stream = yt.streams.get_audio_only()
    output_directory = "./youtube/audios/"
    output_filename = f"{yt.title}.mp3"

    stream.download(output_path=output_directory, filename= output_filename)

window = tk.Tk()
window.geometry("300x120")
window.title("Youtube Downloader")

window.eval('tk::PlaceWindow . center')

url_text = tk.Label(window, text='URL')
url_text.pack(padx=10, pady=5)

url_entry = tk.Entry(window, width=20)
url_entry.pack(padx=10, pady=5)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

video_button = tk.Button(button_frame, text='Vídeo', command=download_video)
video_button.pack(side=tk.LEFT, padx=5)

audio_button = tk.Button(button_frame, text='Áudio', command=download_audio)
audio_button.pack(side=tk.LEFT, padx=5)

window.mainloop()