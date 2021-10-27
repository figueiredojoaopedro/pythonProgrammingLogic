#Here we are going to calculate an Area Of Circle that the customer enters the radius
#A = π . R2
# pi = 3.14159

R = float (input ())

pi = 3.14159
# applying the formula:
A = pi * R*R
#using round function as a decimal limiter

round (A, 4) 
print ("A=", A)