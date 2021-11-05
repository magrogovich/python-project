from pickle import*

evax = {
    "cin":"",
    "name":""
}
with open("sex.dat","ab") as file:
    for i in range(0,3):
        evax["cin"] = input('enter a number')
        evax["name"] = input('enter a name')
        dump(f"{evax}",file)



with open("sex.dat","rb") as file:
    sex = loads(file)
    print(sex)
