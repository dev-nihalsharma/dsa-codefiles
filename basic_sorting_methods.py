# ----- Bubble Sort ------
def bubble_sort(l):
    """
    starts with first element compares it to next if next is smaller, then interchanges position then cursor moves to then next element till biggest element reaches last position
    """

    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

    return l

def selection_sort(l):

    for i in range(len(l) -1):
        min_index = i
        for j in range(i+1,len(l)):
            if l[j] < l[min_index]:
                min_index = j
        temp = l[i]
        l[i] = l[min_index]
        l[min_index] = temp

    return l



# ----- Insertion Sort --------
def insertion_sort(l):
    for i in range(1, len(l)):
        temp = l[i]
        j = i - 1
        while j>=0 and l[j] > temp:
            l[j+1] = l[j]
            l[j] = temp
            j -= 1
        pass
    return l



print(insertion_sort([2,1,6,5,8,3,7,4]))