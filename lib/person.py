#!/usr/bin/env python3

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def birthday(self):
        """Increase person's age by 1."""
        self.age += 1

    def greet(self):
        """Print a friendly greeting."""
        print(f"Hello! My name is {self.name}.")
