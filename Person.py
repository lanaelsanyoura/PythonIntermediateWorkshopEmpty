from datetime import date, datetime #for date

class Person:
    """
    A person class

    ==== Attributes ====
    firstname: str
    lastname: str
    birthdate: date YEAR, MONTH, DAY
    address: str
    """

    def __init__(self):
        """
        Initialize our class instance
        @return:
        """
        pass

    def __str__(self):
        """
        Return the string in a human-readable manner, only print the
        first and last name
        @return: string
        """
        pass

    def age(self):
        """
        Given the current date, return the age of this person
        :return: int age
        """
        pass


    def getInfo(self):
        """
        Return the information of this user to showcase overriding
        :return:
        """
        pass

# Example Build
#person = Person("Joane", "Do", date(1997, 4, 20), "50 st george str")

