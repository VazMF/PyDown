import PySimpleGUI as sg
from lib.download import *


class PythonScreen:

    def __init__(self):
        sg.change_look_and_feel('Python')
        layout = [
            [sg.Text('Link', size=(5, 0)), sg.Input(key='link', size=(75, 10))],
            [sg.Text('Pasta', size=(5, 0)), sg.Input(key='folder', size=(68, 10)), sg.FolderBrowse('...')],
            [sg.Text('O que você quer baixar?', key='instruction')],
            [sg.Radio('Áudio', 'media_format', key='audio'),
             sg.Radio('Playlist de áudios', 'media_format', key='audio_playlist'),
             sg.Radio('Vídeo', 'media_format', key='video'),
             sg.Radio('Playlist de vídeos', 'media_format', key='video_playlist')],
            [sg.Button('Download', key='download')],
            [sg.Output(size=(80, 5))]
        ]

        self.window = sg.Window("PyDown {}{}".format('\U0001F40D', '\U00002B07')).layout(layout)
        self.button, self.values = self.window.Read()

    def start(self):
        folder = self.values['folder']
        while True:
            self.button, self.values = self.window.Read()
            if self.values['audio'] is True:
                download_one_music(self.values['link'], folder)
            elif self.values['audio_playlist'] is True:
                download_playlist(self.values['link'], folder)
            elif self.values['video'] is True:
                download_one_video(self.values['link'], folder)
            elif self.values['video_playlist'] is True:
                download_video_playlist(self.values['link'], folder)


screen = PythonScreen()
screen.start()
