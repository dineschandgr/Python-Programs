import pdb

def addition(a, b):
    answer = a + b
    return answer

breakpoint()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)

#python -m pdb pydebugger_test.py from console