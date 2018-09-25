'''A program that prsesnts movie's trailers through a web browser'''


class Movie():
    '''
    Attributes:
    title (str): title of the movie.
    poster_image_url (str): URL link for the movies's poster image.
    trailer_youtube_url (str): URL link for the movie trailer.
    '''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title.title()
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
