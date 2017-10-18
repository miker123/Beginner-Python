#!/usr/bin/python

a = 21
b = 10
c = 0

#addition
c = a + b
print "Line 1 - Value of c is ", c

#Addition Shortcut. Same as c=c+a
c += a
print "Line 2 - Value of c is ", c 

#Subtraction
c = a - b
print "Line 2 - Value of c is ", c 

c -= a #same as saying c=c-a
print "Line 2 - Value of c is ", c 

#Multiplication
c= a * b 
c *= a
print "Line 3 - Value of c is ", c 

#Division
c = b / a
c /= a 
print "Line 4 - Value of c is ", c 

#Modulus Division
#It takes modulus using two operands and assign the result to left operand
c = b % a
c %= a
print "Line 5 - Value of c is ", c

a = 2
b = 3
#Exponential Power
c = a ** b #Equivalent to c=a^b
c **= a  #Equivalent to c=c^b
print "Line 6 - Value of c is ", c

#Floor Division
a = 10
b = 5
c = a//b 
c //= a
print "Line 7 - Value of c is ", c
