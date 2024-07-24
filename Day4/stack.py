

class  Stack:




    def __init__(self):
        self.count = 0
        self.maximum_size = 4
        self.current_size = 0
        self.data = [0 for i in range(self.maximum_size)]
        self.index_available = 0


    def is_stack_full(self):
        if self.current_size == self.maximum_size:
            return True
        else:
            return False
    
    def is_stack_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False
        
    def push(self, item):
        if self.is_stack_full():
            print("stack is full")
            return
        self.data[self.index_available] = item
        self.index_available += 1 # self.index_available = self.index_available +  1
        self.current_size += 1

    def pop(self):
        if self.is_stack_empty():
            print("Stack is empty. Cannot pop")
        else:
            item_to_pop = self.data[self.index_available-1]
            self.index_available -= 1
            return item_to_pop
        
    def list_content_of_stack(self):

        print("")
        for stack_item in self.data:
            print(stack_item, " " ,end="")

        print("")
        