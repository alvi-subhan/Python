"""Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
inp=input("enter ")

dic={"letters":0,"numbers":0}
for a in inp:
    if a.isdigit():
        dic["numbers"]+=1
    if a.isalpha():
        dic["letters"]+=1
    else:
        pass
print (dic)