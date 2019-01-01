"""
Read the attendees from a CSV file and sign them up for the workshop
"""
import csv
from datetime import date, time, datetime
from Person import Person
from Attendee import Attendee
from Workshop import Workshop

# Create workshop
 # host = Person(...)

host = Person("Joane",
              "Do",
              date(1997, 4, 20), "50 st george str")
title = "Intermediate Python"
desc = "Spruce up your python skills!"
ws = Workshop(date(2018, 11, 24), datetime(2018, 11, 24, 12, 30),
              datetime(2018, 11, 24, 15, 30), "zoom.com/333", title, desc, host)

with open('attendees.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Retrieve the user information using
        # row['firstname], row['lastname'] ...
        # birthDate = ...
        # attendee = ...
        birthlist = row['birthdate'].split('-')
        birthdate = date(int(birthlist[0]), int(birthlist[1]), int(birthlist[2]))
        attendee = Attendee(row['firstname'], row['lastname'], birthdate, row['address'], row['email'])
        ws.add_attendees(attendee)
    print(ws.get_str_attendees())

if __name__ == '__main__':
    pass