from lib.download import *
from lib.interface import *
from time import sleep

header("Welcome to PyDown {}{}".format('\U0001F40D', '\U00002B07'))
sleep(1)

ans = ''
while ans != 5:
    print(line())
    print('What do you want to do?')
    my_list = ['Download an audio', 'Download audios from a playlist', 'Download a video', 'Download a videos playlist', 'Exit']
    menu(my_list)

    ans = str(input('A: ')).strip()
    if ans not in '12345':
        print('\033[31m[ERROR] please, choose a valid option.\033[m')
        ans = str(input('A: ')).strip()

    if ans == '1':
        link = str(input('Link: '))
        download_one_music(link)
    if ans == '2':
        link = str(input('Link: '))
        download_playlist(link)
    if ans == '3':
        link = str(input('Link: '))
        download_one_video(link)
    if ans == '4':
        link = str(input('Link: '))
        download_video_playlist(link)
    if ans == '5':
        break
