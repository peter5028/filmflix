from connect import *
from time import sleep
from printRecords import *

def insertRecord():
    tblFilms = [] # primary key, 0, 1, 2

    # ask user for input for the films table (title, year released, rating, duration, genre)
    title = input("Enter film title: ")
    yearReleased = input("Enter year released: ")
    rating = input("Enter rating: ")
    duration = input("Enter duration in mins: ")
    genre = input("Enter the genre: ")

    # append data from user input to the films list
    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)
    # INSERT INTO tblFilms (title, year released, rating, duration, genre) VALUES("A","B","C,"D","E")
    try:
        cursor.execute("INSERT INTO tblFilms (title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", tblFilms)
        connection.commit()
        print(f"Title {title} added into the films table.")
        sleep(2)
        read()
    except sqlite3.OperationalError as e:
        connection.rollback()
        print(f"Record not added to database: {e}")

if __name__ == "__main__":
    insertRecord()