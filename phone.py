from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to have access to all attributes / methods of parent
        super().__init__(
            name, price, quantity
        )

        # run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # assign to self object
        self.broken_phones = broken_phones