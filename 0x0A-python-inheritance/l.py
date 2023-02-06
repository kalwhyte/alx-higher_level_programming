#!/usr/bin/python3

''' Write a function that returns the list of available attributes and methods of an object: '''

class Number :



    # Class Attributes

    one = 'first'

    two = 'second'

    three = 'third'



    def __init__(self, attr):

        self.attr = attr



    def show(self):

        print(self.one, self.two,

                self.three, self.attr)



n = Number(2)
n.show()



# Passing both the object
# and class as  argument
# to the dir method

print('\nBy passing object of class')

print(dir(n))


print('\nBy passing class itself ')

print(dir(Number))
