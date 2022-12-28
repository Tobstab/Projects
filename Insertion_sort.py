def insertion_sort(A):
    for i in range(1, len(A)):
        j=i #current value to insert
        while j>0 and A[j] < A[j-1]: # go through numbers to the left and swap if they are bigger
            temp = A[j]
            A[j]= A[j-1]
            A[j-1] = temp
            j-=1
    print(A)
    return A

def dec_insertion_sort(A):
    for i in range(1, len(A)):
        j=i #current value to insert
        while j>0 and A[j] > A[j-1]: # go through numbers to the left and swap if they are bigger
            temp = A[j]
            A[j]= A[j-1]
            A[j-1] = temp
            j-=1
    print(A)
    return A

insertion_sort([2,5,1,4,10,7,3])
dec_insertion_sort([2,5,1,4,10,7,3])