import sqlite3



connection = sqlite3.connect("filmflix.db")

cursor = connection.cursor()

connection.commit()
