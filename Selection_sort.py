def selection_sort(A):
    for i in range(len(A)):
        min =i
        for j in range(i+1,len(A)):
            if A[j] < A[min]:
                min = j
        temp = A[i]
        A[i] = A[min]
        A[min] = temp
    print(A)
    return A

selection_sort([2,5,1,4,10,7,3])
