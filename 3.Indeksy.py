zbior = [1,2,3,4,5,6,7,8,9,10]
indeksy =[]
range_of_arr = len(zbior)
item = []
for i in range(0,range_of_arr):
    for j in range(range_of_arr):
        temp = [i,j]
        temp1 =[j,i]
        if(zbior[i]+zbior[j] == 6 ):
            if(temp1 not in  indeksy):
                print(f"Suma liczb o Indeksach {i} i {j} jest równa 6" )
                indeksy.append([i,j])
                print(temp)
print(indeksy)
#it not much but it's honest work