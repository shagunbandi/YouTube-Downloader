from helper import up_down
from audio import download_audio
from video import download_video

print('YouTube Downloader\n')

url = input('Enter the url : \n')
options = ['Audio and Playlist', 'Audio and File', 'Video and Playlist', 'Video and File', 'Exit']


while True:

	try:
		op = up_down(options)
		if op == options[0]:
			download_audio(url, True)
			break
		elif op == options[1]:
			download_audio(url, False)
			break
		elif op == options[2]:
			download_video(url, True)
			break
		elif op == options[3]:
			download_video(url, False)
			break
		elif op == options[4]:
			break
		else:
			print("Please Select a valid option")
	except Exception as e:
		print("*** AN ERROR FOUND ***")
		print(e)
		print("*** END OF ERROR ***")
	

print("\n Thank You")

while True:
	inp = input()
	exit()