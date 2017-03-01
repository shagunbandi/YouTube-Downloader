import requests
from bs4 import BeautifulSoup
from pytube import YouTube


def choices(options, opt):
    cnt = 0
    for option in options:
        if cnt == opt:
            print('[*]', option)
        else:
            print('[ ]', option)
        cnt += 1


def downloader(video_url):
    yt = YouTube(video_url)
    print('Which file format would you like to download for ',yt.filename)

    options = yt.get_videos()
    counter = 0
    choices(options, counter)
    final = ''
    while 1 == 1:
        ch = input()

        if ch == 'd':
            counter += 1

        elif ch == 'u':
            counter -= 1

        elif ch == 'y':
            final = options[counter]
            break
        choices(options, counter)

    final = str(final)
    final = final.split(' ')
    qual = final[-3]
    type = final[-5]
    type = type[2:-1]
    print('Your video',yt.filename ,'has started to download in',qual,'quality')
    video = yt.get(type, resolution=qual)
    video.download('')


def get_playlist(url):
    source_code = requests.get(url)
    html = source_code.text
    soup = BeautifulSoup(html, 'lxml')
    playlist = []
    for vid in soup.findAll(attrs={'class': 'playlist-video'}):
        playlist.append('https://www.youtube.com' + vid['href'])
    return playlist

def download_playlist(url):
    playlist = get_playlist(url)
    cnt = 0
    final = ''
    print('Which file format would you like to download for ')
    for vid in playlist:

        yt = YouTube(vid)
        options = yt.get_videos()

        if cnt == 0:
            cnt += 1
            counter = 0
            choices(options, counter)

            while 1 == 1:
                ch = input()

                if ch == 'd':
                    counter += 1

                elif ch == 'u':
                    counter -= 1

                elif ch == 'y':
                    final = options[counter]
                    break
                choices(options, counter)

            final = str(final)
            final = final.split(' ')
        qual = final[-3]
        type = final[-5]
        type = type[2:-1]
        print('Your video', yt.filename, 'has started to download in', qual, 'quality')
        video = yt.get(type, resolution=qual)
        video.download('')


print('YouTube Downloader\n')
print('would you like to download\n1. song\n2. playlist')

# options = ['song','playlist']
ch = input()
url = input('Enter the url : ')

if ch == '1':
    downloader(url)
else:
    download_playlist(url)