from pytube import YouTube, Playlist
from lib.converter import *


def download_one_music(yt_link, folder):
    yt = YouTube(yt_link).streams.filter(only_audio=True).first().download(folder)
    converter(yt, folder)
    print(f'{yt.title()} was successfully downloaded.')


def download_playlist(yt_link, folder):
    playlist = Playlist(yt_link)
    try:
        for url in playlist:
            yt = YouTube(url).streams.filter(only_audio=True).first().download(folder)
            converter(yt, folder)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'The playlist was successfully downloaded.')


def download_one_video(yt_link, folder):
    try:
        yt = YouTube(yt_link).streams.get_highest_resolution().download(folder)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'{yt.title()} was successfully downloaded.')


def download_video_playlist(yt_link, folder):
    playlist = Playlist(yt_link)
    try:
        for url in playlist:
            yt = YouTube(url).streams.filter().get_highest_resolution().download(folder)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'The playlist was successfully downloaded.')

