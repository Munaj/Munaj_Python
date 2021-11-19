start_val = int(input("Enter arabic number: "))
list_1 = [1000,900,500,400,100,90,50,40,10,9,5,4,1,0]
rom_lett = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}


result = ""

def arab_to_rom(val,i):
    if val >= list_1[i]:
        val = val-list_1[i]
        global result
        result += rom_lett[list_1[i]]
        return arab_to_rom(val,i)
    elif val == 0:
        return
    else:       
        return arab_to_rom(val,i+1)

arab_to_rom(start_val,0)
print(f"{start_val} Is equal to: {result}")
