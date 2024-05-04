def swap(l, swap_i, i):
    temp = l[swap_i]
    l[swap_i] = l[i]
    l[i] = temp
    
def pivot(l, pivot_i, end_i):
    swap_i = pivot_i

    for i in range(pivot_i + 1, end_i + 1):
        if l[i] < l[pivot_i]:
            swap_i += 1
            swap(l, swap_i=swap_i, i=i)

    swap(l, swap_i=swap_i, i=pivot_i)

    return swap_i


def quick_sort(l, left, right):
    if left < right:
        pivot_i = pivot(l, left, right)
        quick_sort(l, left, pivot_i-1)
        quick_sort(l, pivot_i+1, right)

    return l

print(quick_sort([4,2,1,6,3,8,5], 0,6))
