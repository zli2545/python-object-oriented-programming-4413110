# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


from typing import Any


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        # if "price" is retrived, the results should be calculated with discount
        if (name == "price"):
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)
        # this's to say: when retriving, not retrieve directly, but just return the 
        # value of that attribute

    # TODO: __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value):
        if (name == "price"):
            if type(value) is not float:
                raise ValueError("The 'price' attribute must be a float")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    # this is called only when the `__getattr__` is not defined
    # or when the attribute being called to set/get is NOT YET existing
    # ATTENTION: NOT to duplicate a `__getattriubte__` here, else will be trouble
    def __getattr__(self, name):
        return f"{name} is not here!"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# TEST
b1.price = 38.95    # here we're retrieving the "price"
print(b1)

# b1.price = 40   # this is not float   #
# one way is to force it to be a float
b1.price = float(40)
print(b1)

print(b1.randomprop)

