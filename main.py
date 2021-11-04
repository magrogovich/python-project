from pickle import*

class evax:
    cin = ""
    name = ""
    LastName = ""
    sex = ""
    age = 0
    phone = 0
    verif = ""

citizen = evax





def new():
    with open("data.dat","ab") as data:
        citizen.cin = input('enter a CIN: ')
        ListNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ListAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        test = True
        for i in range(0,len(citizen.cin)):
            if (citizen.cin[i] not in ListNum):
                test = False

        while test == False or len(citizen.cin) != 8:
            citizen.cin = input('enter a CIN pls: ')
            test = True
            for i in range(0,len(citizen.cin)):
                if (citizen.cin[i] not in ListNum):
                    test = False


        citizen.name = input("enter your name: ")
        testalpha = True
        for i in range(0,len(citizen.name)):
            if citizen.name[i] not in ListAlpha:
                testalpha = False
        
        while testalpha == False or (len(citizen.name)>10 or len(citizen.name)==0):
            citizen.name = input("enter your name pls: ")
            testalpha = True
            for i in range(0,len(citizen.name)):
                if citizen.name[i] not in ListAlpha:
                    testalpha = False

        citizen.LastName = input("enter your lastname: ")
        testalpha = True
        for i in range(0,len(citizen.LastName)):
            if citizen.LastName[i] not in ListAlpha:
                testalpha = False
        
        while testalpha == False or (len(citizen.LastName)>10 or len(citizen.LastName)==0):
            citizen.LastName = input("enter your lastname pls: ")
            testalpha = True
            for i in range(0,len(citizen.LastName)):
                if citizen.LastName[i] not in ListAlpha:
                    testalpha = False

        citizen.sex = input("enter gender:")
        while citizen.sex.upper() != "M" and citizen.sex.upper()  != "F":
            citizen.sex = input("enter gender pls:")

        citizen.age = int(input("enter age:"))
        while citizen.age < 18:
            citizen.age = int(input("enter age pls:"))

        citizen.phone = input('enter a phone: ')
        testj = True
        for i in range(0,len(citizen.phone)):
            if (citizen.phone[i] not in ListNum):
                testj = False

        while testj == False or len(citizen.phone) != 8:
            citizen.phone = input('enter a phone pls: ')
            testj = True
            for i in range(0,len(citizen.phone)):
                if (citizen.phone[i] not in ListNum):
                    testj = False

        citizen.verif = input("are you infected :")
        while citizen.verif.upper() != "O" and citizen.verif.upper()  != "N":
            citizen.verif = input("are you infected pls:")
    
        dump(citizen,data)
        with open("data.dat","a") as data:
            data.write('\n')


def numberOf(citizen):
        with open("data.dat","rb") as data:
            print(len(data.readlines())-1)
            male = 0
            female = 0
            for i in range(0,len(data.readlines())-1):
                if citizen.gender.upper() == 'M':
                    male = male + 1
                elif citizen.gender.upper() == 'F':
                    female = female + 1

            print(f"male is {male} and female is {female}")



choice = int(input("""
    1_Nouveau citoyen  
    2_Nombre de citoyens enregistrés dans le système Evax
    3_Affichage des citoyens enregistrés par ordre décroissant de l'âge 
    4_Archivage des citoyens qui ont attrapé le virus
    5_Quitter le système 
"""))

if choice == 1:
    new()
elif choice == 2:
    numberOf(citizen)
elif choice == 3:
    orderAge()
elif choice == 4:
    infected()
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
        new()
    elif choice == 2:
        numberOf(citizen)
    elif choice == 3:
        orderAge()
    elif choice == 4:
        infected()
    else:
        print("Good by")







