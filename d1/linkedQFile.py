class LinkedQ:
    def __init__(self, value = None):
        self.first = value
        self.last = None

    def dequeue(self):
        fist = self.first
        self.first = None
        return first

    def enqueue(self, number):
        taken = self.first
        if not taken:
            self.first = number
        else:
            self.last = number

    def isEmpty(self):
        taken = self.first and self.first
        return not taken

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


def basictest():
    q = LinkedQ()
    print(q.isEmpty())

    q1 = Node(2)
    q.enqueue(q1.value)
    q2 = Node(3)
    q3 = Node(1)
    q.enqueue(q3.value)



    print(q.first, q.last)

if __name__ == "__main__":
    basictest()
