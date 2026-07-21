
front = None
rear = None


def enqueue(data):
    global front, rear

    
    new_node = {
        "prev": None,
        "data": data,
        "next": None
    }

    
    if front is None:
        front = rear = new_node
    else:
        rear["next"] = new_node
        new_node["prev"] = rear
        rear = new_node


def dequeue():
    global front, rear

    if front is None:
        print("Queue Underflow")
        return

    print("Deleted Element:", front["data"])

    front = front["next"]

    if front is None:
        rear = None
    else:
        front["prev"] = None
def display():
    temp = front

    if temp is None:
        print("Queue is Empty")
        return

    print("Queue:", end=" ")

    while temp is not None:
        print(temp["data"], end=" ")
        temp = temp["next"]

    print()
enqueue(10)
enqueue(20)
enqueue(30)

display()

dequeue()

display()

enqueue(40)

display()