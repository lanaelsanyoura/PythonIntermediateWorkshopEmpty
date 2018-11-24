"""
Read the attendees from a CSV file and sign them up for the workshop
"""
import csv
from datetime import date, time
from Person import Person
from Attendee import Attendee
from Workshop import Workshop

# Create workshop
# host = Person(...)
#host = Person("Joane",
#                "Do",
#                date(1997, 4, 20), "50 st george str")
#title = "Intermediate Python"
#desc = "Spruce up your python skills!"
#ws = Workshop(date(2018, 11, 24), datetime(2018, 11, 24, 12,30),
#              datetime(2018, 11, 24, 15, 30), "BA1190", title, desc, host)

with open('attendees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Retrieve the user information
        #birthList = row['birthdate'][1:-1].split('-')
        #birthDate = date(int(birthList[0]), int(birthList[1]), int(birthList[2]))
        #attendee = Attendee(row['firstname'], row['lastname'], date,
        #                   row['address'], row['email'])
        #ws.add_attendees(attendee)
        pass
    #print(ws.get_str_attendees())
