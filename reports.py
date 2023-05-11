from connect import *

# title, year released, rating, duration, genre

def allFilms():
    cursor.execute("SELECT * FROM tblFilms") # select all films
    row = cursor.fetchall() # display all the selected films from the database
    for aFilm in row:
        print(aFilm)

def title():
    title = input("Enter film title: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE title = '{title}' ") # select all titles
    row = cursor.fetchall() # diplay all the selected films from the database
    for aFilm in row:
        print(aFilm)

def year():
    yearReleased = input("Enter film's release year: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{yearReleased}' ") # select all titles
    row = cursor.fetchall() # diplay all the selected films from the database
    for aFilm in row:
        print(aFilm)

def rating():
    filmRating = input("Enter film rating: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{filmRating}' ") # select all titles
    row = cursor.fetchall() # diplay all the selected films from the database
    for aFilm in row:
        print(aFilm)

def duration():
    filmDuration = input("Enter film duration: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE duration = '{filmDuration}' ") # select all titles
    row = cursor.fetchall() # diplay all the selected films from the database
    for aFilm in row:
        print(aFilm)        

def genre():
    filmGenre = input("Enter film genre: ")
    cursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{filmGenre}' ") # select all titles
    row = cursor.fetchall() # diplay all the selected films from the database
    for aFilm in row:
        print(aFilm)

# call/invoke the functions
if __name__ == "__main__":
    allFilms()
    title()
    year()
    rating()
    duration()
    genre()
    