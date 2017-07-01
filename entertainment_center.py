import media  # contains the movie class which has characteristics of a movie
import fresh_tomatoes  # contains the layout of the web page and the

# function to render the page

# instances of class movie to populate the web page with actual movie data

thor_ragnarok = media.Movie("Thor: Ragnarock", "https://goo.gl/9vyyef",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

spider_man = media.Movie("Spiderman:Homecoming",
                         "https://i.imgbox.com/574OovOo.jpg",
                         "https://www.youtube.com/watch?v=xEvV3OsE2WM")

justice_league = media.Movie("Justice League", "https://goo.gl/A5LbyF",
                             "https://www.youtube.com/watch?v=3cxixDgHUYw")

wonder_woman = media.Movie("Wonder Woman", "https://goo.gl/3E9Fam",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

iron_man = media.Movie("Iron Man", "https://goo.gl/eB4FFV",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

the_avengers = media.Movie("The Avengers", "https://goo.gl/D637P1",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "https://goo.gl/UjjwUn",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA")  # NOQA

jurassic_park = media.Movie("Jurassic Park", "https://goo.gl/wK6Gio",
                            "https://www.youtube.com/watch?v=_IesovZQR4g")

the_greatest_game_ever_played = media.Movie("The Greatest Game Ever Played",
                                            "https://goo.gl/zWqjr2",
                                            "https://www.youtube.com/watch?v=8xK9yXKldrk")  # NOQA


# list containing movies
movies = [thor_ragnarok, spider_man, justice_league, wonder_woman, iron_man,
          the_avengers, guardians_of_the_galaxy, jurassic_park,
          the_greatest_game_ever_played]

# function to render web page containing data from a list of movies
fresh_tomatoes.open_movies_page(movies)
