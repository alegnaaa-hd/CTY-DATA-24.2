
from basic_linked_list import Person, QL



franklin = Person()

franklin.whoami = "Franklin"

philip = Person()
philip.whoami = "Philip"


data_staff = QL()

data_staff.enqueue(philip)

data_staff.enqueue(franklin)

print(data_staff.print_queue())
first = data_staff.dequeue()
second = data_staff.dequeue()


print("First dequeued should be philip: ")
first.introduce_my_self()
print("Then franklin : ")
second.introduce_my_self()