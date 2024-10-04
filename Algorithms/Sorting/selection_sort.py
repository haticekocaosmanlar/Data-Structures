numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array): # O(n^2)
    for i in range(len(array)):
        min = i
        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    return array

print(selectionSort(numbers))