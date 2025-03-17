from yt_dlp import YoutubeDL
import os

desktop_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Desktop')

url = input("Enter the URL of the video: ")
print("Select the quality of the video:")
print("1. 1080p (best quality up to 1080p)")
print("2. Best available quality (maximum available quality)")

quality = input("Enter your choice: ")

if quality == '1':
    format_option = 'bestvideo[height<=1080]+bestaudio/best'
elif quality == '2':
    format_option = 'bestvideo+bestaudio/best'
else:
    print("Invalid choice! Exiting...")
    exit()

ydl_opts = {
    'format': format_option,
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
    


