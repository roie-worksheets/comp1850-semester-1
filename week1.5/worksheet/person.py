# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, *args) -> None:
        """
        Initializes the Person class with their name and birthday.
        name: str
        birth: date
        """
        if list(map(type, args)) != [str, date]:
            raise TypeError
        elif not args[0]:
            raise ValueError
        [self.name, self.birth] = args;

    def initials(self):
        """
        Returns the initials of the Person's name.
        Transforms "Foo Bar Baz" into "FBB".
        """
        return ''.join(x[0].upper() for x in self.name.split(' '))

    def is_birthday(self):
        """
        Returns whether today's date is the same as
        the person's birthday.
        """
        return self.birth == date(self.birth.year, month=date.today().month, day=date.today().day)
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
