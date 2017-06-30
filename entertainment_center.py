import media  # contains the movie class which has characteristics of a movie
import fresh_tomatoes  # contains the layout of the web page and the function to render the page

# instances of class movie to populate the web page with actual movie data

thor_ragnarok = media.Movie("Thor: Ragnarock", "http://empireonline.media/jpg/70/0/0/1280/960/aspectfit/0/0/0/0/0/0/c/articles/58c043053302c94d18f73263/thor-ragnarok-ew-cover.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=v7MGUNV8MxU")

spider_man = media.Movie("Spiderman:Homecoming", "https://i.imgbox.com/574OovOo.jpg", "https://www.youtube.com/watch?v=xEvV3OsE2WM")  # NOQA

justice_league = media.Movie("Justice League", "http://orig10.deviantart.net/1e5f/f/2017/061/1/a/justice_league_movie_poster_4_by_jackjack671120-db10aub.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=3cxixDgHUYw")

wonder_woman = media.Movie("Wonder Woman", "http://cdn2-www.superherohype.com/assets/uploads/gallery/wonder-woman/wwpost345.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=VSB4wGIdDwo")

iron_man = media.Movie("Iron Man", "http://www.impawards.com/2008/posters/iron_man_ver3_xlg.jpg", "https://www.youtube.com/watch?v=8hYlB38asDY")  # NOQA

the_avengers = media.Movie("The Avengers", "http://orig15.deviantart.net/f2e7/f/2010/228/c/3/__the_avengers___movie_poster_by_themadbutcher.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=eOrNdBpGMv8")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy", "http://agentpalmer.com/wp-content/uploads/2014/08/Official-Guardians-of-the-Galaxy-Movie-Poster.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=d96cjJhvlMA")

jurassic_Park = media.Movie("Jurassic Park", "http://moviereviews.s3.amazonaws.com/2016/04/11/17/47/51/994/oW484gwIHBk7haWwIunUuySqPfx.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=_IesovZQR4g")

the_greatest_game_ever_played = media.Movie("The Greatest Game Ever Played", "https://i.jeded.com/i/the-greatest-game-ever-played.18712.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=8xK9yXKldrk")

movies = [thor_ragnarok, spider_man, justice_league, wonder_woman, iron_man, the_avengers, guardians_of_the_galaxy,
          jurassic_Park, the_greatest_game_ever_played]  # list containing movies

fresh_tomatoes.open_movies_page(movies)  # function to render web page containing data from a list of movies
