#Data Strucutre - List of tuples(First: Song, Second: Times Played)

#Quick Sort for Descending Order
def QuickSort(inputList, low, high):
    
    if low < high:
        pivot = Partition(inputList, low, high)
        QuickSort(inputList, low, pivot - 1)
        QuickSort(inputList, pivot + 1, high)

#Code based on Slide 123: Sorting
def Partition(inputList, low, high):

    pivot = inputList[low][0]
    up = low
    down = high

    while up < down:

        for i in range(up, high):
            if inputList[up][0] < pivot: 
                break
            up += 1

        for i in range(high, low, -1):
            if inputList[down][0] > pivot:
                break
            down -= 1
        
        if up < down:
            inputList[up], inputList[down] = inputList[down], inputList[up]

    #Swaps 
    inputList[low], inputList[down] = inputList[down], inputList[low]

    return down

#Merge Sort for Descending Order
def MergeSort(inputList, left, right):
    if (left < right):
        middle = left + (right - left) // 2

        MergeSort(inputList, left, middle)
        MergeSort(inputList, middle + 1, right)
        Merge(inputList, left, middle, right)

#Code based on slide 90: Sorting slides
def Merge(inputList, left, middle, right):
    #Create sub 'array'
    size1 = middle - left + 1
    size2 = right - middle

    subL = [0] * size1
    subR = [0] * size2

    #Add items into sub 'arrays'
    for i in range(0, size1):
        subL[i] = inputList[left + i]
    for j in range(0, size2):
        subR[j] = inputList[middle + 1 + j]

    #Merge subL and subR
    i = 0
    j = 0 
    k = left

    while i < size1 and j < size2:
        if subL[i][0] >= subR[j][0]:
            inputList[k] = subL[i]
            i += 1
        else:
            inputList[k] = subR[j]
            j += 1
        k +=1
    
    #Fill in the rest of the list when subL or subR become empty
    while i < size1:
        inputList[k] = subL[i]
        i += 1
        k += 1
    
    while j < size2:
        inputList[k] = subR[j]
        j += 1
        k += 1





