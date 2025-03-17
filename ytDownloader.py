from pytube import YouTube 
from yt_dlp import YoutubeDL
import sys
import os

desktop_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop')

url = input("Enter the URL of the video: ")
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best',
    'n_connections': 16, 
    'external_downloader': 'aria2c', 
    'external_downloader_args': ['-x', '16', '-k', '1M'], 
     'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Convert video to mp4 format
    }] ,
    'outtmpl': os.path.join(desktop_path,'%(title)s.%(ext)s'),
}

with YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)

    print (f"Title: {info.get('title')}")
    print (f"Duration: {info.get('duration')}")
    print (f"Title: {info.get('view_count')}")

    print("Downloading...")
    ydl.download([url])
    print("Download completed!")


