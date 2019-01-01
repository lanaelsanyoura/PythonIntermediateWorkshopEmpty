from datetime import date, datetime, time

# from Person import Person
# from Attendee import Attendee
from Attendee import Attendee
from Person import Person


class Workshop():
    """
    A class that has attendees and workshop details

    ==== Attributes ====
    date date: year, month, day
    start_time datetime: year, month, day, hour, minutes
    end_time datetime: year, month, day, hour, minutes
    zoom_link str
    attendees list[Attendees]
    host Person
    description str
    title str
    capacity int: max capacity this workshop can handle, default 50

    Constructor: Workshop(date(2018, 11, 24), datetime(2018, 11, 24, 12,30),
              datetime(2018, 11, 24, 3, 30), "zoom.com/333", title, desc, host)
    """

    def __init__(self, date, start_time, end_time, zoom_link, title, description, host,
                 capacity=50):
        # implement assignments
        pass

    def conflicts(self, other):
        """
        Conflicts:
               <-------- -------->
        <---- ----> <-->   <---- ---->
        :param other: the workshop we are testing for conflicts against
        :return: True if these two workshops conflict in time
        """
        pass

    def add_attendees(self, attendee):
        """
        Add attendees to our workshop list only if we have the right capacity
        and add our workshop to their schedule
        Return True if we added them, and False otherwise
        @param attendee:
        @return: True if we signed them up, False otherwise
        """
        pass

    def __str__(self):
        """
        ===== self.title ====
        self.description
        Hosted by: self.host
        self.date: self.start_time --> self.end_time
        Room self.room

        @return:string representation of this workshop
        """
        str = "===== {} ====\n".format(self.title)
        str += self.description + "\n"
        str += "Hosted by: {} \n".format(self.host)
        str += "{}, {} --> {}\n".format(self.date, self.start_time.time(), self.end_time.time())
        str += "Room {}\n".format(self.zoom_link)
        return str

    def get_str_attendees(self):
        """
        Return a list of all our attendees in a string manner
        @return:
        """
        pass


if __name__ == '__main__':
    # example build
    # title = "Intermediate Python"
    #
    # desc = "Spruce up your python skills!"
    # host = Person("Lana",
    #               "El Sanyoura",
    #               date(1997, 4, 20), "50 st george str")
    # ws = Workshop(date(2020, 10, 31), datetime(2020, 10, 31, 12, 30),
    #               datetime(2020, 10, 31, 15, 30), "zoom.com/333", title, desc, host)
    # attendee1 = Attendee("Joane", "Do", date(1997, 4, 20), "50 st george str", "jd@gmail.com")
    # ws.add_attendees(attendee1)
    pass
