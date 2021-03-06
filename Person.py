from datetime import date, datetime  # for date


class Person:
    """
    A person class

    ==== Attributes ====
    firstname: str
    lastname: str
    birthdate: date YEAR, MONTH, DAY
    address: str
    """

    def __init__(self, firstname, lastname, birthdate, address):
        """
        Initialize our class instance
        @return:
        """
        # self.firstname = ...
        # self.lastname = ...
        # self.birthdate = ...
        # self.address = ...
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
        HINT: date.today() returns the date from today
        :return: int age
        """
        pass

    def getInfo(self):
        """
        Return the string "I am a person"
        :return:
        """
        return "I am a person"


if __name__ == '__main__':
    # Example Build
    # person = Person("Joane", "Do", date(1997, 4, 20), "50 st george str")
    # print(person)
    pass