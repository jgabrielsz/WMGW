# WMGW
#### Video Demo: [link](https://www.youtube.com/watch?v=eehqSzt9nYo)
WMGW is a web-based project that aims to be a movie library, that although it is not possible to watch
movies on the site itself, the user can discover easily which movie you are going to watch next, as the 
movies are divided into several categories, thus facilitating the user's choice. You can also add movies 
to the User's private movie list.

# Description

The project was made using the python language together with the flask framework, the same taught in [cs50](https://cs50.harvard.edu/x/2022/weeks/9/), 
along with html, css and javascript. Bootstrap was also used for some site styling, but I also wrote various
css properties from scratch for the website. 
I decided to use a feature of the framework itself which are the blueprints, which as explained in the [flask 
documentation](https://flask.palletsprojects.com/en/2.2.x/blueprints/), serves to partition the project into different folders, in addition to the folders templates and
static, to facilitate the organization of the project. Using this functionality the organization and project
development was facilitated, with the following organization of folders:
Auth, Main, User, templates and static.

The Auth folder contains files related to user authentication (which by the way
It is not mandatory to access the site), In the User folder are the files referring to the user
that do not include authentication. And in the Main folder are the files referring to everything else
From the website. All three folders have their own templates and static folders if needed.

*NOTE*: In some html files the /static/posters folder is referenced, this folder is not on github
because it contains almost 65000 posters from the site, so I chose not to upload that folder.

I decided not to use an API for this project, as it is not intended to be published, but to be a
possibility of learning by getting hands-on in a relatively large project, and creating the bank
of data and feeding it from scratch is something much more challenging than using an API.

## About the project database
This project's database, named database.db which is referenced in some project files,
is a sqlite3 database and is not on github due to its size. He was created and
powered from scratch, using data from the [imdb dataset](https://www.imdb.com/interfaces/). When running .schema in the database the result is the Following:
"CREATE TABLE people(id TEXT PRIMARY KEY, name TEXT NOT NULL, professions TEXT, knownForTitles TEXT);
CREATE TABLE movies(id TEXT PRIMARY KEY, title TEXT NOT NULL, year INTEGER, genres TEXT);
CREATE TABLE ratings(id INTEGER NOT NULL, averageRating REAL, numVotes INTEGER, FOREIGN KEY(id) REFERENCES movies(id));
CREATE TABLE producers(id TEXT NOT NULL, directors TEXT, writers TEXT);
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT NOT NULL, hash TEXT NOT NULL);
CREATE TABLE users_lists(id INTEGER PRIMARY KEY, list TEXT);"

## Role of each project file

### app.py file
File responsible for interconnecting all blueprints of the project, and is also responsible for initiating
the app. All files that return a page to the user go through app.py, and when necessary
it sends a request from one blueprint to another. Its other function is to store data in the browser of the
user, such as keeping him logged in after closing and opening the site.

### templates/base.html
html base for all the other html files of the project, imports of local scripts or
external sources, such as bootstrap for example, here is written the basis of the project's appearance such as the navbar and the area
will be changed by the other html files of the project through jinja templates.

### static/style.css
css file with all properties defined locally from the site, all blueprints in the project use
this css file for styling the pages, all the spacing, hover effects and sizes of the divs are
defined here.

### static/Logo.png, Logo2.png, fire.jpg, poster_not_found.jpg
Images used in the project, Logo.png is the main logo of the project, Logo2.png is the mini-logo that appears in the
browser, fire.jpg is the background of the site, and poster_not_found.jpg is the image used when the movie is not
has poster.

### static/swiper.js, swiperAuto.js, usrModal.js
Javascript files to make the website carousels work, both the oscars carousel and the carousels
each category
on the main page.

### static/imgs/
Folder that contains the images that are shown in the oscars carousel, in which each image has the name of the id
of the film to which it refers.

### The rest of the folders follow this pattern:
Folder_blueprint/__init__.py , Folder_blueprint/templates/, Folder_blueprint/[blueprint name]_utils.py

### __init__.py of each folder
Main file of each blueprint, where the blueprint is defined, and where the functions that return a page
for the user are defined. For the functions present here to work, it is necessary to import the functions
present in [blueprint name]_utils.py.

### [blueprint name]_utils.py in each folder
File where functions that perform or not perform some action on the database are defined, all functions
present in this file are not executed directly, but called by __init__.py.

### /templates/ from each folder
Folder where the .html files of each blueprint are located, where some have an html called base_[blueprint name].html,
which works like the project's base.html, but only for this page, and it also extends what's in base.html.

### Auth/login_required.py
File that has the function to check if the user is logged in, and if not, redirect to the login page.
This function is imported whenever, at some point in the project, the user needs to be logged in.



