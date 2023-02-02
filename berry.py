num = 0
while num <= 100:
    print(num)
    num = num + 10
    # can also do num += 10

print('all done')

# can also break out of loops using 'break'
while num <= 100:
    if num == 50:
        break
    print(num)
    num = num + 10
    # can also do num += 10


def add_limited_numbers(a, b):
    """add two numbers, making sure sum caps at 100"""
    # if this required explanation, comment like this
    sum = a + b
    if sum > 100:
        sum = 100
    return sum
