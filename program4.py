
class Student:
    def __init__(self, name, school_id):
        self.name = name
        self.school_id = school_id

    def __str__(self):
        return f'Student name: {self.name}, school id: {self.school_id}'


alex = Student('Alex', 'abcdef')
print(alex.name)
print(alex.school_id)
print(alex)