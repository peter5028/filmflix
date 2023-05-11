from printRecords import *
from addRecord import *
from amendRecord import *
from deleteRecord import *
import reports

# create function
"Main Menu"
def menuOptions():
    options = 0
    while options not in ["1","2","3","4","5","6"]:
        print("Film Flix Menu Options:\n1. Display All Records.\n2. Add Record.\n3. Amend Record.\n4. Delete Record.\n5. Report Menu.\n6. Exit Film Flix.")
        options = input("Enter an option form the Menu screen above: ")
        if options not in ["1","2","3","4","5","6"]:
            print(f"{options} not a valid option!")
    return options

#(title, year released, rating, duration, genre)
"Report Menu"
def reportMenu():
    reportOptions = 0 # local variable with a value 0
    while reportOptions not in ["1","2","3","4","5", "6", "7"]:
        print("Report Menu: \nEnter to Display By\n1. All Films.\n2. Title.\n3. Year Release.\n4. Rating.\n5. Duration.\n6. Genre.\n7. Exit Reports Menu")
        #re-assign the value of the options variable
        reportOptions = input("Enter an option from the Report Menu choices above: ") # defualt datatype for input is string
        if reportOptions not in ["1","2","3","4","5", "6", "7"]:
            print(f"{reportOptions} not a valid choice!")
    return reportOptions


def films():
    "Main"
    mainOption = True # asigning mainOption a variable True as boolean
    # while True
    while mainOption:
        options = menuOptions()
        if options == "1":
            read() # calling the read function from the printRecords.py file
        elif options == "2":
            insertRecord()
        elif options == "3":
            amend()
        elif options == "4":
            delete()
        elif options == "5":
            report = True
            while report:
                reportOptions = reportMenu()
                if reportOptions == "1":
                    reports.allFilms()
                elif reportOptions == "2":
                    reports.title()
                elif reportOptions == "3":
                    reports.year()
                elif reportOptions == "4":
                    reports.rating()
                elif reportOptions == "5":
                    reports.duration()
                elif reportOptions == "6":
                    reports.genre()
                else:
                    report = False
                    input("Press Enter to exit the Report Menu: ")
        else:
            mainOption = False
    input("Press Enter to exit the Film Flix: ")
    return mainOption

if __name__ == "__main__":
    films()


