class ExamResult:
    def __init__(self, name, score, grade=None, resitRequired=None):
        self.name = name
        self.score = score
        self.grade = grade
        self.resitRequired = resitRequired


student1 = ExamResult("one", 83, "B", False)
student2 = ExamResult("two", 50, "D", True)
student3 = ExamResult("three", 100, "A")

students = [student1, student2, student3]

for s in students:
    print(
        f"{s.name} scored {s.score} which achieved a grade {s.grade} and a resit is {s.resitRequired}"
    )

for s in students:
    s.grade = chr((ord(s.grade) + 1 - 65) % 26 + 65)