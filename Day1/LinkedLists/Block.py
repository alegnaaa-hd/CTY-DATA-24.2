import uuid
from datetime import datetime
class Block:

  def __init__(self, balance:float,owner_first_name:str, owner_last_name:str, previous_block_hash):
    self.__blockID = str(uuid.uuid1())
    self.__balance = balance
    self.__hash = None
    self.__created_at = str(datetime.now())
    self.__owner_first_name = str(owner_first_name)
    self.__owner_last_name = str(owner_last_name)
    self.__previous_block_hash = str(previous_block_hash)
    self.next = None
    self.setHash()

  
  def setHash(self):
    # This function can only run once. 
    # It runs the first time the Block is initialized
    # It computes a hash of everything in the block and saves it once.
    if self.__hash == None:
       self.__hash = str(hash(str(self.__blockID)+ str(self.__balance) + str(self.__created_at) + str(self.__owner_first_name) + str(self.__owner_last_name) + self.__previous_block_hash))

  def getHash(self):
        return self.__hash
  # Will compute the new hash and check if it is valid
  def check_block_hash_is_valid(self):
     current_hash = self.getHash()
     computed_hash = str(hash(str(self.__blockID) + str(self.__balance) + str(self.__created_at) + str(self.__owner_first_name) + str(self.__owner_last_name) + self.__previous_block_hash))
     if current_hash == computed_hash:
        return True
     return False
     
  def toString(self):
      print("-------------------------")
      print("BlockID: ",self.__blockID)
      print("Block Hash: ",self.__hash)
      print("Created At: ",self.__created_at)
      print("Owner's infos : ",self.__owner_first_name, " ", self.__owner_last_name )
      print("Previous Block's Hash: ",self.__previous_block_hash )
      print("-------------------------")
      

    
    
