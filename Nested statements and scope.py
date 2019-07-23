"""
Nested statements and scope

variables are local to function.

Python will first look out for local values , if not found m, will reach to global level
"""


x = 50

def num():
    global x
    x = 100
    print(x)

    def anothernum():
        global x
        x = 200
        print(x)
    anothernum()

num()
print(x)      ### This will have now the x value as 200











