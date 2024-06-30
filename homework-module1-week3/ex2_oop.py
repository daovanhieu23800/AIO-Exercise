class Person():
    def __init__(self, name: str, yob: int) -> None:
        self.name = name
        self.yob = yob


class Student(Person):
    def __init__(self, name: str, yob: int, grade: float) -> None:
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"Student - Name: {self.name} - YOB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str) -> None:
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self.name} - YOB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self.name} - YOB: {self.yob} - Specialist: {self.specialist}")


class Ward():
    def __init__(self, name: str) -> None:
        self.name = name
        self.people_list = []

    def add_person(self, person: Person):
        self.people_list.append(person)

    def describe(self):
        print(f"Ward Name : {self.name}")
        for p in self.people_list:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.people_list:
            if isinstance(p, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.people_list.sort(reverse=True, key=lambda x: x.yob)

    def compute_average(self):
        age_avg = 0
        for p in self.people_list:
            age_avg += p.yob
        age_avg /= len(self.people_list)
        return age_avg


student1 = Student(name="studentA", yob=2010, grade="7")
student1 . describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1 . describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1 . describe()

teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(doctor1)
ward1.add_person(teacher2)
ward1.add_person(doctor2)
ward1.describe()

print(f"\nNumber of doctors: {ward1.count_doctor()}")
ward1.sort_age()
ward1.describe()
print(f"\nAverage year of birth(teachers): {ward1.compute_average()}")
