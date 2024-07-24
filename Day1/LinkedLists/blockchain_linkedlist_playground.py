from BlockChain import BlockChainAsLinkedList
from Block import Block


def main():
    ledger = BlockChainAsLinkedList()
    # balance:float,owner_first_name:str, owner_last_name:str, previous_block_hash
   
    print("We currently store ",ledger.item_counts()," transactions in the ledger")
    FINISHED = False
    user_choice = ""

    
    ADD = "add"
    DISPLAY = "display"
    EXIT = "exit"
    COMMAND = ""
    previous_hash = 0
    while(not(FINISHED)):
        print("1 Enter ",ADD, "to add a new block toyour block chain")
        print("2 Enter ",DISPLAY, "to display all the transactons in the ledger ")
        COMMAND = str(input("Make a choice: ")).lower()
        if COMMAND == EXIT:
            FINISHED = True
            break
        elif COMMAND == ADD:
            amount = float(input("Transaction amount: "))  
            owner_first_name = input("Block Owner First Name: ")  
            owner_last_name = input("Block Owner Last Name: ")
            new_block = Block(amount, owner_first_name, owner_last_name, previous_hash)
            previous_hash = new_block.getHash()
            ledger.insert(new_block)
        elif COMMAND == DISPLAY:
            ledger.display()
        else:
            print("We do not recognize the choice you made")

    


main()