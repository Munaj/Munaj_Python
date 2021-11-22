
class drink:
    def __init__(self, name, price, percent, capacity):
        self.name = name
        self.price = price
        self.percent = percent
        self.capacity = capacity

    def __add__(self, other):
        name = f"{self.name} z {other.name}"
        price = self.price + other.price
        percent_alk = ((self.percent*self.capacity)/100)+((other.percent*other.capacity)/100)
        percent = round(percent_alk/(self.capacity+other.capacity)*100)
        capacity = (self.capacity + other.capacity)
        return drink(name, price, percent, capacity)

    def __mul__(self,other):
        name = f"{other} razy {self.name}"
        price = self.price*other
        percent = self.percent
        capacity = self.capacity*other
        return drink(name, price, percent, capacity)

    def __str__(self):
        return f"Nazwa drinku: {self.name} \nCena: {self.price}\nPercent: {self.percent}\nCapacity: {self.capacity}"
    def __or__(self,other):
        if(self.percent >= other.percent):
            return self,other
        else:
            return other,self
        
    

wodka = drink("wodka", 8, 40, 50)
rum = drink("rum", 9, 60, 50)
cola = drink("cola", 2, 0, 100)
lod = drink("lod", 0, 0, 30)
cytryna = drink("cytryna",1,0,10)
teqilla = drink("teqilla", 9, 50, 50)


drink1 = wodka + cola
drink2 = teqilla *2
drink3 = rum + cytryna


l = [
    drink1,
    drink2,
    drink3,
    wodka,
    cola,
    lod,
    rum,
    cytryna,
    teqilla
]


for i in range(len(l)):
    for j in range(len(l)):
        m,k = (l[i]|l[j])
        l[i] = m
        l[j] = k


for x in l:
    print(F"{x} \n")