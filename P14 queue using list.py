import queue



def display_queue(q):
    print("Queue elements are:", end=" ")


    while not q.empty():
        element = q.get()
        print(element, end=" ")
    print('\n Queue size after REMOVE is', q.qsize())




q = queue.Queue()




q.put(10)
q.put(20)
q.put(30)
print('Queue size after INSERT is',q.qsize())



display_queue(q)
