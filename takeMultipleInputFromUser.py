#!/usr/bin/env python3

# x,y = str(input("Enter A Two Value: ")).split()

# print("First number is : ", x)
# print("Second number is : ", y)

# a, b, c = input("inter dob : ").split()
# print("your dob is : ",a,"here is b",b)

# a, b = input("Enter two value: ").split()
# print("First number is {} \n Second number is {}".format(a,b))


#taking multiple inputs at a time and casting using list funcions
x = list(map(int, input("Enter multiple value you want : ").split()))
print(x)