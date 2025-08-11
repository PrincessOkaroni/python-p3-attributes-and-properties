#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Pug", "Dalmatian", "Mutt", "Bulldog"]

    def __init__(self, name=None, breed=None):
        self.name = None
        self.breed = None
        if name is not None:
            self.set_name(name)
        if breed is not None:
            self.set_breed(breed)

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    pass
