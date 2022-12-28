#Common Algorithms.


#GCD, Greatest Common Denominator

def gcd(a,b):
    while b !=0:
        temp = a
        a = b
        b = temp%b
    return a

print(gcd(36,8))

#Algorithm performance
#Big O notation
"""
O(1) - constant time, e.g. for looking up a single element in an array
O(log n) - Logarithmic, find an item in a sorted array with binary search
O(n) - Linear time, for example, searching an unsorted array for a specific value
O(nlog n), Log-Linear, complex sorting algorithm like heap sort and merge sort.
O(n^2), Quadratic, Sorting algorithms, such as bubble sort, selection sort and insertion sort

"""


#Sorting algorithms
#- Bubble sort. Performance O(n^2)

#bubble sort
def bubblesort(dataset):
    for i in range(len(dataset) -1, 0,-1): # countdown
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
    return dataset
dataset =[10,22,1,4,16,7]

print(bubblesort(dataset))
        
#Sorting algorithms
#- merge sort. Performance O(nlogn), divide and conquer method

#merge sort
dataset =[10,22,1,4,16,7,12,42]
def mergesort(dataset):
    if len(dataset) >1:
        mid = len(dataset) //2
        left = dataset[mid:]
        right = dataset[:mid]

        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                dataset[k] = left[i]
                i+=1
            else:
                dataset[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            dataset[k]= left[i]
            i+=1
            k+=1

        while j < len(right):
            dataset[k] = right[j]
            j+=1
            k+=1
    return dataset
print(mergesort(dataset))
