#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  # Use the property setter for initial assignment
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def wear(self):
        self.condition = "Worn"
        print("Your shoe is now {}.".format(self.condition))

    def repair(self):
        self.condition = "Used"
        print("Your shoe is now {}.".format(self.condition))
