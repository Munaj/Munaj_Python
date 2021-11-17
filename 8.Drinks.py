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

    def __str__(self):
        return f"Nazwa drinku: {self.name} \nCena: {self.price}\nPercent: {self.percent}\nCapacity: {self.capacity}"

    

wodka = drink("wodka", 8, 40, 50)
rum = drink("rum", 9, 60, 50)
cola = drink("cola", 2, 0, 100)
lod = drink("lod", 0, 0, 30)

print(wodka + cola)



