

class Queue:

    def __init__(self):
        #  define variables you think might be needed
        self.MAXIMUM_SIZE = 4

        self.queue_list = [None for i in range(self.MAXIMUM_SIZE)]

        # self.queue_list = [None for _ in range(self.MAXIMUM_SIZE)]
        """
            or 
            self.queue_list = []
            for i in range(self.MAXIMUM_SIZE):
                self.queue_list.append(None)
        """
        self.front = 0
        self.back = 0


    def enqueue(self, item_to_add):
        if self.back >= 0 and self.back < len(self.queue_list):
            self.queue_list[self.back] = item_to_add
            self.back += 1
        else:
            print("queue cannot take more")
    
    def dequeue(self):
        if self.front >= 0 and self.front <= self.back:
            item_to_dequeue = self.queue_list[self.front]
            self.front +=1 
            return item_to_dequeue
        else:
            print("Cannot happen")
    def size_of_queue(self):
        s = 0
        for i in range(self.front, self.back+1):
            s += 1
        return s
    

