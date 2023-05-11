from connect import *
from time import sleep
from printRecords import *

def delete():
    filmId = input("Enter the film ID of the record to be deleted: ")
    try:
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmId}")

        connection.commit()

        print(f"The record {filmId} has been deleted from the films table.")

        sleep(2)
        read()
    except sqlite3.OperationalError as e:
        connection.rollback()
        print(f"Record not found in database: {e}")

if __name__ == "__main__":
    delete()