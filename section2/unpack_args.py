def multiply(*args):
    result = 1
    for arg in args:
        result*=arg
    return result

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    if operator == "+":
        return sum(args)

print(apply(1,2,3,4,operator="*"))
print(apply(1,2,3,4,operator="+"))