from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: int


alex = Student('Alex', 'abcedf', 3.4)
print(alex)
print(alex.name)

