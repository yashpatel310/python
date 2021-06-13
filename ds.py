#TASK 1
pi = 3.14
radius = float(input("Input the radius of the circle: "))
area = pi*radius*radius
print("The area of circle with radius ",radius," is :",area)


#TASK 2
file_name = input("Input the Filename: ")
extention = '.py'
file_extention = file_name[-3:]
if file_extention == extention:
    print("The extention of file is : 'python'")
else:
    print("The extention of file is not : 'python'")
