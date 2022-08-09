from datetime import datetime

JULY = 7


class UserDataSingleton:
    # dunder vars are similar to private vars but aren't completely private
    __instance = None

    name = "Alex"
    date_of_birth = datetime(2004, JULY, 23)

    @staticmethod
    def getInstance():
        """ Static access method. """
        if UserDataSingleton.__instance == None:
            UserDataSingleton()
        return UserDataSingleton.__instance

    def __init__(self):
        if UserDataSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            UserDataSingleton.__instance = self

    def __str__(self) -> str:
        return f"Name: {self.name} Date Of Birth: {self.date_of_birth}"


s = UserDataSingleton.getInstance()
print(s)

s = UserDataSingleton.getInstance()
print(s)
