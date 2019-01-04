from __future__ import unicode_literals
import youtube_dl


def download_video(url, playlist=False):

	outtmpl = 'Movies\\%(playlist)s\\%(playlist_index)s - %(title)s.%(ext)s' if playlist else 'Movies\\%(title)s.%(ext)s'
	ydl_opts = {
		'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
		'outtmpl': outtmpl,
		'noplaylist' : not playlist,
		'nocheckcertificate' : True,
	}

	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
	except Exception as e:
		print(e)


if __name__ == "__main__":
	url = 'https://www.youtube.com/watch?v=KtlgYxa6BMU'
	# url = 'https://www.youtube.com/watch?v=_KhQT-LGb-4&list=PL4uUU2x5ZgR1JOlcY9SZB94MW6fBE8ovU'
	download_video(url, playlist=True)
	