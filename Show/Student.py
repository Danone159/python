class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_subject(self, subject):
        if subject not in self.grades:
            self.grades[subject] = []
        else:
            print("Predmet už existuje.")

    def add_grade(self, subject, event, points, base):
        if subject in self.grades:
            self.grades[subject].append({"event": event, "points": points, "base": base})
        else:
            print("Najprv pridaj predmet.")

    def print_grades(self):
        for subject, grade_list in self.grades.items():
            print(f"Predmet: {subject}")
            for g in grade_list:
                print(f" - {g['event']}: {g['points']}/{g['base']}")

if __name__ == "__main__":
    s = Student(1, "Janko Hrasko")
    s.add_subject("Matematika")
    s.add_grade("Matematika", "Test 1", 8, 10)
    s.print_grades()
