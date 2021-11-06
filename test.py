from pickle import*
with open("data.dat","rb") as data:
    for i in range(0,5):

        print(load(data))

print("------------------------------------------------------")
with open("file.dat","rb") as file:
    for i in range(0,5):
    
        print(load(file))
