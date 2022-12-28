def quicksort(A, p, r): #takes in an array, the first index and last index
    if p<r:
        #partition the array 
        
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1,r)

        #quicksort left
        #quicksort right

def partition(A, p, r):
    x = A[p] #pivot value
    i = p
    j = r + 1
    while i<j:
        while A[i] < x or i<r:
            i +=1
        while A[j]> x:
            j -=1
        temp = A[j]
        A[j] = A[i]
        A[i] = temp

    temp = A[j]
    A[j] = A[i]
    A[i] = temp

    temp = A[j]
    A[j] = A[p]
    A[p] = temp

    return j

quicksort([1,4,2,16,76,24,19],0,6)