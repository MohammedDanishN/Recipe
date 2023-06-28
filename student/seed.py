from faker import Faker
from random import randint
from .models import *
fake = Faker()


def seed_student_marks(n=10):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subject_obj = Subject.objects.all()
            for subject in subject_obj:
                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=randint(0, 100)
                )
    except Exception as E:
        print(E)


def seed_db(n=10) -> None:

    try:
        for i in range(0, n):
            srn = f'STD{randint(101,999)}'
            dept_obj = Department.objects.all()
            dept_name = dept_obj[randint(0, len(dept_obj)-1)]
            name = fake.name()
            email = fake.email()
            age = randint(18, 25)
            address = fake.address()

            std_id_obj = StudentID.objects.create(srn=srn)

            std_obj = Student.objects.create(
                srn=std_id_obj,
                dept_name=dept_name,
                name=name,
                email=email,
                age=age,
                address=address
            )
    except Exception as e:
        print(e)
