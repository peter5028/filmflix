from connect import *
from time import sleep
from printRecords import *

def amend():
    # which field can be used to update a table(tblFilms)?
    filmID = input("Enter the filmID of the record to be updated: ")
    # field name to be updated
    fieldName = input("Enter the field name (title, year released, rating, duration, genre): ").title()

    newFieldValue = input(f"Enter the value for {fieldName} field: ")
    print(newFieldValue)
    newFieldValue = "'" + newFieldValue + "'"
    print(newFieldValue)

    try:
        # update a specific record
        # UPDATE tblFilms SET title, year released, rating, duration, genre/value WEHERE filmID = 1,2,3,4....
        cursor.execute(f"UPDATE tblFilms SET {fieldName} = {newFieldValue} WHERE filmID = {filmID}")
        connection.commit()

        print(f"Record {filmID} updated in the table")
        sleep(2) # delay the execution of any code that follows for 2 seconds
        read() # call/invoke the function
    except sqlite3.OperationalError as e:
        connection.rollback()
        print(f"Record not updated: {e}")
if __name__ == "__main__":
    amend()