inp=input("enter numbers")
x=inp.split(",")

C=50
H=30
lis=[]
for d in x:
    D=int(d)
    square=(2 * C * D)/H
    sqr=square**0.5
    lis.append(round(sqr))
print(lis)