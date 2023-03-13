queue = []

class node():
    def __init__(self,data ,pointer):
        self.data = data
        self.pointer = pointer

for x in range(10):
    queue.append(node(" " , x+1))
queue[9].pointer = -1

free = 0
end = start = -1

def insert(value):
    global free , start , end
    if free != -1:
        new = free
        free = queue[free].pointer
        queue[new].data = value
        queue[new].pointer = -1

    if end == -1:
        start = new
    else:
        queue[end].pointer = new
    end = new

def out():
    global free , start , end
    current = start
    if start == -1:
        return -1
    else:
        while current != -1:
            print(current , "  ", queue[current].data )
            current = queue[current].pointer

insert('d')
insert('g')
insert('k')
out()