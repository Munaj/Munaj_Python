
given_set =[1,2,3]

def compute_all_subset(arr):
    all_subset = []
    all_subset.append([])
    for item in arr:
        all_subset_length = len(all_subset)
        for i in range(0,all_subset_length):
            temp = all_subset[i].copy()
            temp.append(item)
            all_subset.append(temp)
    return all_subset

print(compute_all_subset(given_set))