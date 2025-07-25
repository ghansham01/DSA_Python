a = 4
# pattern Questions that for logical thinking

# Question No. 1 Rectangular Star Pattern

# def Rectangular_Star_Pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end="")
        # print()

# print(Rectangular_Star_Pattern(a))

# Question No.2 tringle pattern

# def Tringle_Pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print('*', end='')
#         print()

# print("tringle pattern:",Tringle_Pattern(a))

# Question No.3 tringle number pattern 1

# def Triangle_Pattern1(n):
#     for i in range(1, n + 1): 
#         for j in range(1, i + 1):
#             print(j, end=' ')
#         print()  

# print("tringle number pattern:",Triangle_Pattern1(a))

# Question No.4 tringle number pattern 2

# def Tringle_Pattern2(n):
#     for i in range(n):
#         for j in range(i):
#             print(i, end='')
#         print()

# print("tringle number pattern 2:",Tringle_Pattern2(a))

# Quesrion No.5 reverse treingle pattern 

# def reverse_treiangle(n):

#     for i in range(n,0,-1):
#         for j in range(i):
#             print('*', end='')
#         print()


# print("reverse triangle pattern:")
# reverse_treiangle(a)

# Qustion No.6 reverse number treangle
# def reverse_number(n):

#     for i in range(n,0,-1):
#         for j in range(i):
#             print(i,end="")
#         print()

# print('reverser number triangle pattern:')
# reverse_number(a)

# Qustion No.7 star tringle 
def tringle1(n):
    for i in range(0, n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        
        print()
        
# print('traingle is this \n')
tringle1(a)

# Qustion No.8 star tringle 
def tringle2(n):
    for i in range(0, n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        
        print()
        

# print('traingle is this \n')
tringle2(a)