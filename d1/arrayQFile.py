class ArrayQ():
    def __init__(self):
        self.list = []

    def enqueue(self, number):
        self.list.append(number)

    def dequeue(self):
        firstNumber = self.list[0]
        self.list.pop(0)
        return firstNumber

    def isEmpty(self):
        isEmpty = len(self.list) == 0
        return isEmpty

def basictest():
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("test OK")
    else:
        print("FAILED expexted x=1 and y=2 but got x =", x, " y =", y)

if __name__ == "__main__":
    basictest()
