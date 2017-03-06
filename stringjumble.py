"""
stringjumble.py
Author: Earl
Credit: Sam

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

jumble=str(input("Please enter a string of text (the bigger the better): "))
print("You entered " +jumble+ ". Now jumble it:")

print((jumble)[len(jumble)::-1])
lastspace=len(jumble)
for x in range(lastspace-1,-2,-1):
    if jumble[x]==" " or x==-1:
        print(jumble[x+1:lastspace],end=" ")
        lastspace=x
print("")   
lastspace=0
for x in range(0,len(jumble)):
    if jumble[x]==" ":
        if lastspace==0:
            print(jumble[x-1::-1],end=" ")
        else:
            print(jumble[x-1:lastspace:-1],end=" ")
        lastspace=x
    if x>=len(jumble)-1:
        print(jumble[x:lastspace:-1],end=" ")