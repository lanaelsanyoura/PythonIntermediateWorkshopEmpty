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
        # super().__init__(...)
        # self.email = ...
        # self.workshops = ...
        pass # todo remove this pass
    def sign_up(self, workshop):
        """
        Add a workshop to our list if there's no conflict with the one's we've
        already signed up for
        Return True if a workshop was added, and False otherwise
        @param workshop: Workshop we are attending
        @return: True if there is no conflict, False otherwise
        """
        # if this workshop conflicts with existing ones, return False
        # else add the workshop and return True

    def cancel(self, workshop):
        """
        Remove the workshop from our list, and remove ourselves from their list
        @param workshop: Workshop instance
        @return: Nothing
        """


    def __str__(self):
        """
        Return the string of the name of this attendee and all the workshops, using super()
        they are attending
        @return: string
        """


    def getInfo(self):
        """
        Return the string "I am an attendee"
        :return:
        """
        return "I am an attendee"


if __name__ == '__main__':
    # Example Build
    # attendee = Attendee("Lana", "Sanyoura", date(1997, 10, 23), "223", "lsa@gmail.com")
    pass