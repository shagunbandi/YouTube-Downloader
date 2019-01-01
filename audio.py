from __future__ import unicode_literals
import youtube_dl


def download_audio(url, playlist=False, quality='192'):
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': 'music/%(title)s.%(ext)s',
		'extractaudio': True,
		'noplaylist' : not playlist,
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': quality,
		}],
	}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])


if __name__ == "__main__":
	url = 'https://www.youtube.com/watch?v=KtlgYxa6BMU'
	# url = 'https://www.youtube.com/watch?v=_KhQT-LGb-4&list=PL4uUU2x5ZgR1JOlcY9SZB94MW6fBE8ovU'
	download_audio(url, playlist=True)