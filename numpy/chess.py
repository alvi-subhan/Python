import numpy as np

#b=8*8 matrix with all the values zero
b=np.zeros(64,dtype="uint32").reshape(8,8)

#replacing alternative coloumns with 1
b[:,::2]=1

#a is the last column
a=b[:,-1].reshape(8,1)

print(b)





