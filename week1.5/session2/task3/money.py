# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        # Add validation code here, to check that
        # - the pounds parameter is an integer
        # - pounds is not negative
        # - the pence parameter is an integer
        # - pence is not negative and not greater than 99
        # Raise appropriate exceptions if any of these are violated
        if not isinstance(pounds, int) or not isinstance(pence, int):
            raise TypeError
        elif pounds < 0 or pence < 0 or pence > 99:
            raise ValueError

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds:02}.{self.pence:02}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        pence = self.pence + other.pence
        
        if pence > 99:
            return Money(self.pounds + other.pounds + 1, pence - 99)

        return Money(self.pounds + other.pounds, self.pence + other.pence)
