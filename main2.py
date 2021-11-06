from os import lseek, terminal_size
from pickle import*
from typing import Type


evax = {
    "cin":"",
    "name":"",
    "LastName":"",
    "sex":"",
    "age":0,
    "phone":0,
    "verif":"",
}






def new():
    with open("data.dat","ab") as data:
        evax['cin'] = input('enter a CIN: ')
        ListNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ListAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        test = True
        for i in range(0,len(evax['cin'])):
            if (evax['cin'][i] not in ListNum):
                test = False

        while test == False or len(evax['cin']) != 8:
            evax['cin'] = input('enter a CIN pls: ')
            test = True
            for i in range(0,len(evax['cin'])):
                if (evax['cin'][i] not in ListNum):
                    test = False


        evax['name'] = input("enter your name: ")
        testalpha = True
        # testexist = False
        # with open("data.dat","rb") as data:
        #     for i in range (0,int(x)):
        #         module = load(data)
        #         if evax['name'] == module['name']:
        #             testexist = True
        for i in range(0,len(evax['name'])):
            if evax['name'][i] not in ListAlpha:
                testalpha = False
        
        while testalpha == False or (len(evax['name'])>10 or len(evax['name'])==0):
            evax['name'] = input("enter your name pls: ")
            testalpha = True
            # testexist = False
            # with open("data.dat","rb") as data:
            #     for i in range (0,int(x)):
            #         module = load(data)
            #         if evax['name'] == module['name']:
            #             testexist = False
            for i in range(0,len(evax['name'])):
                if evax['name'][i] not in ListAlpha:
                    testalpha = False

        evax['LastName'] = input("enter your lastname: ")
        testalpha = True
        for i in range(0,len(evax['LastName'])):
            if evax['LastName'][i] not in ListAlpha:
                testalpha = False
        
        while testalpha == False or (len(evax['LastName'])>10 or len(evax['LastName'])==0):
            evax['LastName'] = input("enter your lastname pls: ")
            testalpha = True
            for i in range(0,len(evax['LastName'])):
                if evax['LastName'][i] not in ListAlpha:
                    testalpha = False

        evax['sex'] = input("enter gender:")
        while evax['sex'].upper() != "M" and evax['sex'].upper()  != "F":
            evax['sex'] = input("enter gender pls:")

        evax['age'] = int(input("enter age:"))
        while evax['age'] < 18:
            evax['age'] = int(input("enter age pls:"))

        evax['phone'] = input('enter a phone: ')
        testj = True
        for i in range(0,len(evax['phone'])):
            if (evax['phone'][i] not in ListNum):
                testj = False

        while testj == False or len(evax['phone']) != 8:
            evax['phone'] = input('enter a phone pls: ')
            testj = True
            for i in range(0,len(evax['phone'])):
                if (evax['phone'][i] not in ListNum):
                    testj = False

        evax['verif'] = input("are you infected :")
        while evax['verif'].upper() != "O" and evax['verif'].upper()  != "N":
            evax['verif'] = input("are you infected pls:")
    
        dump(evax,data)


def numberOf(evax,x):
    with open("data.dat","rb") as data:
        male = 0
        female = 0
        for i in range (0,int(x)):
            inv = load(data)
            if inv["sex"].upper() == "M":
                male = male + 1
            else:
                female = female + 1
        
        print(male)
        print(female)
        

print("---------------------------------------------")

def orderAge(x):
    T = []
    with open("data.dat","rb") as data:
        for i in range (0,int(x)):
            T.append(load(data))
    print(T)

    test = True
    while test == True:
        test = False
        for i in range(0,int(x)-1):
            if T[i]["age"] > T[i+1]["age"]:
                aux = T[i]
                T[i] = T[i+1]
                T[i+1] = aux
                test = True

    print(T)

    for i in range(0,int(x)):
        with open ("file.dat","ab") as file:
            dump(T[i],file)

        


def infected(x):
    J = []
    with open ("file.dat","rb") as file:
        for i in range(0,int(x)):
            J.append(load(file))
    print(J)
    with open ("file.txt","a") as file:
        for i in range(0,int(x)):
            if J[i]["verif"].upper() == 'O':
                file.write(J[i]["cin"]+"#"+J[i]["name"]+"#"+str(J[i]["age"])+"\n")

    

        



# CALL FOR ALL FUNCTIONS


choice = int(input("""
    1_Nouveau citoyen  
    2_Nombre de citoyens enregistrés dans le système Evax
    3_Affichage des citoyens enregistrés par ordre décroissant de l'âge 
    4_Archivage des citoyens qui ont attrapé le virus
    5_Quitter le système 
"""))

if choice == 1:
    with open("count.txt","r") as count:
        x = count.read()
        new()
        y = int(x) + 1
        with open("count.txt","w") as count:
            count.write(str(y))
elif choice == 2:
    with open("count.txt","r") as count:
        x = count.read()
        numberOf(evax,x)
elif choice == 3:
    with open("count.txt","r") as count:
        x = count.read()
        orderAge(x)
elif choice == 4:
        with open("count.txt","r") as count:
            x = count.read()
            infected(x)
else:
    print("Good by")

while choice != 5:

    choice = int(input("""
    1_Nouveau citoyen  
    2_Nombre de citoyens enregistrés dans le système Evax
    3_Affichage des citoyens enregistrés par ordre décroissant de l'âge 
    4_Archivage des citoyens qui ont attrapé le virus
    5_Quitter le système 
    """))

    if choice == 1:
        with open("count.txt","r") as count:
            x = count.read()
            new()
            y = int(x) + 1
            with open("count.txt","w") as count:
                count.write(str(y))
    elif choice == 2:
        with open("count.txt","r") as count:
            x = count.read()
            numberOf(evax,x)
    elif choice == 3:
        with open("count.txt","r") as count:
            x = count.read()
            orderAge(x)
    elif choice == 4:
        with open("count.txt","r") as count:
            x = count.read()
            infected(x)
    else:
        print("Good by")







