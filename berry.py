# num = 0
# while num <= 100:
#     print(num)
#     num = num + 10
#     # can also do num += 10

# print('all done')

# # can also break out of loops using 'break'
# while num <= 100:
#     if num == 50:
#         break
#     print(num)
#     num = num + 10
#     # can also do num += 10


# def add_limited_numbers(a, b):
#     """add two numbers, making sure sum caps at 100"""
#     # if this required explanation, comment like this
#     sum = a + b
#     if sum > 100:
#         sum = 100
#     return sum


# def get_letter(ltr):
#     morse_lookup = {
#         'a': '.-', 'b': '-...', 'c': '-.-', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-,''w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
#     }


# return morse_lookup.get(ltr.upper(), '')

from random import randint
import math


def bounded_avg(nums):
    """
    returns average of list of nums (nums must be between 1-100)
    >>> bounded_avg([2, 4, 6])
    4.0
    >>> bounded_avg([10, 20, 30, 40, 50])
    30.0
    >>> bounded_avg([2, 4, 500])
    Traceback (most recent call last):
        ...
    ValueError: outside bounds of 1-100
    """
    for n in nums:
        if n < 1 or n > 100:
            raise ValueError('outside bounds of 1-100')
    return sum(nums) / len(nums)


class Triangle:
    # right triangle
    def __init__(self, a, b):
        # create triangle from a + b sides
        self.a = a
        self.b = b

    @ classmethod
    def random(cls):
        return cls(randint(1, 20), randint(1, 20))

    def get_hypotenuse(self):
        # get hypotenuse (length of 3rd side)
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        # get area of triangle
        return (self.a * self.b) / 2

    def describe(self):
        return f"my area is {self.get_area()}"


class Triangle:
    """
    a class used to represent a right triangle
    attributes
    ------------
    a: int
        length of side a
    b: int
        length of side b
    """

    def __repr__(self):
        return f"Triangle a={self.a} b={self.b}"

    def __init__(self, a, b):
        # create triangle from a + b sides
        self.a = a
        self.b = b

    @ classmethod
    def random(cls):
        "class method which returns triangle with random sides"
        return cls(randint(1, 20), randint(1, 20))

    def get_hypotenuse(self):
        "calculates hypotenuse (3rd side of right triangle)"
        # get hypotenuse (length of 3rd side)
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def get_area(self):
        'calculates area of right triangle'
        # get area of triangle
        return (self.a * self.b) / 2

    def describe(self):
        return f"my area is {self.get_area()}"
