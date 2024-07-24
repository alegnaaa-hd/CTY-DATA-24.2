from queue import Queue

a = Queue()

print(a.queue_list)

a.enqueue("Hey there!")

print(a.queue_list)
a.enqueue(12.6)
print(a.queue_list)

print(a.dequeue())
print(a.dequeue())

x = a.dequeue()
print(x)