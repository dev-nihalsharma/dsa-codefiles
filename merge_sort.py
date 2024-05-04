def merge(l1,l2):
    combined= []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[j])
            j += 1

    while i < len(l1):
        combined.append(l1[i])
        i += 1

    while j < len(l2):
        combined.append(l2[j])
        j += 1

    return combined

def merge_sort(l):
    """
    Time: BigO(n logn)
    Memory: BigO(n)
    """
    if len(l) == 1:
        return l
    
    mid_index = int(len(l)/2)

    left = merge_sort(l[mid_index:])
    right = merge_sort(l[:mid_index])

    return merge(left,right)


print(merge_sort([10,7,5,6,3,2]))