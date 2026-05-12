from pytube import YouTube
from pytube import Playlist

link = input("Enter link: ")
yt = YouTube(link)

action = int(input("1. just video \n2.subtitles \n3.playlist \n4.Get URL on each video in playlist \n"))
if action == 1:
    print("download in highest resolution? y/n")
    ans = input().lower()
    if ans == "y":
        YouTube(link).streams.get_highest_resolution().download()
    else:
        yt.streams.first().download()
    print(yt.title, "done")
if action == 2:
    print("enter the code representing the language [en, ru, ua]")
    lang = input().lower()
    yt.captions[lang].download(title="Sub", src=False)
    print(yt.title, "done")
if action == 3:
    playlist = Playlist(link)
    print(f"downloading playlist [{playlist.title}]")
    for video in playlist.videos:
        video.streams.first().download()
        print(video.title, " - done")
if action == 4:
    playlist = Playlist(link)
    for url in playlist.video_urls:
        print(f"{video.title} - {url}")
