#!/usr/bin/python

#The purpose of this is to show how to use exceptions to catch errors
try:
  x="5"
  y="Turtles"
  z = x + y
  print (z)
  
#Used to catch specific errors
except(TypeError,IOError):
  pass

#catch all exceptions. General use
except Exception as err:
  print("Sorry. There has been an error.")
 
 #More Info at http://www.pythonforbeginners.com/error-handling/exception-handling-in-python
