inp=input("enter your sample \n for e.g 1,45,6,7,4 \n")
#sample_size=int(input("enter your sample size"))

#appending the elements of input in lis
lis=inp.split(",")
lis_int=[]

for numbers in lis:
    lis_int.append(int(numbers))
lis2=lis_int[:]
final_lis=[]
x=0



for num1 in lis_int:
    for num2 in lis2:
        if num1!=num2:
            x += 1
            sample = (num1, num2)
            # final_lis.append(sample)

            # calculate mean
            m = round(sum(sample) / len(sample), 2)

            # calculate variance using a list comprehension
            var_res = round(sum([(xi - m) ** 2 for xi in sample]) / len(sample), 2)
            # apending the final reults in the tuple for e.g
            # (1,2,3) , mean ,variance
            tup = (x, sample, m, var_res)
            final_lis.append(tup)

            print(tup)
        else:
            continue

