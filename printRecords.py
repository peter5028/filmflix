from connect import *

def read():
    try:
        cursor.execute("SELECT * FROM tblFilms") # select all films
        row = cursor.fetchall() # get all the selected record form the table in the database
        for aRecord in row:
            print(aRecord)
    except sqlite3.OperationalError as e:
        print(f"Records not found: {e}")

if __name__ == "__ main__":
    read() # call/invoke the function