class Zasobnik:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def display(self):
        if self.is_empty():
            print("Zásobník je momentálne prázdny.")
        else:
            print("Aktuálny stav zásobníka:")
            for item in reversed(self.stack):
                print(f" - {item}")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    z = Zasobnik()
    z.push("auto")
    z.push("vlak")
    z.push("lietadlo")
    z.display()
    print(f"Počet položiek: {z.size()}")

    print(f"Vybral som: {z.pop()}")
    z.display()
