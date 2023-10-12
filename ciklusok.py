
# ciklus bizonyos műveletek ismétlésére való
# ciklisváltozó - számlálja, hogy hányszor futott már le a ciklus
# ciklusmag - ismétlendő utasítások
# ciklusfeltétel - itt adjuk meg, hogy meddig fusson a ciklus

def szamlalos_ciklus1():
     cv:int = 1
     while(cv <= 10): 
        print(f"{cv} Többé nem kések, mert lemaradok fontos információkról!")
        cv += 1

     print(cv, "A cillus után")


def elotesztelos_ciklus():
     ## kérjünk be egy 10-nél nagyobb számot a felhasználótól
     szam: int= int(input("Adjon meg egy 10-nél nagyob számot! "))
     while szam <= 10 :
        print("10-nél nagyobb számot! ")
        szam: int= int(input("Adjon meg egy 10-nél nagyob számot! "))

     print("Hurrá, végre sikerült 10-nél nagyobbat!", szam)


# készíts külön eljárást
# 1. Írd ki a számokat 1 és 10 között a képernyőre egymás mellé
def feladat1():
     cv:int = 1
     while(cv <= 10): 
            print(f"{cv}", end=", ")
            cv += 1

# 2. Írd ki a számokat 20 és 30 között a képernyőre
def feladat2():
     print("\n")
     cv:int = 20
     while(cv <= 30): 
                print(f"{cv}", end=", ")
                cv += 1

# 3. Írd ki a 15 és 25 közötti páros számokat
def feladat3():  
     print("\n")
     cv:int = 16
     while(cv <= 24):
            print(f"{cv}", end=", ")
            cv += 2
    
# 4. Írd ki a számokat egyesével 12 és 30 között fordított sorrendbe
def feladat4():
     print("\n")
     cv:int = 30
     while(cv >= 12):
            print(f"{cv}", end=", ")
            cv -= 1



def vmi():
    print("valami", end=", ")
    print("vége")








