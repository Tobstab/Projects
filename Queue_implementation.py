class MyQueue:
    def __init__(self):
        self.queue = []
        
    def find(self, val):
        if val in self.queue:
            for i in range(len(self.queue)):
                if self.queue[i]  == val:
                    print("The value exists in position "+str(i))
        print ("Value doesn't exist in the queue")
    
    def enqueue(self, val):
        self.queue.append(val)
        
    def dequeue(self):
        if len(self.queue)<1:
            return "Queue is empty, insert values before dequeuing"
        return self.queue.pop(0)
    
Queue1 = MyQueue()
Queue1.enqueue(5)
Queue1.enqueue(10)
Queue1.enqueue(6)
Queue1.enqueue(8)
Queue1.find(5)
x = Queue1.dequeue()

print(x)

    
