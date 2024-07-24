

from stack import Stack


first_stack = Stack()

second_stack = Stack()

first_stack.push(3)
first_stack.push(6)
first_stack.push(8)
first_stack.push(9)

first_stack.list_content_of_stack()

second_stack.push(first_stack.pop())
second_stack.push(first_stack.pop())
second_stack.push(first_stack.pop())
second_stack.push(first_stack.pop())

second_stack.list_content_of_stack()