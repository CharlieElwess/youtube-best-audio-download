import yt_dlp
import ffmpeg
import os

def dl_audio_from_video():
    URL = input("Paste video URL: ")
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/best',
        'outtmpl': '%(title)s.m4a'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URL)
    print("Download complete ㋡")

if __name__ == "__main__":
    dl_audio_from_video()
