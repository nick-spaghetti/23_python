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
