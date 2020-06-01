from pytube import YouTube

def show_progress_bar(stream, bytes, bytes_remaining):
	count_process =  str(len(links)) + ' of {}'
	process = round((bytes_remaining / stream.filesize) * 100)

	print(str(process) + '% - ' + link_video + ' - ' + count_process.format(num))


links = [link.strip() for link in open('READY_LINKS', 'r')]


for num, link in enumerate(links, start=1):

	try:
		yt = YouTube(link)
		yt.register_on_progress_callback(show_progress_bar)

		link_video = yt.title
		
		stream = yt.streams.first()
		stream.download('./downloads')

	except (KeyboardInterrupt):
		raise	
	except:
		print ('Failed to upload video')