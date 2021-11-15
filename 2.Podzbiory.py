
given_set =[1,2,3]

def compute_all_subset(arr):
    allSubset = []
    allSubset.append([])
    for item in arr:
        allSubsetLength = len(allSubset)
        for i in range(0,allSubsetLength):
            temp = allSubset[i].copy()
            temp.append(item)
            allSubset.append(temp)
    return allSubset

print(compute_all_subset(given_set))