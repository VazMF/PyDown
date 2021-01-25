from lib.download import *
from lib.interface import *
from time import sleep

header("Welcome to PyDown {}{}".format('\U0001F40D', '\U00002B07'))
sleep(3)

print('What do you want to do?')
my_list = ['Download an audio', 'Download audios from a playlist', 'Download a video', 'Download a videos playlist']
menu(my_list)

ans = str(input('R: ')).strip()
while ans not in '1234':
    print('\033[31m[ERROR] please, choose a valid option.\033[m')
    ans = str(input('R: ')).strip()

else:
    if ans == '1':
        link = str(input('Link: '))
        download_one_music(link)
    if ans == '2':
        link = str(input('Playlist link: '))
        download_playlist(link)
    if ans == '3':
        link = str(input('Video link: '))
        download_one_video(link)
    if ans == '4':
        link = str(input('Playlist link: '))
        download_video_playlist(link)
