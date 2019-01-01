from datetime import date

from Person import Person


class Attendee(Person):
    """
    An Attendee Class that can sign up to and cancel workshops

    ==== Attributes ====
    firstname: str
    lastname: str
    birthdate: date, YEAR, MONTH, DAY
    address: str
    email: str
    workshops: list[Workshops]
    """

    def __init__(self, firstname, lastname, birthdate, address, email):
        super().__init__(firstname, lastname, birthdate, address)
        self.email = email
        self.workshops = []

    def sign_up(self, workshop):
        """
        Add a workshop to our list if there's no conflict with the one's we've
        already signed up for
        Return True if a workshop was added, and False otherwise
        @param workshop: Workshop we are attending
        @return: True if there is no conflict, False otherwise
        """
        for w in self.workshops:
            if w.conflicts(workshop):
                return False
        self.workshops.append(workshop)
        return True

    def cancel(self, workshop):
        """
        Remove the workshop from our list, and remove ourselves from their list
        @param workshop: Workshop instance
        @return: Nothing
        """
        self.workshops.remove(workshop)
        workshop.attendees.remove(self)

    def __str__(self):
        """
        Return the string of the name of this attendee and all the workshops
        they are attending
        @return: string
        """
        return super(Attendee, self).__str__() + " " + self.email

    def getInfo(self):
        """
        Return the string "I am an attendee"
        :return:
        """
        return "I am an attendee"


if __name__ == '__main__':
    # Example Build
    attendee = Attendee("Lana", "Sanyoura", date(1997, 10, 23), "223", "lsa@gmail.com")
