def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, operation):
    return operation(num)

value = int(input("Enter a value:"))
result1 = operate(value, square)
result2 = operate(value, cube)

print(result1)
print(result2)