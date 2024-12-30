def addition(*args):
    print(args)
    return sum(args)


print(addition(1,2,3,4,5,6))



min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))