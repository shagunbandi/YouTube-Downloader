from __future__ import unicode_literals
import youtube_dl


def download_audio(url, playlist=False, quality='192'):
	
	outtmpl = 'Music\\%(playlist)s\\%(playlist_index)s - %(title)s.%(ext)s' if playlist else 'Music\\%(title)s.%(ext)s'
	ydl_opts = {
		'format': 'bestaudio/best',
		'outtmpl': outtmpl,
		'extractaudio': True,
		'noplaylist' : not playlist,
		'nocheckcertificate' : True,
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': quality,
		}],
	}

	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
	except Exception as e:
		print(e)
	


if __name__ == "__main__":
	url = 'https://www.youtube.com/watch?v=KtlgYxa6BMU'
	# url = 'https://www.youtube.com/watch?v=_KhQT-LGb-4&list=PL4uUU2x5ZgR1JOlcY9SZB94MW6fBE8ovU'

	download_audio(url, playlist=True)
