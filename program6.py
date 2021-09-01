from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int

def main():
    alice = Student('Alice', 12345)
    bob = Student('Bob', 456787)
    print(alice)
    print(bob)


main()