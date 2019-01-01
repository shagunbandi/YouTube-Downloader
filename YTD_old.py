import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import os
from helper import up_down

def downloader(video_url):
    yt = YouTube(video_url)
    print('Which file format would you like to download for ',yt.filename)

    options = yt.get_videos()
    final = up_down(options)
    final = str(final)
    final = final.split(' ')
    qual = final[-3]
    type = final[-5]
    type = type[2:-1]
    print('Your video',yt.filename ,'has started to download in',qual,'quality')
    video = yt.get(type, resolution=qual)
    ensure_dir('Downloads/')
    video.download('Downloads/')


def get_playlist(url):
    source_code = requests.get(url)
    html = source_code.text
    soup = BeautifulSoup(html, 'lxml')
    playlist = []
    for vid in soup.findAll(attrs={'class': 'playlist-video'}):
        playlist.append('https://www.youtube.com' + vid['href'])
    title = str((soup.findAll('h3', {'class':'playlist-title'})[0]).text)
    title = (title.split('\n'))[1]
    while True:
        if title[0] == ' ':
            title = title[1:]
        elif title[-1] == ' ':
            title = title[:-1]
        else:
            break

    return playlist, title


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def download_playlist(url):
    playlist, title = get_playlist(url)
    cnt = 0
    final = ''
    print('Which file format would you like to download ')
    for vid in playlist:

        yt = YouTube(vid)
        options = yt.get_videos()

        if cnt == 0:
            cnt += 1
            final = up_down(options)
            final = str(final)
            final = final.split(' ')

        qual = final[-3]
        type = final[-5]
        type = type[2:-1]
        print('Your video', yt.filename, 'has started to download in', qual, 'quality')
        video = yt.get(type, resolution=qual)

        path = 'Playlist/'+title+'/'

        ensure_dir(path)

        video.download(path)


print('YouTube Downloader\n')

url = input('Enter the url : ')

options = ['Video','Playlist']

final = up_down(options)

if final == options[0]:
    downloader(url)
elif final == options[1]:
    download_playlist(url)
else:
    print('wrong input')