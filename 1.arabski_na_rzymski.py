war_pocz = int(input("Podaj liczbe do translacji na alfabet rzymski: "))
lista = [1000,900,500,400,100,90,50,40,10,9,5,4,1,0]
litery = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}


wynik = ""

def arab_na_rzym(war,i):
    if war >= lista[i]:
        war = war-lista[i]
        global wynik
        wynik += litery[lista[i]]
        return arab_na_rzym(war,i)
    elif war == 0:
        return
    else:       
        return arab_na_rzym(war,i+1)

arab_na_rzym(war_pocz,0)
print(wynik)
