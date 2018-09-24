import webbrowser


class Movie():
	'''
	it's a class that takes several perameters to provide a movie's details.
	'''
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title.title()
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def get_movie_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	# def poster(self):
	# 	open(self.poster_image_url)
