class ClassName:
    """
    A template for a class
    """
    def __init__(self, var1, var2):
        """
        The init method is called whenever we create a class instance
        When we call ClassName(var1, var2), this __init__ method is being called.
        @param var1: a variable you want the class to possess
        @param var2: ^^
        """
        # Create and assign the class attributes
        # you can access attributes through: instance.var1, instance.var2, instance.list
        self.var1 = var1
        self.var2 = var2
        self.list = []

    def method1(self):
        """
        A method is a function that is called on a specific class instance
        You call a method throough: instace.method1()
        @return:
        """

    def __str__(self):
        """
        You can override the Object Class's string method, so that whenever
        we call str(instance), print(instance) etc, it will deal with the string
        that you return in this function
        @return:str in human readable form
        """
        return "Class Template"

    def __eq__(self, other):
        """
        Now, if we have 2 instances, instance1 & instance2, we can compare them
        based on any variable we want.
        This method is called whenever we call "==" on two instances.

        @return: True if these instances are equivalent, False otherwise
        """
        return self.var2 == other.var2





