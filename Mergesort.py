import math
def mergesort(A, p, r):
    if p >= r:
        return
    q = math.floor((p + r/2))
    mergesort(A, p ,q)
    mergesort(A, q+1, r)
    merge(A, p, q, r)

def merge(Arr, p, q,r): #sorted arrays A B
    C=[]
    i = 0 #counter for A
    j = 0 #counter for B
    A = Arr[p:q]
    B = Arr[q+1:r]
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
        
    while i<len(A):
        C.append(A[i])
        i+=1

    while j<len(B):
        C.append(B[j])
        j+=1
    return C

#print("Sorted: ", merge([1,2,3,4,5],[2,6,10,12]))
print("Sorted: ", mergesort([1,2,3,4,5,2,6,10,12], 0,len([1,2,3,4,5,2,6,10,12])))