N = int(input("enter the number"))

def lefttriangle(n):
    for i in range(n):
        print('*'*(i+1))

lefttriangle(N)

def rightTriangle(n):
    for i in range(1, n+1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(i):
            print("*", end="")
        print()

print(" right triangle pattern: ")
rightTriangle(N)


def pyramidTriangle(n):
    for i in range(n):
        print(" " * (n-i) + "*" * (2*i-1))

print(" pyramid triangle pattern: ")
pyramidTriangle(N)


def InvertedTriangle(n):
    for i in range(n):
        print("*" * (n-i))

print(" Inverted triangle pattern: ")
InvertedTriangle(N)