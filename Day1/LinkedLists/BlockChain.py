
from Block import Block
class BlockChainAsLinkedList:

    def __init__(self):
        self.head = None

    # Inserts and returns True or false if the new block was inserted
    def insert(self,block: Block):
        if block is None:
            return False
        if block.check_block_hash_is_valid() is False:
            return False
        
        if self.head == None:
            self.head = block 
            self.head.next = None
            return True
        else:
            currentBlock = self.head 
            # loop till the last item of the linked
            # list, then insert the new item after the last item 
            while(currentBlock.next != None):
                currentBlock = currentBlock.next
                if currentBlock.check_block_hash_is_valid() is False:
                    return False
                
            # as from here currentHead has the address to the last item of the list
            currentBlock.next = block
            block.next = None 
            return True
    def item_counts(self): 
        current = self.head 
        count = 0
        while (current != None):
            current = current.next 
            count += 1
        return count

    def display(self):
        currentBlock = self.head
        print("", end="")
        while(currentBlock != None):
            currentBlock.toString()
            currentBlock = currentBlock.next
        print(" NULL \n")

    
