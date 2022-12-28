#not finished yet
k=4

A = [27,29,35,42,5,15]

#binary tree imagined so that the root node is k

def searchtree(A, k, d): #k the value by which the array has been circuraly shifted by and hence the parent node, d the desired value. A the array.
    i=k
    #base case when its a single leaf node
    if i == len(A)-1: 
        return A[i]

    #if k to large then cycle back to the front
    print(k,A)
    if k>len(A)-1:
        i=0

    #otherwise traverse left or right
    if A[i+1]<d:
        searchtree(A,i+2,d) # right
    else:
        searchtree(A, i+1, d) #left

print(searchtree(A, 4, 27))
