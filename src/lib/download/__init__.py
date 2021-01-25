from pip._vendor.requests.utils import from_key_val_list
from pytube import YouTube, Playlist
from lib.converter import *


def download_one_music(yt_link):
    folder = "/home/vaz_mf/Música"
    yt = YouTube(yt_link).streams.filter(only_audio=True).first().download(folder)
    converter(yt)
    print(f'\033[32m{yt.title()} was successfully downloaded.\033m')


def download_playlist(yt_link):
    folder = "/home/vaz_mf/Música"
    playlist = Playlist(yt_link)
    for url in playlist:
        yt = YouTube(url).streams.filter(only_audio=True).first().download(folder)
        converter(yt)
    print(f'\033[32mThe playlist was successfully downloaded.\033[m')


def download_one_video(yt_link):
    folder = "/home/vaz_mf/Vídeos"
    yt = YouTube(yt_link).streams.get_highest_resolution().download(folder)
    print(f'\033[32m{yt.title()} was successfully downloaded.\033[m')


def download_video_playlist(yt_link):
    folder = "/home/vaz_mf/Vídeos"
    playlist = Playlist(yt_link)
    for url in playlist:
        yt = YouTube(url).streams.filter().get_highest_resolution().download(folder)
    print(f'\033[32mThe playlist was successfully downloaded.\033[m')

