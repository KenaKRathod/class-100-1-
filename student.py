class Student(object):
    def __init__(self, name, age, gender, level, grades=None) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}
    def setGrade(self, course, grade):
        self.grades[course] = grade
    def getGrade(self, course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
joan = Student("joan", 12, "male", 6, {"math":3.3})
hanna = Student("hanna", 20, "female", 9, {"math":3.5})
print(joan.getGPA())
print(hanna.getGPA())

