print("enter amount in this format (D 267 for deposit) and (W 500 for withdrawl) /n and enter q when you are done")

q_flag=True

#def parsing_input():

dic={"deposit":0,"withdrawl":0}
while q_flag:
    inp=input("/n enter transaction ")
    if inp== "q":
        break
    if inp.startswith("d") or inp.startswith("D"):
        x=inp.split(" ")
        dic["deposit"]+=int(x[1])
    elif inp.startswith("w") or inp.startswith("W"):
        y=inp.split(" ")
        dic["withdrawl"]+=int(y[1])

Net_amount= dic["deposit"]-dic["withdrawl"]

print (Net_amount)

