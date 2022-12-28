import math

class Heap():
    def __init__(self):
        self.arr = []
        self.heap_size = 0
        self.root_val = 0

    def max_heapify(self, i , n = "."):
        if n == ".":
            n = self.heap_size
        left = 2*i +1
        right = 2*i +2
        print("i: {}, left: {}, right: {}".format(i,left,right))
        if left < n and self.arr[left]>self.arr[i]:
            largest_val = left
        else:
            largest_val = i
        if right < n and self.arr[right] > self.arr[largest_val]:
            largest_val = right
        if largest_val != i:
            self.arr[i], self.arr[largest_val] = self.arr[largest_val], self.arr[i]
            self.max_heapify(largest_val)
        

    def build_max_heap(self):
        for i in range(len(self.arr)//2, -1,-1):
            self.max_heapify(i)

    def heapsort(self):
        for i in range(self.heap_size, 0, -1):
            self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1]
            self.max_heapify(1, i-1)

    def __call__(self, array):
        if array == None:
            print("Please assign an array to Heap: ")
        else:
            self.arr = array
            self.heap_size = len(self.arr)
    
    def __repr__(self) -> str:
        return str(self.arr)
            

#testing heap

array = Heap()
array([2,14,23,4,8,1,5,7,12])
print(array)
array.build_max_heap()
print(array)