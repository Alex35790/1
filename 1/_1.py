print("Enter a number:") 
num1 = float(input()) 
print("Enter a boundary number:")
boundary = float(input()) 

if num1 < boundary:
    print("The first number is less than the boundary.") 
elif num1 > boundary: 
    print("The first number is greater than the boundary.") 
    if num1 > boundary * 3:
        print("The first number is more than 3 times greater than the boundary.") 