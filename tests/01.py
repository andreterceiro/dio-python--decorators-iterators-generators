def summer(a, b):
    return a + b

def subtractor(a, b):
    return a - b

def caller(operation):
    if operation == "+":
        return summer
    else:
        return subtractor
    
print(caller("+")(3, 1)) #4