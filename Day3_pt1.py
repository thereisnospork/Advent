import numpy as np

input = 325489
sqrt_input = input **.5
def square(x):
    return x*x

odds = range(1,1000,2)
odd_squares = list(map(square, odds))

def bot_right(number, squares):
    for square in squares:
        if square > number:
            return square

bottom_right = bot_right(input,odd_squares)
side_length = bottom_right **.5
center = side_length//2
steps_baseline = side_length-1
steps = steps_baseline

if bottom_right - input <= side_length:
    steps_to_center = abs(input-(bottom_right-center))
steps_from_center = side_length //2

steps = steps_to_center+steps_from_center
print(steps)
#
# print(5//2)
#
# print(steps_to_center)
#
# # print(side_length)
# # print(input-bottom_right)
# # print(bottom_right)
# print(center)