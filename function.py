#!/usr/bin/python

# Function definition is here
def printMe( str ):
   newData="test" #Object newData is now local to the printMe function
   global varGlobal=2 #use global to declare a global variable from inside a function
   "This prints a passed string into this function"
   print str
   #Python can return any python object,
   return #returns None as nothing there tp return

#Below is the main program
# Now you can call printme function
str="I'm first call to user defined function!"
printMe(str)
printMe(str)

#fixed parameters-->Interpreter and function will expect that specific number of variables
#def printMe(*str) means that *str is optional (optional parameters)
#def printMe(**kw) are named parameters.
