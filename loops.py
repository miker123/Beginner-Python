#!/usr/bin/env python

#this will help with understanding basic loop structures.

#for loops
print("\nFor Loop Output:")
#loop through strings and print them out
words=["Apple","Asus", "Dell", "Samsung"]
for w in words:
	print(w)

#loop through variables in the range of 1 to 10
for i in range(1,10):
	print(i)

print("\nWhile loop output:")
#while loop to print all the brands
brands=["Apple", "Asus", "Dell", "Samsung"]
i=0
while i<len(brands):
	print(brands[i])
	i = i+1

print("\nIf Statement Output:")
#if/else loop. If True, then do X. Else do Y
if(1==2):
	print("True")
elif(2==1): #else if Used when wanting to see if the value is one of a few values
	print("Also True")
else:
	print("Caught")

#nesting values are loops inside loops. Like inception of loops. Loopception??	
i = 1
while(i < 10):
   j = 0
   while(j <= i):	
	print (j)
	
print("\nExample of a break statement:")
#break is used to terminates a loop statement and transfers execution to the statement immediately following the loop.
for letter in 'Python':  
   if letter == 'h':
      break
   else:
      print ('Current Letter :', letter)

#continue can be used in for and while loops. 
#When used, continue rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
for letter in 'Python': 
   if letter == 'h':
      continue
   print ('Current Letter :', letter)

#pass is used when a statement is required syntactically but you do not want any command or code to execute.
#null operation and nothing occurs when it runs
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

