class Person:

    def __init__(self):
        self.next = None
        self.whoami = ""

    def introduce_my_self(self):
        print("My name is ", self.whoami)

class QL:

    def __init__(self):
        self.head = None

    def print_queue(self):

        someone = self.head

        while someone != None:
            someone.introduce_my_self()
            someone = someone.next

    def is_empty(self):
        return self.head == None
    
    def enqueue(self, someone):

        if self.head == None:
            self.head = someone
        else:
            temp_person = self.head

            while temp_person.next != None :
                temp_person = temp_person.next
            
            temp_person.next = someone
            someone.next = None
    def dequeue(self):
        if self.is_empty():
            print("Nothing to deuque")
            
        else:
            person_going_out = self.head 
            self.head = self.head.next 
            person_going_out.next = None  

            return person_going_out