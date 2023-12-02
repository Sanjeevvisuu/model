import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_files.settings")
import django
django.setup()

from faker import Faker
faker = Faker()
from crud.models import students_data

def gen(n):
    for i in range(n):
        name = faker.name()
        std = faker.random_int(min=1, max=12)  # Assuming std is an integer between 1 and 12
        section = faker.random_letter()  # Assuming section is a single letter
        school = faker.company()
        ph_no = faker.phone_number()

        stu, created = students_data.objects.get_or_create(
            name=name, std=std, section=section, school=school, ph_no=ph_no
        )

        if created:
            print(f"Student created: {stu.name}")
        else:
            print("Student not created.")

# Example: Generate 10 fake students
gen(10)
