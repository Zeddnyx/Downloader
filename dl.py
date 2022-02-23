import pafy
import os

def DownloadYT():
	print('----------------------\n[!] Youtube downloader\n----------------------\n')
	url = input('[?] Link : ')
	link_url = pafy.new(url)
	print('')
	print('[*] Title  : ',link_url.title)
	print('[*] Author : ',link_url.author)
	print('')
	print('[1] Audio only\n[2] Video')
	asq = input('[?] Choice :')

	if asq == '1':
		os.system('clear')
		audiostreams = link_url.audiostreams
		for a in audiostreams:
			print('[!] This is all resulution audio')
			print('-[*]', a.bitrate, a.extension, a.get_filesize())

			cho = int(input('\n[?] Choice resolution :'))
			if cho == 1:
				print('Downloading...')
				audiostreams[1].download()
				break

			elif cho == 2:
				print('Downloading...')
				audiostreams[2].download()
				break

			elif cho == 3:
				print('Downloading...')
				audiostreams[3].download()
				break

			elif cho == 4:
				print('Downloading...')
				audiostreams[4].download()
				break

			elif cho == 5:
				print('Downloading...')
				audiostreams[5].download()
				break

			elif cho == 6:
				print('Downloading...')
				audiostreams[6].download()
				break

			elif cho == 7:
				print('Downloading...')
				audiostreams[7].download()
				break

			else:
				pass


	elif asq == '2':
		os.system('clear')
		print('\n[/] Downloading Video...')
		dl = link_url.getbest()
		dl.download()


def DownloadFB():
	print('-----------------------------\n[!] Facebook downloader\n-----------------------------\n')
	urlfb = input('[?] Link : ')
	return '[!] Sorry this tool not available right now'


def DownloadIG():
	print('------------------------------\n[!] Instagram downloader \n---------------------------\n')
	urlig = input('[?] Link : ')
	return '[!] Sorry this tool not available right now'


def Menu():

	print('=====================================\n[!] Tools for downloading video/audio\n[*] Author : Zeddnyx\n=====================================\n')
	print('[1] Youtube\n[2] Facebook\n[3] Instagram\n')
	ask = int(input('[?] Choice : '))
	print('')
	try: 
		if ask == 1:
			os.system('clear')
			return DownloadYT()

		elif ask == 2:
			os.system('clear')
			return DownloadFB()

		elif ask == 3:
			os.system('clear')
			return DownloadIG()

	except:
		print('\n[!] Invalid input !!!')

os.system('clear')
Menu()

