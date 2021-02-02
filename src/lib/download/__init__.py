from pytube import YouTube, Playlist
from lib.converter import *

music_folder = "/home/vaz_mf/Música"
video_folder = "/home/vaz_mf/Vídeos"


def download_one_music(yt_link):
    yt = YouTube(yt_link).streams.filter(only_audio=True).first().download(music_folder)
    converter(yt)
    print(f'{yt.title()} was successfully downloaded.')


def download_playlist(yt_link):
    playlist = Playlist(yt_link)
    try:
        for url in playlist:
            yt = YouTube(url).streams.filter(only_audio=True).first().download(music_folder)
            converter(yt)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'The playlist was successfully downloaded.')



def download_one_video(yt_link):
    try:
        yt = YouTube(yt_link).streams.get_highest_resolution().download(video_folder)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'{yt.title()} was successfully downloaded.')


def download_video_playlist(yt_link):
    playlist = Playlist(yt_link)
    try:
        for url in playlist:
            yt = YouTube(url).streams.filter().get_highest_resolution().download(video_folder)
    except:
        print("[ERROR] Please, try again")
    else:
        print(f'The playlist was successfully downloaded.')

