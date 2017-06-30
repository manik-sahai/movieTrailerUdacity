# class movie contains -title, -poster_image, -youtube_trailer


class Movie:
    """ This class Movie provides a way to store movie related info """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
