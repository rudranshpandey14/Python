#Check whether quadratic equation has real or imaginary roots
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = b*b - 4*a*c

if d > 0:
    print("Roots are real and distinct")
elif d == 0:
    print("Roots are real and equal")
else:
    print("Roots are imaginary")

