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

#break is used
#continue is to 

#nesting values
