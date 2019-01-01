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
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address

    def __str__(self):
        """
        Return the string in a human-readable manner, only print the
        first and last name
        @return: string
        """
        return str.format("{} {}", self.firstname, self.lastname)

    def age(self):
        """
        Given the current date, return the age of this person
        :return: int age
        """
        today = date.today()
        age = today - self.birthdate
        if today < date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def getInfo(self):
        """
        Return the string "I am a person"
        :return:
        """
        return "I am a person"


if __name__ == '__main__':
    # Example Build
    person = Person("Joane", "Do", date(1997, 4, 20), "50 st george str")
    print(person)
