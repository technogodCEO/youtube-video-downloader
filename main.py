from yt_dlp import YoutubeDL

URLS = input("Enter url to download here: ")
with YoutubeDL() as ydl:
    ydl.download(URLS)