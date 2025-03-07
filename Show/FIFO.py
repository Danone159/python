class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None

    def show(self):
        if self.is_empty():
            print("Fronta je prázdna.")
        else:
            print("Fronta obsahuje:")
            print(" -> ".join(str(item) for item in self.queue))

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("pes")
    q.enqueue("mačka")
    q.enqueue("papagáj")

    q.show()
    print(f"Odstránený prvok: {q.dequeue()}")
    q.show()

    print(f"Odstránený prvok: {q.dequeue()}")
    print(f"Odstránený prvok: {q.dequeue()}")

    if q.dequeue() is None:
        print("Fronta je už prázdna.")
