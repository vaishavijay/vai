def swap(age1,age2):
    if(age1 > age2):
        yuh = age1
        age1 = age2
        age2 = yuh
    return(age1, age2)

def driver():
    x=int(input("Numero 1 "))
    y=int(input("Numer 2"))
    swap(x,y)
