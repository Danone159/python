class Time:
    def __init__(self, hours, minutes):
        if not (0 <= hours < 24) or not (0 <= minutes < 60):
            raise ValueError("Neplatné hodnoty času.")
        self.hours = hours
        self.minutes = minutes

    def display(self):
        print(self.format_time())

    def format_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}"

    def shift(self, h, m):
        total_minutes = (self.hours * 60 + self.minutes + h * 60 + m) % (24 * 60)
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

if __name__ == "__main__":
    t = Time(14, 20)
    t.display()
    t.shift(3, 50)
    t.display()
