class MyCircularQueue():
    def __init__(self,k):
        self.k=k
        self.queue = [None]*k
        self.head = self.tail = -1

    def enQueue(self,data):
        print(self.head,"-")
        print(self.tail, "-")
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def printQueue(self):
        print("self.head",self.head)
        print("self.tail", self.tail)
        if (self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:

            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            print()

    def deQueue(self):
        if self.head==-1:
            print("There is no element in the circular Queue")
        elif self.head ==self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail =-1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1)%self.k
            return temp


obj = MyCircularQueue(5)

obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
obj.enQueue(5)
print("Initial queue")
obj.printQueue()
obj.deQueue()
print("---------------")
obj.printQueue()
obj.deQueue()
print("---------------")
obj.printQueue()
obj.enQueue(6)
print("---------------")
obj.printQueue()


