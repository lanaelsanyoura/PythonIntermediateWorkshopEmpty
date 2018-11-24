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
    def __init__(self):
        pass

    def sign_up(self, workshop):
        """
        Add a workshop to our list if there's no conflict with the one's we've
        already signed up for
        @param workshop: Workshop we are attending
        @return: True if there is no conflict, False otherwise
        """
        pass

    def cancel(self, workshop):
        """
        Remove the workshop from our list, and remove ourselves from their list
        @param workshop: Workshop instance
        @return: Nothing
        """
        pass

    def __str__(self):
        """
        Return the string of the name of this attendee and all the workshops
        they are attending
        @return: string
        """
        pass

    def getInfo(self):
        """
        Return the information of this user to showcase overriding
        :return:
        """
        pass

# Example Build
# attendee = Attendee("Lana", "Sanyoura", date(1997, 10, 23), "223", "lsa@gmail.com")