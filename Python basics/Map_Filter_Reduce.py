from functools import reduce

nums = [4,2,9,4,7,5,9,4,2,5,6,7,4,21,3]

def is_even(num):
    return num % 2 == 0

evens = list(filter(is_even, nums))
doubles = list(map(lambda  num: num * 2,evens ))
sum = reduce(lambda a,b: a+b, evens)
print(evens)
print(doubles)
print(sum)

odds = list(filter(lambda num: num % 2 == 1, nums))
print(odds)