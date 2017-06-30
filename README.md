# Read Me for Movie Trailer Website
This repo contains python source code to dynamically generate a web page containing a list of movie tiles which on being clicked show the youtube trailer.
There are *three python files* for this website:
1. **fresh_tomatoes.py**
contains the html, css and javascript code (structure, style and interactivity for the web page). It has two functions one called **open_movies_page** that takes a movie list parameter to render them on the web page and another function called **create_movie_tiles_content** that generates html content for each of the movie tiles.
2. **media&#46;py** contains the definition of the class movie and has instance variables for title, movie poster, and the youtube trailer of the movie. It also has the constructor for the movie class.
3. **entertainment_center&#46;py** contains various instances of the movie class with actual values for title, poster link and youtube link passed into the constructor for the movie class. All the instance names are put in a list which is then passed to the calling function open_movies_page function of the fresh_tomatoes.py module.

### How to Generate the Movie Trailer Website
Follow the following steps to run the website
1. The target machine should have python version 2.7 installed.
2. Download and keep the three python files (described above) in to same folder.
3. It can be run in two ways :
* from the command line go to the folder where the three python files reside. Type **python entertainment_center.py** and hit enter. The program will compile and a new **fresh_tomatoes.html** will be generated and also opened in the browser.
* open the python file **entertainment_center.py** in a python IDE (integrated development environment) and from the toolbar click Run. Similar to command line the program will compile and a new **fresh_tomatoes.html** will be generated and also opened in the browser.
4. Once web page opens in a browser, click on the poster of any movie displayed there to view its trailer.

#### Coding Convention
PEP 8 coding standard has been followed. (Some extra long urls exceeding 80 characters have been marked with #NOQA)

#### Note
The background color of the body of the web page has been customized and is different from the given default value.