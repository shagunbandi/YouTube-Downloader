from helper import up_down
from audio import download_audio
from video import download_video

print('YouTube Downloader\n')

url = input('Enter the url : ')

audio_or_video_options = ['Audio', 'Video']
audio_or_video = up_down(audio_or_video_options)

playlist_or_not = input("Do you want to download the playlist (y/n)")
playlist_or_not = True if playlist_or_not == 'y' else False

if audio_or_video == audio_or_video_options[0]:
    download_audio(url, playlist_or_not)
elif audio_or_video == audio_or_video_options[1]:
    download_video(url, playlist_or_not)